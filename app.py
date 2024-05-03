from flask import Flask, request, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route('/video-info', methods=['POST'])
def get_video_info():
    youtube_link = request.json.get('youtubeLink')
    if not youtube_link:
        return jsonify({'error': 'YouTube link is required'}), 400

    video_info = get_youtube_video_info(youtube_link)
    if 'error' in video_info:
        return jsonify(video_info), 500
    else:
        return jsonify(video_info)

def get_youtube_video_info(youtube_link):
    try:
        yt = YouTube(youtube_link)
        video_info = {
            'title': yt.title,
            'duration': yt.length,
            'formats': []
        }

        # Download the highest resolution progressive stream
        stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
        if stream:
            video_info['formats'].append({
                'name': stream.abr,
                'url': stream.url
            })
            download_path = stream.download()
            video_info['download_path'] = download_path

        return video_info
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
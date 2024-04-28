from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def heelo_world():
    return "<p>Hey gusy wassup!</p>"

@app.route("/help")
def help():
    return jsonify(
        message = "hello"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

#function to fetch hostname and ip
def fetchDetails():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(hostname), str(ip)


@app.route("/")
def heelo_world():
    return "<p>Hey gusy wassup!</p>"

@app.route("/help")
def help():
    return jsonify(
        message = "hello"
    )

@app.route("/index", methods=["GET"])
def index_opage():
    hostname, ip = fetchDetails()
    return render_template("index.html", hostname=hostname, ip=ip)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
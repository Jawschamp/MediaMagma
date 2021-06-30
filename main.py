from APIs.SegDownloader.downloader import SegmentedDownloader



from flask import Flask, render_template

app = Flask(__name__)

@app.route("/test")
def hello():
    return render_template("mainlayout.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000)
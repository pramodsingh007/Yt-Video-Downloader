from flask import Flask, flash,render_template, request, url_for,redirect,get_flashed_messages
from YoutubeDownloader import YtDownloader
import os


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# d= YtDownloader("https://www.youtube.com/watch?v=JGu9PkpU3o8&list=RDMM&index=10")
# print(d.title)

id = ""
@app.route('/',methods=["POST","GET"])
def home():
    if request.method == "POST":
        link = request.form.get("url")
        d_video = YtDownloader(link=link)
        thumbanail=  d_video.thumbnail
        title = d_video.title
        global id
        id = d_video.id
        return render_template ('download.html',v_thumbnail = thumbanail,title=title)
        
    return render_template('index.html')

@app.route('/https://www.youtube.com/watch')
def download_page():
    try:
        global id
        id = request.args.get("v")
        d_video = YtDownloader(link=f"https://www.youtube.com/watch?v={id}")
        title = d_video.title
        thumbanail = d_video.thumbnail
    except:
        print("error")
    return render_template ('download.html',v_thumbnail = thumbanail,title=title)

@app.route('/download')
def download():
    d_video = YtDownloader(link=f"https://www.youtube.com/watch?v={id}")
    d_video.Download_video()
    flash("Video Successfully  Downloaded ")
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

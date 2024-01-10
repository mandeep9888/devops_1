from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://img.buzzfeed.com/buzzfeed-static/static/2020-05/13/22/asset/e477c1fe1aa3/sub-buzz-569-1589409692-5.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/2020-05/13/22/asset/389c33c2ebda/sub-buzz-666-1589409882-2.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/2020-05/13/23/asset/6f9a0cf3220a/sub-buzz-723-1589412782-14.png?downsize=600:*&output-format=auto&output-quality=auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/2020-05/13/22/asset/f1ecf6765b8f/sub-buzz-650-1589410005-23.jpg?crop=640:781;0,0&downsize=600:*&output-format=auto&output-quality=auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/2020-05/13/23/asset/cc967b792394/sub-buzz-77-1589413047-9.png?downsize=600:*&output-format=auto&output-quality=auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/2020-05/13/22/asset/ae698d94a25f/sub-buzz-604-1589410569-20.jpg?downsize=600:*&output-format=auto&output-quality=auto"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
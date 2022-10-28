from flask import Flask, render_template
import requests
import post

posts_api = "https://api.npoint.io/b1c641f654ac32a59f9c"
all_posts = requests.get(posts_api).json()
post_data = []
for each in all_posts:
    post_data.append(post.Post(each))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts = all_posts, id = 0)

@app.route('/post/<id>')
def get_post(id):
    return render_template("index.html", all_posts = [all_posts[int(id)-1]])


if __name__ == "__main__":
    app.run(debug=True)

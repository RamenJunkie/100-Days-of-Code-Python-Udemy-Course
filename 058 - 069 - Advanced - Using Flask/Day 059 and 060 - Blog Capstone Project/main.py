from flask import Flask, render_template, request
import requests
import post

#mailer = mailer_class.Mailer()

app = Flask(__name__)

posts_api = "https://api.npoint.io/3fedf8fd887c99909c24"
all_posts = requests.get(posts_api).json()
post_data = []
for each in all_posts:
    post_data.append(post.Post(each))



@app.route('/')
def home():
    return render_template("index.html", all_posts = all_posts, header_image="home")

@app.route('/about.html')
def about():
    return render_template("about.html", header_image="about")

@app.route('/contact.html')
def contact():
    return render_template("contact.html", header_image="contact", notice_msg=" ")

@app.route('/post_<id>')
def get_post(id):
    return render_template("post.html", post = all_posts[int(id)])

@app.route('/mail', methods=["POST", "GET"])
def mail_to():
    name = str(request.form.get("name"))
    email = request.form.get("email")
    message = request.form.get("message")

    email_text = f"Subject: Blog Contact\n\nFrom: {name},\nEmail: {email}\n\n{message}"
    print(email_text)
    #mailer.send_email(email_text)
    return render_template("contact.html", header_image="contact", notice_msg="Message Sent Successfully!")

if __name__ == "__main__":
    app.run(debug=True)

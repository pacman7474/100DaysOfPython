from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/674f5423f73deab1e9a7"
    response = requests.get(blog_url)
    blog_json = response.json()
    h1_title = "Phillip's Blog"
    h2_subtitle = "Catch up on what I'm doing"
    return render_template("old_index.html",my_img="home-bg.jpg",posts=blog_json,h1_title=h1_title,h2_subtitle=h2_subtitle)

@app.route('/about')
def about():
    h1_title = "About Me"
    h2_subtitle = "This is what I do"
    return render_template("about.html",my_img="about-bg.jpg",h1_title=h1_title,h2_subtitle=h2_subtitle)

@app.route('/contact')
def contact():
    h1_title = "Contact Me"
    h2_subtitle = "Have questions? I have answers"
    return render_template("contact.html",my_img="contact-bg.jpg",h1_title=h1_title,h2_subtitle=h2_subtitle)


@app.route('/post/<int:num>')
def post(num):
    blog_url = "https://api.npoint.io/674f5423f73deab1e9a7"
    response = requests.get(blog_url)
    blog_json = response.json()
    h1_title = ""
    h2_subtitle = ""
    content = ""
    image_url = ""
    for blog in blog_json:
        print(blog["id"])
        print(num)
        if blog["id"] == num:
            h1_title = blog["title"]
            h2_subtitle = blog["subtitle"]
            content = blog["body"]
            image_url = blog["image_url"]

    return render_template("post.html",my_img="post-bg.jpg",post=content,h1_title=h1_title,h2_subtitle=h2_subtitle,image_url=image_url)


if __name__ == "__main__":
    app.run(debug=True)

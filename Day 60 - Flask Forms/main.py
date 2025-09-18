from flask import Flask, render_template, request
import requests
import smtplib

my_email = "phillip.dev.ops@gmail.com"
password = "pmvo zpmq csqe ihlq"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=["POST","GET"])
def contact():
    if request.method == "POST":
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=request.form["email"],
                msg=f"Subject:{request.form['name']}: Contact Me\n\n{request.form['message']}")
        title="Successfully sent your message"
        return render_template("contact.html",title=title)
    else:
        title="Contact Me"
        return render_template("contact.html",title=title)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

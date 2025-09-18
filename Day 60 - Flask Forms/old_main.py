from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("old_index.html")

@app.route('/login',methods=["Post"])
def login():
    return render_template("login.html",username=request.form['username'],password=request.form['password'])



if __name__ == "__main__":
    app.run(debug=True)

from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Dewi"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {
            "author": {"username": "Susan"},
            "body": "The Avengers movie was so cool!",
        },
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/about")
def about():
    user = {"username": "Dewi"}
    return render_template("about.html", user=user)


if __name__ == "__main__":
    app.run()

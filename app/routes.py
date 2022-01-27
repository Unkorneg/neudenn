from flask import Flask


@app.route("/")
def index():
    return "Hello world !"


@app.route("/about")
def about():
    return "This is the about page"


if __name__ == "__main__":
    app.run()

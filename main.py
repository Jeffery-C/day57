from flask import Flask, render_template
import requests

app = Flask(__name__)

data_url = "https://api.npoint.io/39b677c948e74c2e7f5d"
response = requests.get(url=data_url)
response.raise_for_status()
data = response.json()


@app.route('/')
def home():
    return render_template("index.html", data=data)


@app.route("/post/<int:num>}")
def get_post(num):
    post_data = None
    for post in data:
        if int(post["id"]) == num:
            post_data = post
    return render_template("post.html", post=post_data)


if __name__ == "__main__":
    app.run(debug=True)

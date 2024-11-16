from flask import Flask, render_template, request
from replies import replies

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    selected_action = request.form.get("action") if request.method == "POST" else ""

    actions = list(replies.keys())

    return render_template("index.html", actions=actions, selected_action=selected_action, replies=replies)

if __name__ == "__main__":
    app.run(debug=False)
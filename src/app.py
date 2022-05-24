from flask import Flask, render_template, request
from markupsafe import escape
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<name>")
def hello(name):
    return f"ECHO: {escape(name)}!"


@app.route("/echo", methods=["POST", "GET"])
def echo():
    result = ""
    if request.method == "POST":
        # for key in request.form:
        #     result = result + f"{key} : {request.form[key]}\n"
        return render_template("echo.html", request_info=request.form)
    else:
        result = "Unsupported Operation"
        return f"Result:\n{result}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

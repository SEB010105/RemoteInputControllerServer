import pyautogui
from flask import Flask, request, render_template
from flask_cors import CORS
from markdown import markdown


app = Flask(__name__,)
CORS(app)


actions = {
    "press": lambda x: pyautogui.press(x),
    "down": lambda x: pyautogui.keyDown(x),
    "up": lambda x: pyautogui.keyUp(x),
    "write": lambda x: pyautogui.write(x)
}


@app.route("/")
def show_read_me():
    readme = open("readme.md").read()
    styling = "<style>" + open("style.css").read() + "</style>"

    mkd_text = markdown(styling + readme, extensions=["fenced_code"])

    return mkd_text


@app.route("/test", methods=["POST"])
def handle_post():
    json = request.get_json(force=True)

    try:
        action = json["action"].lower()
        content = json["content"]

        actions[action](content)
    except KeyError:
        return "Invalid Input", 400

    return ""


app.run(
    debug=True,
    port=5000,
    host="0.0.0.0"
)

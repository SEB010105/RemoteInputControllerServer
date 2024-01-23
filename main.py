import pyautogui
from flask import Flask, request, render_template
from flask_cors import CORS
from markdown import markdown


app = Flask(__name__,)
CORS(app)


def handle_action(action):
    json = request.get_json(force=True)

    action(json)

    return ""


@app.route("/")
def show_read_me():
    readme = open("readme.md").read()
    styling = "<style>" + open("style.css").read() + "</style>"

    mkd_text = markdown(styling + readme, extensions=["fenced_code"])

    return mkd_text


@app.route("/press", methods=["POST"])
def press():
    return handle_action(
        lambda json: pyautogui.press(json["key"])
    )


@app.route("/write", methods=["POST"])
def write():
    return handle_action(
        lambda json: pyautogui.write(json["keys"])
    )


@app.route("/down", methods=["POST"])
def down():
    return handle_action(
        lambda json: pyautogui.keyDown(json["key"])
    )


@app.route("/up", methods=["POST"])
def up():
    return handle_action(
        lambda json: pyautogui.keyUp(json["key"])
    )


@app.route("/click", methods=["POST"])
def click():
    return handle_action(
        lambda json: pyautogui.click(x=json["x"], y=json["y"], button=json["button"])
    )


app.run(
    debug=True,
    port=5000,
    host="0.0.0.0"
)

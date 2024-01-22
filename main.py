import pyautogui
from flask import Flask, request


app = Flask(__name__)

actions = {
    "press": lambda x: pyautogui.press(x),
    "down": lambda x: pyautogui.keyDown(x),
    "up": lambda x: pyautogui.keyUp(x),
    "write": lambda x: pyautogui.write(x)
}


@app.route("/", methods=["POST"])
def handle_post():
    json = request.get_json()

    try:
        action = json["action"].lower()
        content = json["content"]

        actions[action](content)
    except KeyError:
        return "Invalid Input", 400

    return ""


app.run(debug=True, port=5000)

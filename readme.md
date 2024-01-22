### Usage
Post a JSON to `localhost:PORT` (default PORT: 5000)

Example JSON to press `w` on the keyboard.
```json
{
    "action": "press",
    "content": "w"
}
```

The attribute `action` is a string which defines what the application does.

List of actions:
- press
- down
- up
- write

The attribute `content` tells the application what button to press or text to write.

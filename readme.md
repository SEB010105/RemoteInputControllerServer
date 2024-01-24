## Usage
Post a JSON to one of the endpoints of `localhost:PORT`. (default PORT: 5000)

## Endpoints
### /press
Presses a key once.

Attribute:

- `key: string` key to be pressed

### /write
Writes multiples keys in quick succession.

Attribute:

- `keys: string` keys to be written

### /down
Holds down a key.

Attribute: 

- `key: string` key to be held down

### /up
Releases a held down key.

Attribute

- `key: string` : key to be released

### /click
Clicks using the mouse.

Attributes: 

- `x: numver` x coordinate of click
- `y: number` y coordinate of click 
- `button: string` button to be clicked

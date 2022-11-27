# WInput

Simple Windows-oriented library to read raw input from console using multithreading

## Example

```py
def listener(key: Key):
    print(f"Got {key} from keyboard")

keyboard = WInput()
keyboard.subscribe(listener) # Add new listener

keyboard.run() # Run WInput in a new thread
keyboard.join() # Joins WInput thread to parernt thread, inherited from Thread class
```
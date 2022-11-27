# CWInput

Simple Windows-oriented library to read raw input from console using multithreading.

## Installation

You can get this package from [PyPi](https://pypi.org/project/cwinput/)


```sh
pip install cwinput
```

## Example

```py
def listener(key: Key):
    print(f"Got {key} from keyboard")

keyboard = CWInput()
keyboard.subscribe(listener) # Add new listener

keyboard.run() # Run CWInput in a new thread
keyboard.join() # Joins CWInput thread to parent thread, inherited from Thread class
```
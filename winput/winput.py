import msvcrt
from threading import Thread
from typing import Callable

from winput.binds import Keys


# Type hint alias
Key = Keys | str


class WInput(Thread):
    """
    Simple multithreading Windows library for reading raw input from console.

    Example:
    ```
    def listener(key: Key):
        print(f"Got {key} from keyboard")

    keyboard = WInput()
    keyboard.subscribe(listener) # Add new listener

    keyboard.run() # Run WInput in a new thread
    ```
    """

    listeners = []

    def __init__(self) -> None:
        super(WInput, self).__init__()
        self.running = False

    def subscribe(self, func: Callable) -> None:
        """
        Add new listener

        NOTE: Listener should accept only one parameter 
        """
        self.listeners.append(func)

    def unsubscribe(self, func: Callable) -> None:
        """
        Remove listener from list
        """
        self.listeners.remove(func)

    def run(self) -> None:
        """
        Start listening to console input
        """
        self.running = True

        while self.running:
            char = msvcrt.getwch()
            char = Keys.get(char) or char

            if char.encode("utf-8") == Keys.ESCAPE_SEQ_WIDE.value:
                gch = msvcrt.getwch().encode("utf-8")
                char = Keys.get(gch, True) or char

            for listener in self.listeners:
                listener(char)

    def stop(self) -> None:
        """
        Stop listening to updates
        """
        self.running = False

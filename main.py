import keyboard
import pyautogui
from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed:
        if button.name == 'left':
            print(f"Left mouse button clicked at ({x}, {y})")

def clickFunction(r: int):
    pyautogui.click(button="left", clicks=r, interval=0.01)

if __name__ == '__main__':
    # activation -> ctrl + shift + i
    keyboard.wait("ctrl+alt+m")
    print("activation successfull")
    with Listener(on_click=on_click) as listener:
        listener.join()
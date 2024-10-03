import keyboard
import pyautogui

def clickFunction(r: int):
    pyautogui.click(button="left", clicks=r, interval=0.01)

if __name__ == '__main__':
    # activation -> ctrl + shift + i
    keyboard.wait("ctrl+alt+m")
    print("activation successfull")
    clickFunction(10^1000)
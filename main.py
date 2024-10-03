import keyboard
import pyautogui

def clickFunction(r: int):
    for i in range(r):
        pyautogui.leftClick()

if __name__ == '__main__':
    # activation -> ctrl + shift + i
    keyboard.wait("ctrl+shift+i")
    print("activation successfull")
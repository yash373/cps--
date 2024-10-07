import keyboard
import pyautogui

if __name__ == '__main__':
    cps = int(input("Enter desired cps: "))
    print("Press 'b' to get started")
    
    while True:
        # activation -> ctrl + shift + i
        keyboard.wait("b")
        print("activation successfull")
        pyautogui.click(button="left",clicks=cps,interval=1/60)
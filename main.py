#from pynput import keyboard
import os
import time

mainMenuString = "AUTO OFFLINE CLIENT\n\n[1] Start\n[2] Stop Shutdown\n[3] Settings & Help\n[4] Exit"

def mainMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(mainMenuString)

    opt = input("\nSelect an option: ")

    if opt.isdigit():
        opt = int(opt)
        if opt == 1:
            print("1")
        elif opt == 2:
            print("2")
        elif opt == 3:
            print("3")
        elif opt == 4:
            print("\n\nThanks for using! :)")
            print("Exiting...")
            exit(0)
        else:
            print("Invalid option. Please try again.")
            time.sleep(0.3)
            mainMenu()
    else:
        print("Invalid option. Please try again.")
        time.sleep(0.3)
        mainMenu()


def start():
    print("start")

def stopShutdown():
    print("stopShutdown")

def settingsHelp():
    print("settingsHelp")


if __name__ == "__main__":
    mainMenu()
#from pynput import keyboard
import os
import time

mainMenuString = "[1] Start\n[2] Stop Shutdown\n[3] Settings & Help\n[4] Exit"
headerString = "AUTO OFFLINE CLIENT\n"

def mainMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(headerString)
    print(mainMenuString)

    opt = input("\nSelect an option: ")

    if opt.isdigit():
        opt = int(opt)
        if opt == 1:
            start()
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
    os.system('cls' if os.name == 'nt' else 'clear')

    if os.name == 'nt':
        print(headerString)
        print("Enter amount with s for seconds, m for minutes, h for hours, and d for days.\nExample: 42m = 42 minutes\n")
        opt = input("Pick amount: ")

        if opt.isdigit() == False: # If opt does not contain any Format
            format = opt[-1]
            opt = opt[:-1]

            if opt.isdigit():
                time = int(opt)
            else:
                print("Invalid option. Please try again.")
                time.sleep(0.3)
                start()

            if format == "m":
                time = time * 60
            elif format == "h":
                time = time * 3600
            elif format == "d":
                time = time * 86400

            if time > 312206400: # 9,9 Years
                print("You exceeded the maximum time limit of 10 Years. Please try again.")
                time.sleep(1)
                start()
            else: 
                shutdown(time)
        else:
            print("Invalid input. Please try again.")
            time.sleep(0.3)
            start()
    
    else:
        print(headerString)
        print("Enter amount with m for minutes, h for hours, and d for days.\nExample: 42m = 42 minutes\nNote: Seconds are not supported in Unix.\n")
        opt = input("Pick amount: ")

        if opt.isdigit() == False: # If opt does not contain any Format
            format = opt[-1]
            opt = opt[:-1]

            if opt.isdigit():
                time = int(opt)
            else:
                print("Invalid option. Please try again.")
                time.sleep(0.3)
                start()

            if format == "h":
                time = time * 60
            elif format == "d":
                time = time * 1440

            shutdown(time)
        else:
            print("Invalid input. Please try again.")
            time.sleep(0.3)
            start()



    # if opt.isdigit():
    #     opt = int(opt)
    #     print(opt)
    #     shutdown(opt)
    # else:
    #     print("Invalid option. Please try again.")
    #     time.sleep(0.3)
    #     mainMenu()

def stopShutdown():
    print("stopShutdown")

def settingsHelp():
    print("settingsHelp")


def shutdown(time):
    if os.name == 'nt':
        try:
            resp = os.system("shutdown -s -t " + str(time))
        except:
            print("Error occurred. Trying again...")
            os.system("shutdown /a")
            shutdown(time)

        if resp == 1190:
            print("Shutdown already in progress. Cancelling...")
            os.system("shutdown /a")
            shutdown(time)

    elif os.name == 'posix':
        try:
            os.system("sudo shutdown -h +" + str(time))
        except:
            print("Error occurred. Trying again...")
            os.system("shutdown -c")
            shutdown(time)
    else:
        print("Unkown Operating System.\nTry Unix Shutdown?")
        cont = input("(y/n): ")
        if cont.lower() == "y":
            try:
                os.system("sudo shutdown -h +" + str(time))
            except:
                print("Error occurred. Trying again...")
                os.system("shutdown /c")
                shutdown(time)
        else:
            print("Returning to main menu...")
            time.sleep(0.3)
            mainMenu()



if __name__ == "__main__":
    mainMenu()
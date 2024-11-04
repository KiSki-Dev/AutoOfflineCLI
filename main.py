#from pynput import keyboard
import os
import time
import webbrowser
import requests
import pathlib

mainMenuString = "[1] Start\n[2] Stop Shutdown\n[3] About & Help\n[4] Exit"
headerString = "AUTO OFFLINE CLIENT\n"
version = 0.3
updateURL = "https://raw.githubusercontent.com/KiSki-Dev/AutoOfflineCLI/refs/heads/main/versions.json"

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
            stopShutdown()
        elif opt == 3:
            aboutHelp()
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
        print("\nEnter amount with s for seconds, m for minutes, h for hours, and d for days.\nExample: 42m = 42 minutes\n")
        opt = input("Pick amount: ")

        if opt.isdigit() == False: # If opt does not contain any Format
            format = opt[-1]
            opt = opt[:-1]

            if opt.isdigit():
                amount = int(opt)
            else:
                print("Invalid option. Please try again.")
                time.sleep(0.3)
                start()

            if format == "m":
                amount = amount * 60
            elif format == "h":
                amount = amount * 3600
            elif format == "d":
                amount = amount * 86400

            if amount > 312206400: # 9,9 Years
                print("You exceeded the maximum time limit of 10 Years. Please try again.")
                time.sleep(1)
                start()
            else: 
                shutdown(amount)
        else:
            print("Invalid input. Please try again.")
            time.sleep(0.8)
            start()
    
    else:
        print(headerString)
        print("Enter amount with m for minutes, h for hours, and d for days.\nExample: 42m = 42 minutes\nNote: Seconds are not supported in Unix.\n")
        opt = input("Pick amount: ")

        if opt.isdigit() == False: # If opt does not contain any Format
            format = opt[-1]
            opt = opt[:-1]

            if opt.isdigit():
                amount = int(opt)
            else:
                print("Invalid option. Please try again.")
                time.sleep(0.3)
                start()

            if format == "h":
                amount = amount * 60
            elif format == "d":
                amount = amount * 1440

            shutdown(amount)
        else:
            print("Invalid input. Please try again.")
            time.sleep(0.8)
            start()


def stopShutdown():
    if os.name == 'nt':
        try:
            os.system("shutdown -a")
        except:
            print("Error occurred. Please try again.")
        time.sleep(1)

    elif os.name == 'posix':
        try:
            os.system("shutdown -c")
        except:
            print("Error occurred. Please try again.")
        time.sleep(1)

    else:
        print("Unkown Operating System.\nTry Unix Stop Shutdown?")
        cont = input("(y/n): ")
        if cont.lower() == "y":
            try:
                os.system("shutdown -c")
            except:
                print("Error occurred. Please try again.")
            time.sleep(1)
        else:
            print("Returning to main menu...")
            time.sleep(0.3)

    mainMenu()

def shutdown(amount):
    if os.name == 'nt':
        try:
            resp = os.system("shutdown -s -t " + str(amount))
        except:
            print("Error occurred. Trying again...")
            os.system("shutdown -a")
            shutdown(amount)

        if resp == 1190:
            print("Shutdown already in progress. Cancelling...")
            os.system("shutdown -a")
            shutdown(amount)

        time.sleep(1)

    elif os.name == 'posix':
        try:
            os.system("sudo shutdown -h +" + str(amount))
        except:
            print("Error occurred. Trying again...")
            os.system("shutdown -c")
            shutdown(amount)
        time.sleep(1)

    else:
        print("Unkown Operating System.\nTry Unix Shutdown?")
        cont = input("(y/n): ")
        if cont.lower() == "y":
            try:
                os.system("sudo shutdown -h +" + str(amount))
            except:
                print("Error occurred. Trying again...")
                os.system("shutdown -c")
                shutdown(amount)
            time.sleep(1)
        else:
            print("Returning to main menu...")
            time.sleep(0.3)

    mainMenu()

def aboutHelp():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(headerString)
    print("[1] About\n[2] Help\n[3] Back")

    opt = input("\nSelect an option: ")

    if opt.isdigit():
        opt = int(opt)
        if opt == 1:
            about()
        elif opt == 2:
            help()
        elif opt == 3:
            mainMenu()
        else:
            print("Invalid option. Please try again.")
            time.sleep(0.3)
            aboutHelp()
    else:
        print("Invalid option. Please try again.")
        time.sleep(0.3)
        aboutHelp()

def about():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(headerString)
    print("[1] Check for Updates\n[2] GitHub\n[3] Discord Support Server")

    opt = input("\nSelect an option: ")

    if opt.isdigit():
        opt = int(opt)
        if opt == 1:
            checkForUpdate()
        elif opt == 2:
            webbrowser.open("https://github.com/KiSki-Dev", new=2)
            input("\nOpening 'https://github.com/KiSki-Dev'")
            mainMenu()

        elif opt == 3:
            webbrowser.open("https://discord.com/invite/cYqpx7dqsn", new=2)
            input("\nOpening 'https://discord.com/invite/cYqpx7dqsn'")
            mainMenu()

        else:
            print("Invalid option. Please try again.")
            time.sleep(0.3)
            aboutHelp()
    else:
        print("Invalid option. Please try again.")
        time.sleep(0.3)
        aboutHelp()

def help():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(headerString)
    print("You can select your time until shutdown using the following units:\ns = seconds | m = minutes | h = hours | d = days | w = weeks\n\nYou can also use the following quick Parameters.")

    input("\nPress enter to get back to the Main Menu.")
    mainMenu()

def checkForUpdate():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(headerString)

    response = requests.get(updateURL)

    if response.status_code == 200:
        data = response.json()

        newestData = data["versions"]["newest"]

        if version != newestData["version"]:
            # Check if Dev
            currentData = data["versions"]["old"][str(version)]

            print("Update avaible!\n\nCurrent Version: " + str(version) +  "\nRelease Date: " + str(currentData["date"]) + "\nUpdate-Title: " + str(currentData["title"]) + "\n\nNewest Version: " + str(newestData["version"]))
            input("\n\nPress enter to update AutoOffline!")

            downloadURL = "https://github.com/KiSki-Dev/AutoOfflineCLI/releases/latest/download/main.py"
            downloadPath = pathlib.Path(__file__).parent.resolve()
            response = requests.get(downloadURL, stream=True)
            file_path = os.path.join(downloadPath, "main.py")
            print("Downloading...")

            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    print("Updating...")
                    file.write(chunk)

        if version == newestData["version"]:
            print("No Update avaible!\n\nCurrent Version: " + str(version) +  "\nRelease Date: " + str(newestData["date"]) + "\nUpdate-Title: " + str(newestData["title"]))
            input("\nPress enter to get back to the Main Menu.")
            mainMenu()
    else:
        print("There has been a Error checking for Updates. Please check your WiFi Connection.")



if __name__ == "__main__":
    mainMenu()
import os 
import sys

def sel_intel():
    print("You have switched to your intel integrated driver. ")
    print('NOTE: When switching primary graphic drivers, restarting your pc is required. Rebooting may require root privileges.\n')

    os.system("sudo prime-select intel")

def sel_nvidia():
    print("You have selected to your nvidia driver. ")
    print('NOTE: When switching primary graphic drivers, restarting your pc is required. Rebooting may require root privileges.\n')

    os.system("sudo prime-select nvidia")
    
def rmv_nvidia():
    os.system("sudo apt purge nvidia-*")

def rbt():
    os.system('sudo reboot')

def quit():
     sys.exit(0)


def menu():
    print('----------------------------------------------------------')
    print('                 Python GPU Switcher for Linux            ')
    print('----------------------------------------------------------')

    print("The current graphics driver in use is: ")
    os.system("prime-select query")

    print("                  ")


    print('1) Select Intel GPU')
    print('2) Select Nvidia GPU')
    print('3) Delete Nvidia Drivers')
    print('4) Show GPU in use')
    print('5) Reboot')
    print('6) exit')


def main():
    while True:
        menu()

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number 1 through 4.")
            continue
        if choice == 1:
            sel_intel()
        elif choice == 2:
            sel_nvidia()
        elif choice == 3:
            rmv_nvidia()
        elif choice == 4:
            display_used()
        elif choice == 5:
            rbt()
        elif choice == 6:
            quit()

            
if __name__ == "__main__": 
	main()
    

import time
def Start():
    print("Welcome to...")
def Title():
    print("   ____ ___  _   _ ____   ___  _     _____  __        ___    ____   ")
    print("  / ___/ _ \| \ | / ___| / _ \| |   | ____| \ \      / / \  |  _ \  ")
    print(" | |  | | | |  \| \___ \| | | | |   |  _|    \ \ /\ / / _ \ | |_) | ")
    print(" | |__| |_| | |\  |___) | |_| | |___| |___    \ V  V / ___ \|  _ <  ")
    print("  \____\___/|_| \_|____/ \___/|_____|_____|    \_/\_/_/   \_\_| \_\ (fullscreen)")
Start()
time.sleep(2)
Title()
Life = 100
exper = 0
PlName = input("Insert your name -->")
print("Welcome to this adventure", PlName)
print("You have ❤️",Life, "life")
print("You have 🟢",exper, "xp")
ContAdv = input("Do you want to start this adventure (y/n)")
if ContAdv == "n":
    exit() 
elif ContAdv == "y":
    print("Let´s go!")
else:
    print("Incorrect value!")
    ContAdv()
print("In a city so far far away is a couple of brothers named Joe and Jack who they are thieves and plans bad things for the city...")
time.sleep(7)
print("Fortunately", PlName, "protects the city against this bad couple!")
time.sleep(3)
print("07-24-2023")
time.sleep(10)
print(PlName,":What a nice day to sit down and relax... With no problems outside")
time.sleep(2)
print("BOOM")
time.sleep(1)
print(PlName,"NO!. What exploded!?")
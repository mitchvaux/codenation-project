import time
print("Hello there and welcome to...")
time.sleep (2)
print ("Corona Zombies!")
time.sleep (2)
print("Will your bowels be eaten or will you be sipping on a nice cold beer? Lets find out...")
time.sleep (2)
print("But before we start..")
global name
time.sleep (2)
name = input("What is your name? ")
def end():
    time.sleep(2)
    print(f"\n \nCongratulations {name}, you have survived the zombie apocalypse!!!!!")
    time.sleep(3)
    final_choice = input("Do you want to play again? (yes/no): ").lower().strip()
    if final_choice ==  "yes" or final_choice == "y":
        start_game()
    elif final_choice == "no" or final_choice == "n":
        time.sleep(1)
        print("Oh, it's like that is it? Fine then... Bye!")
    else:
        time.sleep(1)
        print('You can\'t even type "yes" or "no" into a computer so you don\'t get to play our game')
def chapter_seven():
    time.sleep(2)
    print("\nYou continue walking through the city.")
    time.sleep(2)
    print("Where are you going next.")
    time.sleep(2)
    print("To the winchester for a cold pint?")
    time.sleep(2)
    print("To the shopping center to endlessly slay zombies?")
    time.sleep(2)
    print("Or home to relax?")
    choice8 = input("(pub/shopping/home): ").lower().strip()
    if choice8 == "pub":
        print("You fight your way to The Winchester,")
        time.sleep(1.5)
        print("where you have a nice cold pint and wait for all this to blow over")
        end()
    elif choice8 == "shopping":
        print("You fight your way to the shopping center,")
        time.sleep(1.5)
        print("where you spend your days endlessly killing the undead!")
        end()
    elif choice8 == "home":
        print("You fight your way home,")
        time.sleep(1.5)
        print("where you decide to make a text based adventure game to pass the time")
        end()
    else:
        print("Invalid Command")
        chapter_seven()
def chapter_six():
    time.sleep(2)
    print("\nArmed with your crowbar you explore the ruined city,")
    time.sleep(2)
    print("where you find an empty car with the keys in it.")
    time.sleep(2)
    choice7 = input("Do you take the car or continue on foot (car/walk): ").lower().strip()
    if choice7 == "walk":
        chapter_seven()
    elif choice7 == "car":
        print("You didn't check how much fuel it had in it!")
        time.sleep(2)
        print("It runs out and you're left stranded in the road.")
        time.sleep(2)
        print("The zombies see you and attack,")
        time.sleep(2)
        print("you fight them off for as long as you can but exentualy you are overrun and eaten alive")
        time.sleep(2)
        print(f"\n{name} was eaten alive by zombies")
        time.sleep(3)
        final_choice = input("Do you want to play again? (yes/no): ").lower().strip()
        if final_choice ==  "yes" or final_choice == "y":
            start_game()
        elif final_choice == "no" or final_choice == "n":
            time.sleep(1)
            print("Oh, it's like that is it? Fine then... Bye!")
        else:
            time.sleep(1)
            print('You can\'t even type "yes" or "no" into a computer so you don\'t get to play our game')
    else:
        print("Invalid Command")
        chapter_six()
def chapter_five():
    time.sleep(2)
    print("\nYou take the crowbar and head outside, ready for a fight")
    time.sleep(2)
    choice6 = input("Do you want explore or return home? (explore/home): ").lower().strip()
    if choice6 == "explore":
        chapter_six()
    elif choice6 == "home":
        print("\nYou decide it's time to return home to avoid the chaos.")
        time.sleep(2)
        print("When you get there you play call of duty zombies while the rest of the world falls into anarchy.")
        time.sleep(2)
        print(f"\ncongratulations {name}, you have survived the zombie apocalypse!!!")
        time.sleep(3)
        final_choice = input("Do you want to play again? (yes/no): ").lower().strip()
        if final_choice ==  "yes" or final_choice == "y":
            start_game()
        elif final_choice == "no" or final_choice == "n":
            time.sleep(1)
            print("Oh, it's like that is it? Fine then... Bye!")
        else:
            time.sleep(1)
            print('You can\'t even type "yes" or "no" into a computer so you don\'t get to play our game')
    else:
        print("Invalid Command")
        chapter_five()
def chapter_four():
    time.sleep(2)
    print("\nYou run to your local hardware store, being careful to avoid the zombies that prowl the streets")
    time.sleep(2)
    print("Inside the store you find a crowbar and a broom.")
    time.sleep(2)
    choice5 = input("Which one will you take? (crowbar/broom): ").lower().strip()
    if choice5 == "crowbar":
        chapter_five()
    elif choice5 == "broom":
        print("\nYou take your broom outside, ready to fight off the zombies")
        time.sleep(2)
        print("Sadly you are immediately killed because you chose a broom as a weapon.")
        time.sleep(2)
        print("If it makes you feel better the zombies used the broom to clean up your remains")
        time.sleep(2)
        print(f"{name} was killed by the undead!!!")
        time.sleep(3)
        final_choice = input("Do you want to play again? (yes/no): ").lower().strip()
        if final_choice ==  "yes" or final_choice == "y":
            start_game()
        elif final_choice == "no" or final_choice == "n":
            time.sleep(1)
            print("Oh, it's like that is it? Fine then... Bye!")
        else:
            time.sleep(1)
            print('You can\'t even type "yes" or "no" into a computer so you don\'t get to play our game')
    else:
        print("Invalid Command")
        chapter_four()
def chapter_three():
    time.sleep(2)
    print("\nYou run for your life, dodging fires and the undead.")
    time.sleep(2)
    print("Eventualy you escape the zombie horde.")
    time.sleep(2)
    choice4 = input("Do you want to go find food or find weapons? (food/weapons): ").lower().strip()
    if choice4 == "weapons" or choice4 == "weapon":
        chapter_four()
    elif choice4 == "food":
        print("\nYou run to your local takeout and find piles of food,")
        time.sleep(2)
        print("thinking your safe you walk in where you're ambushed by zombies.")
        time.sleep(2)
        print("You fight as hard as you can but without weapons you easily get overrun")
        time.sleep(2)
        print("The zombies end up eating you instead of the takeout food!!!")
        time.sleep(2)
        print(f"\n \n{name} has been eaten alive by the undead!!!")
        time.sleep(3)
        final_choice = input("Do you want to play again? (yes/no): ").lower().strip()
        if final_choice ==  "yes" or final_choice == "y":
            start_game()
        elif final_choice == "no" or final_choice == "n":
            time.sleep(1)
            print("Oh, it's like that is it? Fine then... Bye!")
        else:
            time.sleep(1)
            print('You can\'t even type "yes" or "no" into a computer so you don\'t get to play our game')
    else:
        print("Invalid Command")
        chapter_three()
def chapter_two():
    time.sleep(2)
    print("\nYou step outside your house to see the world on fire.")
    time.sleep(2)
    print("People run down the street screeming while the slow ones are ripped apart by the undead.")
    time.sleep(2)
    print("Infront of you stands a zombie!")
    time.sleep(2)
    choice3 = input("Do you run or fight (run/fight): ").lower().strip()
    if choice3 == "run":
        chapter_three()
    elif choice3 == "fight":
        print("\nYou try to atack the zombie but you have no weapons.")
        time.sleep(2)
        print("You struggle with the zombie but you are eventualy eaten alive!!!")
        time.sleep(2)
        print(f"{name} died!!!")
        time.sleep(3)
        final_choice = input("Do you want to play again? (yes/no): ").lower().strip()
        if final_choice ==  "yes" or final_choice == "y":
            start_game()
        elif final_choice == "no" or final_choice == "n":
            time.sleep(1)
            print("Oh, it's like that is it? Fine then... Bye!")
        else:
            time.sleep(1)
            print('You can\'t even type "yes" or "no" into a computer so you don\'t get to play our game')
    else:
        print("Invalid Command")
        chapter_two()
def chapter_one():
    time.sleep(2)
    print("\nLET'S BEGIN!!!")
    time.sleep(2)
    print("\nYou've woken up and seen on the TV an announcement from Boris,")
    time.sleep(2)
    print("he's saying that there is a deadly new disease going around,")
    time.sleep(2)
    print("causing chaos throughout the world!!!")
    time.sleep(2)
    choice2 = input("Do you want to stay at home or leave for supplies (stay/leave): ").lower().strip()
    if choice2 == "leave":
        chapter_two()
    elif choice2 == "stay":
        print("\nYou stay inside and continue to watch TV,")
        time.sleep(2)
        print("you are completely safe.")
        time.sleep(2)
        print("You learned a lot about the new disease.")
        time.sleep(2)
        print("You learned to social distance and wear a mask")
        time.sleep(2)
        print(f"Thank you {name}, you protected the NHS!!!")
        time.sleep(3)
        final_choice = input("Do you want to play again? (yes/no): ").lower().strip()
        if final_choice ==  "yes" or final_choice == "y":
            start_game()
        elif final_choice == "no" or final_choice == "n":
            time.sleep(1)
            print("Oh, it's like that is it? Fine then... Bye!")
        else:
            time.sleep(1)
            print('You can\'t even type "yes" or "no" into a computer so you don\'t get to play our game')
    else:
        print("Invalid Command")
        chapter_one()
def start_game():
    time.sleep(0.5)
    print(f"Hello {name}!")
    time.sleep(2)
    print("We are The A Team")
    time.sleep(2)
    print("Created by Marcus Drury, Mitch Shone and Dan Robinson")
    time.sleep(2)
    choice1 = input("Do you want to play our game? (yes/no): ").lower().strip()
    if choice1 == "yes" or choice1 == "y":
        chapter_one()
    elif choice1 == "no" or choice1 == "n":
        print("Oh, it's like that is it? Fine then... Bye!")
    else:
        print("Invalid Command")
        start_game()
start_game()






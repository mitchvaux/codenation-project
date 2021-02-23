def start ():
    start()
global name
name = input("Enter your name: ")
print("Hello", name + " We are the A team @ codenation created by marcus dury,mitch shone,dan robinson  welcome to our text based survival")

answer = input("do you want to play (yes/no)")

if answer.lower().strip() == "yes":
    answer = input ("Welcome to corona zombies You have woken up and turn on the tv to see an announcement from Biff Boris giving an introduction to covid 19.")

elif answer.lower().strip() == "no":
    answer = input ("unlucky your playing anyway lol")

answer = input ("Do you want to stay inside or leave (stay/run)")

if answer == "stay":
    answer = input ("You stay inside and continue to watch TV and you're completely safe. You learned about covid19 You learned to social distance wear a mask and you protected the nhs thankyou after a week you decide to go for a run")
    
elif answer == "run":
    answer = input ("You step outside your flat and encounter a zombie ahhhhhhh ")

answer = input ("Do you fight/flight ?")

if answer == "fight":
    answer = input ("you have no weapons and have to flight anyway")
    
elif answer == "flight":
    answer = input ("You escaped the zombie")
    
answer = input ("Do you want to go find ???? please choose (food/weapons)")

if answer == "food":
    answer = input ("you go to local chinese restraunt but there is no weapons so you continue to hardware store ")
    
elif answer == "weapons":
    answer = input ("You go to the local hardware store to find a weapon !")
    
answer = input ("Do you choose broom or crowbar ???? please choose (broom/crowbar)")
    
if answer == "broom":
    answer = input ("you have your weapon go outside and eaten alive instantly by zombies if it makes you feel better they used the broom to mop up your remains and magically you respawn outside")
    
elif answer == "crowbar":
    answer = input ("you take your crowbar and head towards the town")
    
answer = input ("you find a bugatti veyron outside with the keys in it Do you take or leave it ? please choose (take/leave)")
    
if answer == "take":
    answer = input ("you take the car it starts phew you drive away but a minuite later stalls and runs out of fuel you are now bk on foot")
    
elif answer == "leave":
    answer = input ("you leave the car and continue on")

answer = input ("where are you going next......local shopping center or winchester please choose one (shop/pub)")

if answer == "shop":
    answer = input ("you spend your time in the shopping center killing zombies while music plays call of duty zombie tune")
endgame:("shop") 

if answer == "pub":
    answer = input ("you go to the winchester and have a nice cold pint till this all blows over well done you choose the correct path music plays rockstar by post malone GAME OVER")

else:
    print ("please choose correct answers hope you enjoyed this game")

endgame:("pub") 
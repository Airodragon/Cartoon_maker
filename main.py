from ironman import ironman
from shinchan import shinchan
import shinchan
import doraemon
import pikachu
import ironman
print("<------------------WELCOME TO CARTOON MAKER--------------------->")
print("<----------------------------A turtle based cartoon maker:----------------------------------> ")
while 1:
    print("Choose:\n1: SHINCHAN\n2: Doraemon\n3:Pikachu\n4:Ironman\nany other key to exit")
    try:
        a = int(input("Enter Input: "))
        if(a==1):
            shinchan.shinchan()
        elif(a==2):
            doraemon.Doraemon()
        elif(a==3):
            pikachu.pikachu()
        elif(a==4):
            ironman.ironman()
    except Exception as q:
        break
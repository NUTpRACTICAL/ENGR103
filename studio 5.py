import math
#PART1
############################################################
lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
cntr=0

while True:
    if lst[cntr]==100:
        print("There is a ",lst[cntr], "at index no. ", cntr)
        break
    else:
        cntr+=1

while True:
    knowledge=input("how much do you know about NBA? 1=a lot, 2= a bit, 3=idk: ")
    if knowledge=="1":
        print("visit NBA offical website for recent games: https://www.nba.com/games")
        break
    elif knowledge=="2":
        print("vist the NBA official website for more info about different teams: https://www.nba.com/teams")
        break
    elif knowledge=="3":
        print("learn more on following link: https://www.lineups.com/articles/nba-101-beginners-guide-to-how-the-nba-works/")
        break
    else:
        print("please enter valid number, thx")
        continue

####################################################
#PART 2
###################################################

volumeOfPond= 2*200*200 #meter
q_in=3
d=0.5#guess
c=0.98
g=9.81
h=2
while True:
    a = (math.pi*(d**2))/4
    q_out=a*c*(math.sqrt(2*g*h))
    if q_out>=q_in:
        print (d)
        break
    d=d+0.05


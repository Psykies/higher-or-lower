from art import logo, vs
from follower_data import data
import random
import os

def select_data(x):
    pick = random.choice(x)
    x.remove(pick)
    return (pick, x)

def print_info(dict):
    name = dict.get("name")
    description = dict.get("description")

    country = dict.get("country")
    print (f"{name} {description} from {country}")




#frist create a space hwere two information of different object is shown to be compared for the user

total = len(data)
total_list = list(range(total))
on_list = total_list

a_set, on_list = select_data(on_list)
b_set, on_list = select_data(on_list)








total_point = 0
#winner goes to next round while loser is replaced with another object
game = "on"
while game == "on":
    # Clearing the Screen
    os.system('cls')
    print (logo)
    if len(on_list)== 0:
        print ("you have got the higghest score; you win")
    print()
    print_info(data[a_set])
    print (vs)
    print_info(data[b_set])
    print ()
    print (f"Your total score is {total_point}")
    print ()
    print ("try to guess whihc of the set A or B has the higher follower")
    ans = input("guess a or b")
    print ()
    if ans == "a":
        if (data[a_set].get("follower_count")) > (data[b_set].get("follower_count")):
            print ("you are correct")
            total_point +=1
            print (f"Your total score is {total_point}")
            a_set = a_set
            b_set, on_list = select_data(on_list)
        else:
            print ("you are wrong.Game over")
            print (f"Your total score is {total_point}")
            game = "off"


    if ans == "b":
        if (data[a_set].get("follower_count")) < (data[b_set].get("follower_count")):
            a_set = b_set 
            b_set, on_list = select_data(on_list)
            print ("you are correct")
            total_point += 1
            print (f"Your total score is {total_point}")
        else:
            print ("you are wrong.Game over")
            print (f"Your total score is {total_point}")
            game = "off"

#continue until the answer is wrong print the score



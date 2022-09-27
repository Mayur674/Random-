#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


you=input("Let's play the game of luck with computer\nrock/paper/scissor\nyou choose:----")
hand=("rock","paper","scissor")
computer=random.choice(hand)
print("computer choose:----",computer)
if you==computer:
    print("Match is tied\nbecause both choose same")
else:
    if you=='rock':
        if computer=='paper':
            print("Computer won the match\nbecause paper cover the rock")
        else:
            print("Congratulation!!!\nyou won the match\nbecause rock smash the scissor")
    elif you=='paper':
        if computer=='rock':
            print("Congratulation!!!\nyou won the match\nbecause paper cover the rock ")
        else:
            print("computer won the match\nbecause scissor cut the paper")
    elif you=='scissor':
        if computer=='rock':
            print("computer won the match\nbecause rock smash the scissor")
        else:
            print("Congrulation!!!\nyou won the match\nbecause scissor cut the paper")


# In[7]:


print("Let's play cricket\nIt's toss time\nUmpire swing the coin in the air")
a=("HEAD","TAILS")
b=random.choice(a)
you=input("you called:---").upper()
umpire=print("umpire says it's",b)
if you==b:
    print("you won the toss")
else:    
    print("opponent won the toss")


# In[ ]:





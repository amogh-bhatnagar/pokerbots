''' 
This is to test if your idea is good.
So it will run the engine many times and tell you how many you won and how many you lost
'''
###Lines below taken from engine.py idk i feel like they're needed
from collections import namedtuple
from threading import Thread
from queue import Queue
import time
import json
import subprocess
import socket
import eval7
import sys
import os
import copy

sys.path.append(os.getcwd())
from config import *
##############

import engine as engine
from engine import Game

idea_tester = Game()
h_wins = 0
v_wins = 0
ties = 0

num_runs = 20

for _ in range(num_runs):
    idea_tester.run() #runs the engine (we should see if we can take out the part where it prints in terminal)
    f = open('gamelog.txt', 'r') #these lines read the file but idk if they work
    last_line = f.readlines()[-1] #grabs the last line of the gamelog.txt
    print("###################################################################################")
    print(last_line)
    print("###################################################################################")
    pre_score = ""
    for char in last_line: #extracts the scores
        if char in "0123456789-V":
            pre_score += char
    score_list_str = pre_score.split("V")
    h_score = float(score_list_str[0]) #next two lines get the scores into floats 
    v_score = float(score_list_str[1])
    if h_score > v_score:
        h_wins += 1
    elif h_score < v_score:
        v_wins += 1
    else:
        ties += 1

prob = float(h_wins/num_runs)

print("###################################################################################")
print("###################################################################################")
print("###################################################################################")
print("Number of games:", num_runs)
print("Hero wins:", h_wins)
print("Villian wins:", v_wins)
print("Ties:", ties)
print("Probability of winning with idea:", prob)







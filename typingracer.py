import time
import threading
import os
import math
from webscraper.textscraper import call_available_text

cmd = ""
time_limit = 60
user_input = " "
true_list = []
wordcount_list = []
#============================================================================================================================================#


def accuracy():
    accuracy = len(true_list) / len(phrase)
    print(f"Your accuracy: {round(accuracy*100, 2)}%")


def wpm():
    wordcount = phrase.split(" ")
    minutefulltime =  60/time_taken
    wpm = len(wordcount) * minutefulltime
    print(f"Your words per minute is: {math.floor(wpm)}")

    
def typing():
    global start_time, phrase, trueorfalse, true_list, user_input
    start_time = time.time()
    phrase = call_available_text()
    print()
    print(phrase)
    user_input = input("")
    time.sleep(0.001)
    try:
        for i in range(len(phrase)):
            trueorfalse = phrase[i] == user_input[i]
            if trueorfalse == True:
                true_list.append(trueorfalse)
    except IndexError:
        pass


def timer():
    global time_taken
    while True:
        time_taken = time.time() - start_time
        if user_input != "" and user_input != " ":
            print()
            print(f"Wow! You took {round(time_taken, 2)} seconds")
            break
        elif user_input == "":
            print("Nice one! You failed :D")
            os._exit(1)
        if time_taken > time_limit:
            print()
            print(f"Time's up! {time_limit} seconds time limit finished. Race ended!")
            print("Your accuracy and wpm: 0.0%")
            os._exit(1)
        time.sleep(0.001)


#============================================================================================================================================#

typingthread = threading.Thread(target=typing)
timerthread = threading.Thread(target=timer)
while cmd != "START".lower():
    cmd = input(f"Copy the phrase as fast as possible. You have {time_limit} seconds.\nType 'start' to start. \n")

typingthread.start()
timerthread.start()

typingthread.join()
timerthread.join()

accuracy()
wpm()
import time
import threading
import os

cmd = ""
time_limit = 5
user_input = ""
true_list = []

#============================================================================================================================================#


def accuracy():
    accuracy = len(true_list) / len(phrase)
    print(f"Your accuracy: {round(accuracy, 2)}%")

    
def typing():
    global start_time, phrase, trueorfalse, true_list, user_input
    start_time = time.time()
    phrase = "Hello, there! How are you?"
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
    while True:
        time_taken = time.time() - start_time
        if user_input != "":
            print()
            print(f"Wow! You took {round(time_taken, 2)} seconds")
            break
        if time_taken > time_limit:
            print()
            print(f"Time's up! {time_limit} seconds time limit finished. Race ended!")
            print("Your accuracy: 0.0%")
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
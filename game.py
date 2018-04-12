# ============Mental operations game===============
# Import the libraries
import time, signal, sys, select, pygame, os, threading, time
from timeit import default_timer
from random import randint

# ============Global variables=====================
continuePlaying = True
timeout = 7
bonus = 3
lessThanRounds = 0

# ============Define functions for the game========

class AlarmException(Exception):
    pass

class Alarm (threading.Thread):
    def __init__ (self, timeout):
        threading.Thread.__init__ (self)
        self.timeout = timeout
        self.setDaemon (True)
    def run (self):
        time.sleep (self.timeout)
        os._exit (1)

def alarmHandler(signum, frame):
    raise AlarmException

#fix this part
def my_raw_input(prompt, timeout):
    signal.signal(signal.SIGABRT, alarmHandler)
    #signal.alarm(timeout)
    alarm = Alarm(timeout)
    alarm.start()
    try:
        userGuess = int(input(prompt))
        # The line below deactivates the alarm once the time's over.
        signal.alarm(0)
        return userGuess
    except AlarmException:
        print("Uh-oh! Time's up for that one!")
        userGuess = ""
        return userGuess
    signal.signal(signal.SIGABRT, signal.SIG_IGN)
    return ''


def compute_list(list_with_values):
    x = 0
    final_result = list_with_values[x]
    list_with_values.pop(0)
    while len(list_with_values) != 0:
        operator = list_with_values[x]
        if operator == "+":
            final_result += list_with_values[x + 1]
            list_with_values.pop(0)
            list_with_values.pop(0)
        elif operator == "-":
            final_result -= list_with_values[x + 1]
            list_with_values.pop(0)
            list_with_values.pop(0)
        elif operator == "*":
            final_result *= list_with_values[x + 1]
            list_with_values.pop(0)
            list_with_values.pop(0)
        elif operator == "/":
            final_result /= list_with_values[x + 1]
            list_with_values.pop(0)
            list_with_values.pop(0)
    return final_result


'''def load_music():
    pygame.init()
    pygame.mixer.init()
    soundObj = pygame.mixer.Sound('/Users/alexbr/Documents/Python/Personal Projects/Ready/CTBL_2.wav')
    soundObj.play(-1)'''


def initiate_game(level, option, bonus, lessThanRounds):
    #load_music()
    goodGuess = 0
    badGuess = 0
    zeroGuess = 0
    time_easy_level = default_timer()
    numbers_with_operators = []
    local_operators = ["+", "-", "*"]
    rounds = 4
    timing_option = 1.2
    global continuePlaying
    global timeout

    if option == 1:
        bound_operation = 1
    elif option == 2:
        bound_operation = 2
    if level == 1:
        upper_bound = 10
    elif level == 2:
        upper_bound = 100
    elif level == 3:
        upper_bound = 500
        # ====Repeat operations according to the user's rounds===========
    while lessThanRounds != rounds:
        # ===10 Random numbers between 1 and upper_bound (randint()) are generated =========
        easy_level = [randint(1, upper_bound) for i in range(1, 10)]
        # ===Each list of random numbers is appended with a random operator===
        for item in easy_level:
            numbers_with_operators.append(item)
            time.sleep(timing_option)
            print(numbers_with_operators)
            # print numbers_with_operators[counter_of_numbers]
            numbers_with_operators.append(local_operators[randint(0, bound_operation)])
            # print numbers_with_operators[counter_of_numbers]
            # print numbers_with_operators
            if len(numbers_with_operators) == 18:
                print(numbers_with_operators)
                numbers_with_operators.append(randint(1, upper_bound))
                time.sleep(timing_option)
                print(numbers_with_operators)
            else:
                time.sleep(timing_option)
                print(numbers_with_operators)
        print("This is operation number: ")
        print(lessThanRounds + 1)
        print("\n")
        user_guess = my_raw_input("What's the result? ", timeout)
        computer_result = compute_list(numbers_with_operators)
        if user_guess == computer_result:
            goodGuess += 1
            timeout = 7
            counter_of_numbers = 0
            print("Good guess!")
            if goodGuess == bonus:
                rounds += 3
                print("Bonus activated!!!")
                timing_option -= 0.2
                bonus += 3
        elif user_guess == "":
            print("Sorry, you didn't answer.")
            zeroGuess += 1
            timeout = 7
            counter_of_numbers = 0
            bonus -= 1
            print("The result was: " + str(computer_result))
        elif user_guess != computer_result:
            print("Sorry, that is not the result.")
            badGuess += 1
            timeout = 7
            counter_of_numbers = 0
            print("The result was: " + str(computer_result))
        del numbers_with_operators[:]
        lessThanRounds += 1
    duration = default_timer() - time_easy_level
    continuePlaying = False
    print("Your results are: \n")
    print("Good guesses: " + str(goodGuess) + "\nBad guesses: " + str(badGuess) + "\nZero guesses: " + str(zeroGuess))
    print("Total seconds playing: " + str(duration) + " seconds")
    return continuePlaying


def difficulty_level(continuePlaying, option_for_operation):
    global bonus
    print("1.Easy\n")
    print("2.Medium\n")
    print("3.Hard\n")
    print("4.Quit\n")
    difficulty_level = input("Please, select the number of the difficulty level: 	\n")
    # rounds=int(raw_input("How many round can you calculate: \n"))
    print("Remember, you have 3 rounds but they can increase.")
    if difficulty_level == "4":
        print("End of the game.\n")
        continuePlaying = False
    elif difficulty_level == "1":
        level = 1
        initiate_game(level, option_for_operation, bonus, lessThanRounds)
    elif difficulty_level == "2":
        level = 2
        initiate_game(level, option_for_operation, bonus, lessThanRounds)
    elif difficulty_level == "3":
        level = 3
        initiate_game(level, option_for_operation, bonus, lessThanRounds)
    else:
        print("Please, enter a number")


def main():
    global continuePlaying
    while (continuePlaying):
        print("Welcome to the mental operations game.\n")
        print("1.Addition and Subtraction\n")
        print("2.Addition, Subtraction and Product\n")
        print("3.Quit\n")
        option_for_operation = int(input("Please, choose and option: \n"))
        if option_for_operation == 1:
            difficulty_level(continuePlaying, option_for_operation)
        elif option_for_operation == 2:
            difficulty_level(continuePlaying, option_for_operation)
        elif option_for_operation == 3:
            print("End of the game.\n")
            continuePlaying = False
        else:
            print("Not a valid option, please select a number from the displayed options.")


if __name__ == '__main__':
    main()

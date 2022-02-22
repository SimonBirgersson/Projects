# script with functions for generating a simple math quiz of varying length
import operator
import random


def randomcalc():
    """generates random math problem on the form a +-/* b = ?"""
    # dict of possible math operators
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    # randomize two numbers
    num1 = random.randint(0, 12)
    num2 = random.randint(1, 10)  # I don't sample 0's to protect against divide-by-zero

    # picks one random operator
    op = random.choice(list(ops.keys()))

    # does the calculation for the correct answer
    answer = ops.get(op)(num1, num2)

    # prints question
    print(f"What is {num1} {op} {num2}?\n"
    return answer


def askquestion():
    """Asks user math question in randomcalc, returns True if the entering value is correct"""

    # get one random question
    answer = randomcalc()

    # user input
    guess = float(input())

    # compare answer and guess, returns True if correct
    return guess == answer


def quiz(num):
    """ "Generates a math quiz with "num" questions."""

    # intro prompt
    print("Welcome. This is a %i question math quiz\n", num)

    # initialize score tracker
    score = 0

    # loop of questions
    for i in range(num):

        # asks one question
        correct = askquestion()

        # if correct, increase score, don't if incorrect.
        if correct:
            score += 1
            print("Correct!\n")
        else:
            print("Incorrect!\n")

    # summarize results
    return f"Your score was {score}/{num}"

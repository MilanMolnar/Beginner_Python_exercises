from question import Question
import time
import sys


def sprint(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2 / 2)


question_prompts = [
    "what color are apples?\n(A) Green/red          (B) Purple\n(C) Orange          (D) Blue\n\n",              #1
    "what color are bananas?\n(A) Red           (B) Purple\n(C) Yellow          (D) Teal\n\n",                  #21
    "what color are stawberries?\n(A) Blue          (B) Red\n(C) Orange         (D) Black\n\n",                 #32
    "why did the chicken cross the road?\n(A) I dont know          (B)yes Red\n(C) Correct answer         (D) whynotlul?\n\n", #43
    "what does all the work?\n(A) chicken          (B) i love salmon\n(C) knife         (D) Its raaaaaw\n\n",   #54
    "are you gay?\n(A) I am          (B) I am\n(C) I am         (D) I am\n\n",                                  #65
    "what color is the best?\n(A) Blue          (B) Red\n(C) Orange         (D) Black\n\n",                     #76
    "you cant answer this!\n\n",                                                                                #87
    "Hablaelaleloa\n(A) Marka cola          (B) Pepsi cola\n(C) Coca cola         (D) Sparos cola\n\n",         #98
    "why are you running?\n(A) lol          (B) aAAaaAaaaaa\n(C) ...         (D) engriboj\n\n",                 #109
    "who invented the theory of relativity\n(A) Newton          (B) Newton\n(C) Newton         (D) Einstein\n\n", #1110
]

questions = [
    Question(question_prompts[0], "Aa"),
    Question(question_prompts[1], "Cc"),
    Question(question_prompts[2], "Bb"),
    Question(question_prompts[3], "Cc"),
    Question(question_prompts[4], "Cc"),
    Question(question_prompts[5], "Ee"),
    Question(question_prompts[6], "Aa"),
    Question(question_prompts[7], "$"),
    Question(question_prompts[8], "Cc"),
    Question(question_prompts[9], "Bb"),
    Question(question_prompts[10], "Dd"),
]

possible_options = ["a", "A", "B", "b", "c", "C", "D" ,"d", "E", "$"]
def run_test(questions):
    score = 0
    for question in questions:
        while True:
            answer = input(question.prompts)
            if answer in possible_options:
                break
            else:
                sprint("Not a valid option!")
        if answer in question.answer:
            score += 1
            sprint("Correct!")
        else:
            sprint("Incorrect!")
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")
    if score == 11:
        sprint("Megmondtam a valaszokat mi?")
    elif score > 7:
        sprint("Nice F-in job dude")
    elif 3 > score:
        sprint("Fucking disgrace!")
    elif score >= 4:
        sprint("you are not as dumb as you look")
    elif score == 0:
        sprint("Waste of human matter")


run_test(questions)
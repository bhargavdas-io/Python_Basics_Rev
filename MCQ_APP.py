from Questions import Questions

question_array  = ["What is the colour of an Apple?\n(a) Orange\n(b) Teal\n(c) Red\n\n",
                    "What is the day before Sunday?\n(a) Saturday\n(b) Monday\n(c) Wednesday\n\n",
                    "Who is a member of Linkin park?\n(a) Mike Shinoda\n(b) Chester Bennington\n(c) Both of the above\n\n"
                   ]

questions = [
    Questions(question_array[0], "c"),
    Questions(question_array[1], "a"),
    Questions(question_array[2],"c")

]

def run_test(questions):

    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You scored " + str(score) + "/" +str(len(questions)) + "correct")

run_test(questions)


print("welcome to owens triva adventure")
type("type go to start")
score = 0
knowledge = 0
q2 = 0
while score == 0:
    answer = input("")
    if answer == ("go"):
        print("(x - 7) / 4 = 4")
        print("solve for x")
        answer1 = input('')
        answer1 = int(answer1)
        if answer1 == (19):
            score = score+1
            print("correct your score is now "+str(score))
        else:
            score = score-1
            print("inncorect 1 point has been deducted from your score. it is now"+str(score))
    else:
        print("type go to start")

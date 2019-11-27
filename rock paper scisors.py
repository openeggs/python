raw_data = [
50.0,
]
#ai data is percent of times ai loses
rock = 1
paper = 0
scisors = 0
running = 0
best_odds = 0
ai_wins = 0
ai_fails = 0
ties = 0
data_points = 0
rock_row = 0
paper_row = 0
scisors_row = 0
score_toggle = 0
#-------------make the toggle----------------
score_toggle = input('''
type score for the score
type quit to quit
type info to learn more about this program

type yes to display score after each round
type no if you dont want the score displayed after each round
''')
if score_toggle == 'yes' or 'no':
    pass
else:
    score_toggle = input('''
type yes to toggle on score
type no to toggle of score
''')
if (rock>paper) and (rock>scisors):
    best_odds = 'paper'
elif (paper>rock) and (paper>scisors):
    best_odds = 'scisors'
elif (scisors>rock) and (scisors>paper):
    best_odds = 'rock'

while running == 0:
    data = input('rock paper scisors: ')
    if data == 'rock':
        paper_row = 0
        scisors_row = 0
        rock_row = rock_row + 1
        if rock_row >= 2:
            if (rock>paper) and (rock>scisors):
                best_odds = 'paper'
            elif (paper>rock) and (paper>scisors):
                best_odds = 'scisors'
            elif (scisors>rock) and (scisors>paper):
                best_odds = 'rock'
            print('paper')
            if data == 'scisors':
                ai_fails = ai_fails + 1
                if score_toggle == 'yes':
                    print('you win')
                else:
                    running = 0
            if data == 'rock':
                ai_wins = ai_wins + 1
                if score_toggle == 'yes':
                    print('you lose')
                else:
                    running = 0
            else:
                ties = ties + 1
                print('tie')
        else:
            if ai_wins == 0:
                pass
            else:
                data_points = int(ai_fails / (ai_wins + ai_fails) * 100)
            rock = rock + 1
            print(best_odds)
            if (rock>paper) and (rock>scisors):
                best_odds = 'paper'
            elif (paper>rock) and (paper>scisors):
                best_odds = 'scisors'
            elif (scisors>rock) and (scisors>paper):
                best_odds = 'rock'
            if best_odds == 'paper':
                ai_wins = ai_wins + 1
                if score_toggle == 'yes':
                    print('you lose')
                else:
                    running = 0
            elif best_odds == 'scisors':
                ai_fails = ai_fails + 1
                if score_toggle == 'yes':
                    print('you win')
                else:
                    running = 0
            else:
                ties = ties + 1
                if score_toggle == 'yes':
                    print('tie')
                else:
                    running = 0
    elif data == 'paper':
        paper_row = paper_row + 1
        rock_row = 0
        scisors_row = 0
        if paper_row >= 2:
            if (rock>paper) and (rock>scisors):
                best_odds = 'paper'
            elif (paper>rock) and (paper>scisors):
                best_odds = 'scisors'
            elif (scisors>rock) and (scisors>paper):
                best_odds = 'rock'
            print('scisors')
            if data == 'paper':
                if score_toggle == 'yes':
                    print('you lose')
                else:
                    running = 0
                ai_wins = ai_wins + 1
            elif data == 'rock':
                if score_toggle == 'yes':
                    print('you win')
                else:
                    running = 0
                ai_fails = ai_fails + 1
            else:
                ties = ties + 1
                if score_toggle == 'yes':
                    print('tie')
                else:
                    running = 0
        else:
            if ai_wins == 0:
                pass
            else:
                data_points = int(ai_fails / (ai_wins + ai_fails) * 100)
            paper = paper + 1
            print(best_odds)
            if best_odds == 'scisors':
                ai_fails = ai_fails + 1
                if score_toggle == 'yes':
                    print('you lose')
                else:
                    running = 0
            elif best_odds == 'rock':
                ai_wins = ai_wins + 1
                if score_toggle == 'yes':
                    print('you win')
                else:
                    running = 0
            else:
                ties = ties + 1
                if score_toggle == 'yes':
                    print('tie')
                else:
                    running = 0
            if (rock>paper) and (rock>scisors):
                best_odds = 'paper'
            elif (paper>rock) and (paper>scisors):
                best_odds = 'scisors'
            elif (scisors>rock) and (scisors>paper):
                best_odds = 'rock'
    elif data == 'scisors':
        paper_row = 0
        rock_row = 0
        scisors_row = scisors_row + 1
        if scisors_row >= 2:
            if (rock>paper) and (rock>scisors):
                best_odds = 'paper'
            elif (paper>rock) and (paper>scisors):
                best_odds = 'scisors'
            elif (scisors>rock) and (scisors>paper):
                best_odds = 'rock'
            print('rock')
            if data == 'paper':
                if score_toggle == 'yes':
                    print('you win')
                else:
                    running = 0
                ai_fails = ai_fails + 1
            elif data =='scisors':
                if score_toggle == 'yes':
                    print('you lose')
                else:
                    running = 0
                ai_fails = ai_fails + 1
            else:
                if score_toggle == 'yes':
                    print('tie')
                else:
                    running = 0
                ties = ties + 1
        else:
            if ai_wins == 0:
                pass
            else:
                data_points = int(ai_fails / (ai_wins + ai_fails) * 100)
            scisors = scisors + 1
            print(best_odds)
            if best_odds == 'rock':
                ai_fails = ai_fails + 1
                if score_toggle == 'yes':
                    print('you lose')
                else:
                    running = 0
            elif best_odds == 'paper':
                ai_wins = ai_wins + 1
                if score_toggle == 'yes':
                    print('you win')
                else:
                    running = 0
            else:
                ties = ties + 1
                if score_toggle == 'yes':
                    print('tie')
                else:
                    running = 0
    elif data == 'info':
        print('''
rock paper scisors AI
language: python3
scripted by: Owen Basore
V 1.0 nov 2019 Owen Inc
the ai has wins ''',int(sum(raw_data)),'''% of matches''')
    elif data == 'score':
        print('you scored ',ai_fails,' points')
        print('the computer scored ',ai_wins,' points')
        print('you tied ',ties,' times')
    elif data == 'quit':
        data_points = int(ai_wins / (ai_wins + ai_fails) * 100)
        print('the ai wins ',int(sum(raw_data)),'% of time')
        if ai_wins > ai_fails:
            print('you lost')
            print('you score',ai_fails)
            print('ai scored ',ai_wins)
        elif ai_fails > ai_wins:
            print('you won')
            print('you score',ai_fails)
            print('ai scored ',ai_wins)
        else:
            print('tie')
            print('you score',ai_fails)
            print('ai scored ',ai_wins)
        with open('rock_paper_scisors.py', 'r+') as foo:
            data = foo.readlines()
            pos = 2 - 1  # list position to edit
            if ai_wins + ai_fails == 0:
                running = 1
            else:
                raw_data.append(data_points)
                data.insert(pos, str(sum(raw_data)/len(raw_data)) + ", \n")
                x = data[pos + 1]
                data.remove(x)
                foo.seek(0)
                for i in data:
                    i.strip()
                    foo.write(str(i))
                    running = 1
    else:
        print('error')

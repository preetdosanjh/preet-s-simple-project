print('Hello! Welcome to the trivia game!')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1: In a website browser address bar, what does "www" stand for?')
    if ans.lower().strip() == 'world wide web' :
        score += 1
        print("Correct!")
    else:
        print('Incorrect')

        
    ans = input('2: What is the tiny piece at the end of a shoelace called?')
    if ans.lower().strip() == 'aglet' :
        score += 1
        print('Correct!')
    else:
        print('Incorrect')


    ans = input('3: What does BMW stand for in English?')
    if ans.lower().strip() == 'Bavarian Motor Works' :
        score += 1
        print('Correct!')
    else:
        print('Incorrect')


    ans = input('4: Which two countries share the largest border?')
    if ans.lower().strip() == 'USA and Canada' or 'Canada and USA' :
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

print('Thank you for playing, you got ', score, " questions correct. ")
mark = (score/total_q) * 100

print('Mark: ', mark)

# Python Quiz Game
print("Welcome to the Math Quiz!\n")

questions = ("What is 2 + 2?: ", "What is 4 + 4?: ")
options = (("A 4", "B 2", "C 1"), ("A 3", "B 8", "C 0"))
answers = ("A", "B")
guesses = []
score = 0

for question_num in range(len(questions)):
    print("--------")
    print(questions[question_num])

    
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT! Next Question:")
    else:
        print("INCORRECT! Next Question:")
        print(f"The correct answer is {answers[question_num]}")

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

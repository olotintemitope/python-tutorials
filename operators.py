isBayoHome = bool(0)

if isBayoHome:
    print("Hello Friend")
else:
    print("I will come back later")


def calculateScore(score: int):
    if score >= 80:
        print("You're a brilliant guy")
    elif 75 <= score <= 79:
        print("You're somewhat a brilliant guy")
    elif 70 <= score <= 74:
        print("You're a good guy")
    elif 65 <= score <= 69:
        print("You're just there!")
    else:
        print("Your parent needs a refund")


try:
    score = int(input("Enter your score : "))
    calculateScore(score)
except ValueError:
    print("Pls re-enter score enter as an integer")

import random

def showGuess(guess,answer):
    correctNums = {
        number for number, correct in zip(guess, answer) if number == correct
    }
    misplacedNums = set(guess) & set(answer) - correctNums
    wrongNums = set(guess) - set(answer)

    print("Correct Numbers:", ", ".join(sorted(correctNums)))
    print("Misplaced Numbers:", ", ".join(sorted(misplacedNums)))
    print("Wrong Numbers:", ", ".join(sorted(wrongNums)))
    
def gameOver(answer):
    print(f"The answer was {answer}\n")
    
def main():
    answer = "%05d" % random.randint(0,99999)
    for guessNum in range(0,6):
        guess = input(f"\nGuess number {guessNum}: ")
        guess = guess.zfill(5)
        showGuess(guess,answer)
        if guess == answer:
            print("Correct")
            break;
    else:
        gameOver(answer)
if __name__ == "__main__":
    main()
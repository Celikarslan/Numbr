import pathlib
import random
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme

console = Console(width=50)

def showGuess(guesses,answer):
    for guess in guesses:
        styled_guess = []
        for x,y in zip(guess,answer):
            if x == y:
                style = "bold white on dark_green"
            elif x > y and x is not '_':
                style = "bold white on red"
            elif x < y:
                style = "bold white on bright_cyan"
            elif x in ascii_letters:
                style = "white on black"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{x}[/]")

        console.print("".join(styled_guess), justify="center")
    
def gameOver(guesses,answer,guessCorrect):
    refresh(headline="Game Over")
    showGuess(guesses, answer)
    if guessCorrect:
        console.print(f"\n[bold white on green]Correct, the number is {answer}[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the number was {answer}[/]")
    
def refresh(headline):
    console.clear()
    console.rule(f"[bold white]:ice: {headline} :fire:[/]\n",style="magenta")
    
    
def main():
    answer = "%5d" % random.randint(10000,99999)
    guesses = ["_"*5] * 6
    for guessNum in range(6):
        refresh(headline=f"Guess {guessNum + 1}")
        showGuess(guesses, answer)

        guesses[guessNum] = input("\nGuess Number: ")
        while not guesses[guessNum].isdigit() or len(guesses[guessNum]) > 5:
            guesses[guessNum] = input("\nPlease Guess a Number between 0-99999: ")
        guesses[guessNum] = guesses[guessNum].zfill(5)
        if guesses[guessNum] == answer:
            break
    gameOver(guesses,answer,guessCorrect=guesses[guessNum] == answer)
if __name__ == "__main__":
    main()
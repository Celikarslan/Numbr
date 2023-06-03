import pathlib
import random
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme

console = Console(width=50, theme=Theme({"warning": "red on yellow"}))

def showGuess(guesses,answer):
    for guess in guesses:
        styled_guess = []
        for number, correct in zip(guess, answer):
            if number == correct:
                style = "bold white on green"
            elif number in answer:
                style = "bold white on yellow"
            elif number in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{number}[/]")

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
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")
    
    
def main():
    answer = "%05d" % random.randint(0,99999)
    guesses = ["_"*5] * 6
    for guessNum in range(6):
        refresh(headline=f"Guess {guessNum + 1}")
        showGuess(guesses, answer)

        guesses[guessNum] = input("\nGuess Number: ").upper()
        if guesses[guessNum] == answer:
            break
    gameOver(guesses,answer,guessCorrect=guesses[guessNum] == answer)
if __name__ == "__main__":
    main()
import random
import hangman_words
from hangman_art import logo, stages
print(logo)


chosen_word = random.choice(hangman_words.word_list)


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lives = 7
end_game = False
guessed_letter = []


display = []
for letter in chosen_word:
    display += "_"

while lives > 0 and not end_game:
  guess = input("Guess a letter: ").lower()
  if guess in chosen_word:
    print("Your guess is correct!")
  elif guess not in alphabet:
    print("Please enter only letters.")
  elif guess not in chosen_word:
    lives -= 1
    print(stages[lives])
    print(f"Sorry, that guess is not correct. You have {lives} lives remaning")
    guessed_letter += guess
    if lives == 0:
     print("Game Over")
     print(f"The correct word was {chosen_word}")
    elif guessed_letter.count(guess) > 1:
      print(f"You have already guessed this letter: {guess}")
  elif "_" not in display:
     print("Congrats you have won the game!")
     end_game = True

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  print(f"{' '.join(display)}")

  if "_" not in display:
    print("Congrats you have won the game!")
    end_game = True

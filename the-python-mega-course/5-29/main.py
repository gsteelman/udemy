hiddenWord = "python"
userWord = ""

while userWord != hiddenWord:
  userWord = raw_input("Enter the hidden word: ")

  if userWord == hiddenWord:
    print("You guessed it!")
  else:
    print("Guess again!")

print("Thanks for playing!")
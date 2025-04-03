import random
num = random.randint(1, 10)
while True:
    guess = int(input("Guess a number (1-10): "))
    if guess == num:
        print("🎉 Correct! You guessed it.")
        break
    elif guess < num:
        print("Try higher!")
    else:
        print("Try lower!")

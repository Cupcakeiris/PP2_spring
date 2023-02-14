import random
g = random.randint(1, 20)

print("Hello! What is your name?")
name = input()
print(f"Well, {name},I am thinking of a number between 1 and 20.\nTake a guess.")

x = int(input())
count = 0
while x != g:
    if x > g:
        print("Your guess is too high.\nTake a guess")
        x = int(input())
    elif x < g:
        print("Your guess is too low.\nTake a guess")
        x = int(input())
    count += 1
print(f"Good job, {name}! You guessed my number in {count} guesses!")

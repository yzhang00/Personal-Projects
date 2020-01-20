import random

# array storing words
word_bank = []
# opening file from relative location
with open('ngrams/sowpods.txt', 'r') as f:
    line = f.readline().strip()
    while line:
        word_bank.append(line)
        line = f.readline().strip()
# randomly selecting word and creating background structures
word = random.choice(word_bank)
word_split = list(word)
word_fin = []
guessed = []
for i in range(0, len(word_split)):
    word_fin.append(word_split[i])
    word_fin.append(" ")
    guessed.append("_")
    guessed.append(" ")

print("Welcome to: H A N G M A N")
print("You have 6 lives.")

# continues guessing until word has been guessed
lives = 6
while "_" in guessed and lives > 0:
    correctly = False
    user = input("Please guess a letter: ")
    user = user.capitalize()
    for x in range(0, len(guessed)):
        if word_fin[x] == user:
            guessed[x] = user
            correctly = True
    if not correctly:
        lives = lives - 1
    print("".join(guessed))
    print("Lives remaining:", lives)
if lives == 0:
    print("You lose. The word was:", word)
else:
    print("You win!")



realWord = ["m","e","t","a","l","l","i","c","a"]
guessList = ["-","-","-","-","-","-","-","-","-"]

playerName = input("Name:")

print(f"Hello {playerName} lets play hangman")

lifecounter = 10

while(lifecounter > 0):
    flag = 0

    for i in guessList:
        print(i)
    guess = input("Guess a word:")

    for i in range(9):
        if(realWord[i] == guess):
            guessList[i] = guess
            flag = 1

    if(flag == 0):
        lifecounter -= 1
        print(f"Wrong!\nYou have {lifecounter} left")

    if(realWord == guessList):
        break

if(lifecounter > 0):
    print(str(guessList))
    print("You win")
else:
    print("You died")

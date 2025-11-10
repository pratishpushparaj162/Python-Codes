import random
from itertools import islice

def nth_index(iterable, value, n):
    matches = (idx for idx, val in enumerate(iterable) if val == value)
    return next(islice(matches, n-1, n), None)

def game():
    ascii="abcdefghijklmnopqrstuvwxyz"
    last=""
    hyphens_empty = ""
    word_list = ['python', 'java', 'kotlin', 'javascript']
    tries = 8
    random_word = random.choice(word_list)
    random_word_list = list(random_word)
    hyphens = list(len(random_word) * '-')
    while tries != 0:
        print("")
        print(hyphens_empty.join(hyphens))
        user_input = input("Input a letter: ")
        if user_input in random_word_list and user_input not in hyphens:
            ind = random_word_list.index(user_input)
            del hyphens[ind]
            hyphens.insert(ind, user_input)
            last=last+user_input
            count = random_word.count(user_input)
            if count > 1:
                ind2 = nth_index(random_word_list, user_input, 2)
                del hyphens[ind2]
                hyphens.insert(ind2, user_input)
        elif len(user_input)!=1:
            print("You should print a single letter")
        elif user_input not in ascii:
            print("It is not an ASCII lowercase letter")
        elif user_input in last:
            print("You already typed this letter")
        elif user_input not in random_word_list:
            print("No such letter in the word")
            last=last+user_input
            tries -= 1
    if hyphens==random_word_list:
        print("You guessed the word "+random_word+"!")
        print("You survived!")
    else:
        print("You are hanged!")

print("H A N G M A N")
s=input('Type "play" to play the game, "exit" to quit:')
if s=="play":
    game()
else:
    exit()

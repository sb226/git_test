import random
from word  import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letter in a word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    life = 6
    
    while len(word_letters) > 0 and life >0:
        #letter used
        # ' '.join([a, b, c]) --> 'a b c'
        print('You have used these letters: ', ' '.join(used_letters))

        #current word in - - - - and only appear letter when guessed right
        #Short version of doing this (this is good)
        #word_list = [letter if letter in used_letters else '_' for letter in word]

        #Long version of doing this (it's fucking shit)
        word_list = []
        for letter in word:
            if letter not in used_letters:
                letter = '_'
            else:
                letter = letter
            word_list.append(letter)
        print('Current word:', ' '.join(word_list))
        #print(word_letters)
        #getting user input
        user_letter = input('Guess a letter: ').upper()
        #if guess letter still available in the alphabet 
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            #If the letter guess right then remove from list of word 
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            #If letter guess wrong then minus 1 life
            else:
                life -= 1
                print('Letter is not in the word')
        #If guess letter already guessed 
        elif user_letter in used_letters:
            print('You guessed that already')
        else:
            print('invalid character')
        #print(used_letters)
        #print(word_letters)
        print(life)
    if life == 0:
        print('You ran out of life, now go get a life. The word was', word)
    else:
        print('Noice  suuuuu, the word is', word)
hangman()




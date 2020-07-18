# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 23:28:34 2018

@author: farhan
"""

import os, time, hangman1
path = os.getcwd()
os.chdir(path)
vowels = 'aeiouAEIOU'
vowels = list(vowels)


def words():
    word = input('What is the hangman word: ')
    definition = input('Write the description of the word: ')
    return word, definition

def PlayAgain():
    print('Do you want to play again? ')
    return input().lower().startswith('y')

def main():        
    word, definition = words()
    word = list(word.lower())
    Hangman = len(word)*'_'
    Hangman = list(Hangman)
    for i in Hangman:
        if i in vowels:
            Hangman[Hangman.index(i)] = 'X'
    os.system('CLS')
    count = 0
    while True:
        if count == 6:
            print('You lost :(')
            print('The word was ',end = '')
            for h in word:
                print(h, end = '')
            print('\n')
            break
        if Hangman == word:
            print('You won!')
            break
        n = []
        print('definition of the word: ',definition)
        for i in Hangman:
            print(i, end = '  ')
        hangman1.draw(count)
        letter = input('\n\nWrite a letter: ').lower()
        if letter == '':
            break
        if letter.lower() not in word:
            count += 1
        if letter.lower() in word:
            for i in enumerate(word):
                for j in i:
                    if j == letter.lower():
                        n.append(i[i.index(j)-1])
            for i in n:
                Hangman[i] = letter

        time.sleep(0.25)
        os.system('CLS')
                
while True:
    main()
    if PlayAgain() == False:
        break

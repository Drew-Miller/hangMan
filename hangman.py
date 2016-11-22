#!/usr/bin/env python3

import random


#API
#has guesses limit
#has a displayed and word list
#can tell you if won
class hangMan:
    def __init__(self, n=8, path="/usr/share/dict/words"):
        with open(path) as f:
            lines = f.readlines()

        lines = [line.rstrip('\n') for line in open(path)]

        index = random.randrange(0, len(lines))

        self.word = lines[index]

        self.displayed = []

        for letter in self.word:
            if not letter.isalpha():
                self.displayed.append(letter)
            else:
                self.displayed.append('~')

        self.guessed = []
        self.guesses = n

    #function for passing in a new letter that user has guessed
    def guessLetter(self, guess):
        #cannot guess same letter twice
        if self.ended() < 0:
            return False

        if guess in self.guessed:
            return False

        correct = False
        for i,l in enumerate(self.word):
            if l is guess:
                correct = True
                self.displayed[i] = guess

        if not correct:
            self.guesses -= 1

        self.guessed.append(guess)
        return True

    #-1 on lost, 0 on still playing, 1 on win
    def ended(self):
        #if we have guessed all of the letters, we have won
        if not self.displayed.__contains__('~'):
            return 1

        #if we ran out of guesses, we lose
        elif self.guesses <= 0:
            return -1

        #else we return a 0
        #to indicate the game isn't over
        else:
            return 0
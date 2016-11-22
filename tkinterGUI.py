#!/usr/bin/env python3

from tkinter import *
from hangman import hangMan
from tkinter import font as font

class hangManGUI(Frame):
    def __init__(self):
        self.root = Tk()

        Frame.__init__(self, self.root)

        self.pack()

        self.__widgets__(self.__makeGuess__)
        self.__play__()

        self.mainloop()

    def __makeGuess__(self, key):
        if key == "new game":
            self.__play__()

        self.__game.guessLetter(key)
        self.__showDisplay()

    def __showDisplay(self):
        self.__guessCount.config(text=str("Guesses:" + str(self.__game.guesses)))

        self.__displayed.configure(state='normal')

        self.__displayed.delete('1.0', END)

        self.__displayed.insert(END, '\n')

        for l in self.__game.displayed:
            self.__displayed.insert(END, str(l))

        self.__guessedLetters.configure(state='normal')

        self.__guessedLetters.delete('1.0', END)

        for l in self.__game.guessed:
            self.__guessedLetters.insert(END, str(l))

        self.__guessedLetters.configure(state='disabled')


    def __widgets__(self, callback):
        #initialize the buttons
        j = 0
        i = 0
        block = 10
        mRow = 0

        letters = [['q','w','e','r','t','y','u','i','o','p'],
                   ['a','s','d','f','g','h','j','k','l'],
                   [' ','z','x','c','v','b','n','m','new game']]

        self.__buttons = Frame(self)
        self.__buttons.grid(row=1, column=0)

        for column in letters:
            for l in column:
                if l.isalpha():
                    b = HMButton(self.__buttons, callback, text=str(l))
                    b.config(width=block)
                    b.grid(row=i, column=j, columnspan=1, sticky=N + E + W + S)

                if len(l) > 1:
                    b = HMButton(self.__buttons, callback, text=str(l))
                    b.config(width=block)
                    b.grid(row=i, column=j, columnspan= mRow - j + 1, sticky=N + E + W + S)


                if mRow < j:
                    mRow = j

                j+=1

            j=0
            i+=1

        #set the upper portion of the GUI
        self.__upper = Frame(self, width = 10, height = 10)
        self.__upper.grid(row=0, column=0)
        self.__font = font.Font(family='Helvetica', size=30, weight='bold')

        #set the text
        self.__displayed = Text(self.__upper, font = self.__font, height=5, width=20)
        self.__displayed.config(state=DISABLED)
        self.__displayed.grid(row = 2, column = 1)

        #set the guess portion
        self.__guessDisplay = Frame(self.__upper)
        self.__guessDisplay.grid(row=0, column=0, sticky=N+W)

        self.__guessCount = Label(self.__guessDisplay)
        self.__guessCount.grid(row=0, column=0, sticky=N+W)

        self.__guessedLetters = Text(self.__guessDisplay, font=self.__font, height = 1, width=20)
        self.__guessedLetters.config(state=DISABLED)
        self.__guessedLetters.grid(row=1, column=0, stick=N+W)

    def __play__(self):
        self.__game = hangMan()
        self.__showDisplay()

class HMButton(Button):
    def __init__(self, master, command, text):
        Button.__init__(self, master, command = lambda : command(text), text=text)


h = hangManGUI()
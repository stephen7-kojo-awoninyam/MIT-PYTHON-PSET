# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:10:59 2023

@author: Win11
"""

# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
WILDCARD = '*'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*': 1, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):

    # converting all letters to lowercase
    word = word.lower()

    first_component = 0

    # formular for finding the second component
    second_component = 7*len(word)-3*(n-len(word))

    # if statement to check whether the second component is greater than or equal to on
    if second_component < 1:

        # if lesser than one assign 1 to the second component
        second_component = 1

    else:

        # else use the value generated from the formular
        second_component = second_component

    # loop over the word to calculate the value of the word based on the dictionary
    for index in range(len(word)):

        char = word[index]

        first_component += SCRABBLE_LETTER_VALUES[char]

    # assign the product of the two component to a variable score
    score = second_component * first_component

    # return the results
    return score

    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    pass  # TO DO... Remove this line when you implement this function

#
# Make sure you understand how this function works and what it does!
#


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    hand[WILDCARD] = hand.get(WILDCARD, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#


def update_hand(hand, word):
    # converting the words to lowercase
    word = word.lower()

    # copying the content of dictionary hand to the variable newWord so that the original dictionary wont be modified
    newWord = hand.copy()

    # looping through the words
    for letter in word:

        # checking if the the word is in the hands and its more than one
        if letter in newWord and newWord[letter] >= 1:

            # if its more than one decrease the word by one
            newWord[letter] -= 1

        else:

            # if its not in the hand or frequencyh is zero print
            print("letter not in hand", letter)
    # return the dictionary
    return newWord

    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 
    
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
   """

    pass  # TO DO... Remove this line when you implement this function

#
# Problem #3: Test word validity
#


def is_valid_word(word, hand, word_list):
    word = word.lower()
    # Copy the content of the hand dictionary to the variable checkWord
    checkWord = hand.copy()

    # Check if the word contains a wildcard character (*)
    if WILDCARD in word:
        # Replace the wildcard with each vowel and check if any variation is valid
        for vowel in VOWELS:
            # replace the wildcard with a vowel
            word_with_vowel = word.replace(WILDCARD, vowel)
            # after replacing the wildcard with a vowel, form a new word with it
            checkWord = get_frequency_dict(word_with_vowel)
            if is_valid_candidate(word_with_vowel, checkWord, word_list):
                return True
            # return False  # If no variation is valid, return False
    else:
        # Check if the original word is valid
        return is_valid_candidate(word, checkWord, word_list)


def is_valid_candidate(word, checkWord, word_list):
    # Loop through the characters in the candidate word
    for char in word:
        # Check that the characters in the candidate word are in the hand
        if char in checkWord and checkWord[char] > 0:
            # Decrease the value of the repeated character by 1
            checkWord[char] -= 1
        else:
            # If the character is not in the hand, return False
            return False

    # Loop through the word list to check if the candidate word is in it
    for words in word_list:
        # If the candidate word is in the word list, return True

        if words.lower() == word:
            return True

    # If the candidate word is not in the word list, return False
    return False

    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    pass  # TO DO... Remove this line when you implement this function

#
# Problem #5: Playing a hand
#


def calculate_handlen(hand):

    handWord = hand.copy()

    val = int(handWord.value())

    count = 0

    for i in val:

        count += i

    return count

    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """

    pass  # TO DO... Remove this line when you implement this function


def play_hand(hand, word_list):

    handWord = hand.copy()

    score = 0

    string1 = ""

    print(handWord)

    while True:

        user_word = input(
            "Enter word, or !! to indicate that you are finished: ")

        if user_word == "!!":

            break

        else:

            if is_valid_word(user_word, handWord, word_list):

                print(get_word_score(user_word, len(user_word)))

                score += get_word_score(user_word, len(user_word))

            else:

                print("word not valid")

            for letters in hand:

                for char in user_word:

                    if char not in letters:

                        string1 += char

                handWord = get_frequency_dict(string1)

            play_hand(handWord, word_list)

    return score

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score

    # As long as there are still letters left in the hand:

    # Display the hand

    # Ask user for input

    # If the input is two exclamation points:

    # End the game (break out of the loop)

    # Otherwise (the input is not two exclamation points):

    # If the word is valid:

    # Tell the user how many points the word earned,
    # and the updated total score

    # Otherwise (the word is not valid):
    # Reject invalid word (print a message)

    # update the user's hand by removing the letters of their inputted word

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function


#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):

  # combine the vowels and consonants as one

    ALPHABET = VOWELS + CONSONANTS

    # convert the alphabet into a list

    ALPHALIST = list(ALPHABET)

    # shuffle the list for fairness in randomization

    random.shuffle(ALPHALIST)

    # convert the shuffled list of alphabet back to string

    ALPHABET = ''.join(ALPHALIST)

    # loop through the letters in the hand

    for char in hand.keys():

        # if the letter to be replaced not in the hand

        if letter not in hand.keys():

            # return the original letters in the hand

            return hand

        # else if the letter is in the hand but its value less than or equal to 1

        elif letter in hand.keys() and hand[letter] <= 1:

            # return the original letters in the hand

            return hand

        else:

            # choose a letter rondomly from the alphabet

            article = random.choice(ALPHABET)

            # replace the random letter with the letter you want to replace

            hand[article] = hand.pop(letter)

    # return the new hand

    return hand

    """ 
        Allow the user to replace all copies of one letter in the hand (chosen by user)
        with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
        should be different from user's choice, and should not be any of the letters
        already in the hand.

        If user provide a letter not in the hand, the hand should be the same.

        Has no side effects: does not mutate hand.

        For example:
            substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
        might return:
            {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
        The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
        already in the hand.

        hand: dictionary (string -> int)
        letter: string
        returns: dictionary (string -> int)
        """

    pass  # TO DO... Remove this line when you implement this function


def play_game(word_list):
    # number of letters the hand can accomodate
    n = 7
    
    # initializing the total score
    total_score = 0
    
    # checks how many times you want to play the game
    total_hands = int(input("Enter the number of hands to play: "))
    
    # Initializing the can substitute to true
    can_substitute = True
    
    # Initializing the can play to true
    can_play = True
    
    # using the while loop to check the number of times to play the game
    while total_hands > 0:
        
        # generating new set of hands
        hand = deal_hand(n)
        
        # Displaying the genreated letters in hands  
        print("Current Hand:",end=" ")
        
        display_hand(hand)
        
        # check if th  user want to  make substitution to a letter
        if can_substitute:
            # prompt the user to enter yes if so
            substitute = input("Do you want to substtute a word?: ") == "yes"
            
            # if so 
            if substitute:
                # then it should be done once
                can_substitute = False
                # prompt the user to enter the letter he want to replace
                letter = input("Enter the letter to replace: ")
                # assign the new hand to the initial hand
                hand = substitute_hand(hand, letter)
         
        # calculate the score of the hand using the play hand function    
        score = play_hand(hand, word_list)  
        
        # ask the user he wants to replay again and prompt him to enter yes
        if can_play and input("Do you like to play?: ") == "yes":
            
            # then it should be done once
            can_play = False 
            
            # calculate the new score for the replay
            score2 = play_hand(hand, word_list)
            
            # compare the initial and final score and give us the highest
            score = max(score,score2)
            
        # add it to the total score 
        total_score += score    
        
        # print the total score
        print("the total score is:" ,total_score)
            
            
            
            
    
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    # TO DO... Remove this line when you implement this function
    print("play_game not implemented.")


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

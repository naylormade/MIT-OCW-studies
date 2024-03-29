import random
import string
import re


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    inFile = open("words.txt", 'r')
    line = inFile.readline()
    wordlist = line.split()
    #print(f'    {len(wordlist)} words loaded.')
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    listy = []
    for letter in secret_word:
      if letter in letters_guessed:
        listy.append(letter)
      elif letter is " ":
        listy.append(" ")
      else:
        listy.append("_")
    return ''.join(listy)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    return ''.join([x for x in string.ascii_lowercase if x not in letters_guessed])
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    word = choose_word(wordlist)
    num_guesses = 6
    print("Welcome to Hangman")
    print(f'The secret word is {len(word)} characters long and you have {num_guesses} guesses.')

    while num_guesses > 0:
      
      print(f'Guesses left: {num_guesses}')
      print(f'Letters that have not been used: {get_available_letters(letters_guessed)}')
      guess = input("Please choose a letter to guess: ").lower()
      while guess not in string.ascii_lowercase:
        guess = input("Please choose a LETTER to guess: ").lower()
      letters_guessed.append(guess)
      print(get_guessed_word(word, letters_guessed))

      if is_word_guessed(word, letters_guessed):
        break
      num_guesses -= 1
      print("\n")
      if num_guesses == 0:
        print("You have used all your guesses!")
        print(f'The word is {word}.')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    if len(my_word.strip()) != len(other_word):
      #print("False cus length")
      return False
    for letter in my_word:
      if letter == "_":
        continue
      if letter not in other_word:
        #print("False cus no match")
        return False
    #print("True")
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    pattern = " "

    for ch in my_word:
      if ch in string.ascii_lowercase:
        pattern += ch
      elif ch == "_":
        pattern += "[a-z]"
      else:
        break  # shouldn't get here
    # add space to ensure it is an actual word
    pattern += " "
    potential_matching_words = set(re.findall(pattern, ' '.join(wordlist)))
    stripped = [x.strip() for x in potential_matching_words]
    print(f'hints: {stripped}')
    return sorted(stripped)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    word = choose_word(wordlist)
    num_guesses = 6
    print("Welcome to Hangman")
    print(f'The secret word is {len(word)} characters long and you have {num_guesses} guesses.')

    while num_guesses > 0:
      print('--------------')
      print(f'Guesses left: {num_guesses}')
      print(f'Available letters: {get_available_letters(letters_guessed)}')
      guess = "$"
      while guess not in string.ascii_lowercase:
        guess = input("Please guess a letter: ").lower()
        if guess == "*":
          show_possible_matches(get_guessed_word(word, letters_guessed))
      letters_guessed.append(guess)
      print(get_guessed_word(word, letters_guessed))

      if is_word_guessed(word, letters_guessed):
        break
      num_guesses -= 1
      print("\n")
      if num_guesses == 0:
        print("You have used all your guesses!")
        print(f'The word is {word}.')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

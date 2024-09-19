# define fonction that will return a word. We can create a list of words or import a list.
import random

word_list = ['unadvised'
'heavy','false','cherry','excuse','festive','park','hate','rule','dream','boundary','fall','applaud','swing','geese''suit',
'rural''cagey''long-term''squash''brainy''mitten''feigned''numerous''healthy''hour''malicious''rose''harmonious''juicy''fire''rambunctious''pine''multiply''sneaky''roof'
'boring','bedroom''mint''worthless''anger''delay''undress''copy''aboard''berry''tax''even''purpose''massive''market''rail''grouchy''therapeutic''punish''toe'
'observation''lavish''crash''pet''shocking''boat''rhythm''detect''testy''bee''whine''horrible''automatic''glorious''damaging''terrific''doctor''gate''change'
'maddening''drag''snobbish''trace''extra-large''tenuous''frequent''snakes''trade''nappy''common''practice''lace''watery''cactus''haunt''rampant']

def get_word():

    word = random.choice(word_list) 
    return word.upper()# the word will return in uppercase


#for the game 
def play(word):

#the list of variables
    word_completion = "_" * len(word) #same lenght as the choosen word but contains only underscores
    guessed = False #our variable guessed is inialiazed to false
    guessed_letters = [] #contains the letter the user guessed
    guessed_words = [] #contains the words the user guessed
    tries = 6 # the number of tries left before the user loses
    print("Welcome to the Hangman Game!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")#print new line

    while not guessed and tries > 0: #The condition says that the game runs until the word is guessed or there's no more tries
        guess = input("Please guess a letter or word").upper()
    # 3 possible cases: 
        # 1: Guessing a letter
        # 2: Guessing a word
        # 3: or guessing something else like special characters or numbers

#Here guess has length of one and contains only characters from the alphabets
    if len(guess) == 1 and guess.isalpha():
#Here it means that the word guessed is equal to the length of the actual word and contains only letters
        
#This variable means that verfifies if the letter had already bean guessed, if the letter is in the word or is not in the word 
        if guess in guessed_letters:
            print('Letter already guessed. Try another one', guess)

        elif guess not in word:
            print(guess, 'is not in the word')
            tries -= 1 #here we decrement the number of trie left
            guessed_letters.append(guess) #here 'append' adds the letter guessed in the list of letters already guessed
        else:
            print('Well done', guess, 'is the word')#here the user guessed the word
            guessed_letters.append(guess)
            word_as_list = list(word_completion)#new variable to update the number of guesses is left for the user
        elif len(guess) == len(word) and guess.isalpha():
        
            if guess in guessed_words:
                print('You already guessed that word', guess)
            elif guess != word:
            print(guess, "its not the word.")
            tries -= 1
            guessed_words.append(guess)
    else:
        guessed = True
        word_completion = word

        else:
            print('Word not valid')
            print(display_hangman(tries))
            print(word_completion)
            print("\n")
        
        if guessed:
            print('Congrats, you guessed the word!')
        else:
            print('You run out of tries. The word was' + word ".")
            




def display_hangman(tries):
    stages = [  # final state
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
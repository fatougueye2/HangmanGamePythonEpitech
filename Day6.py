############1.1#############
def f ( x ) :
    return 2 * x + 1
def g () :
    return 7
y = f (2)
#print ( y )
y = f (5) + g ()
#print ( y )

#"Pour la premiere fonction f prend en argument x. si x est egal a 2, elle le multiplie x par 2 + 1"
#"La seconde retourne le resultat 7"
#"La fonction f est appelé avec x = 2. La valeur 5 est affecté a la valeur y"
#"Dabord y est calculer 2 * 5 + 1, ensuite g (7) est appelé, et enfin la valeur est affecté a y"

#################1.2##################
"""""
def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print ("O O O O O O")
def ham () :
    print (" ============ ")
def ham () :
    print (" ============ ")
def bread () :
    print (" <////////// > ")


bread()
lettuce()
tomato()
ham()
ham()
bread()
"""

##################1.3###################


"""""
def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print ("O O O O O O")
def ham () :
    print (" ============ ")
def ham () :
    print (" ============ ")
def bread () :
    print (" <////////// > ")

for _ in range(42):
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()

"""
    
###################1.4###############

""""
def prepare_sandwiches(42):

    if not isinstance(42, int)  or 42 <= 0: print("I can't do this") 
    return

def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print ("O O O O O O")
def ham () :
    print (" ============ ")
def ham () :
    print (" ============ ")
def bread () :
    print (" <////////// > ")

for _ in range(42):
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()
    
 """""

#################1.5##################




################Challenge##############

###### Option recursive 
#import time

# Python3 program for the above approach
#def power(x, n):

    # If x^0 return 1
    #if (n == 0):
        #return 1

    # If we need to find of 0^y
    #if (x == 0):
        #return 0

    # For all other cases
    #return x * power(x, n - 1)


# Driver Code
#if __name__ == "__main__":
   # x = 42
   # n = 84

    # Function call
    #print(power(x, n))

##################2.1###################
""""
def clean(s):
      return "".join(c.lower() for c in s if c .isalnum)


def palyn(k, y, a):
        if (y == a):
            return True #si il y a une seule lettre
        
        if (k[y] != k[a]):
            return False #si elle est premiere ou derniere et si les lettre ne corresponde pas
        
        if (y < a + 1) :
            return palyn(k, y + 1 , a - 1)
        
        return True #si il y a plus de 2 characters, verifie si le string du milieu est un palyndrome


k = "kayak"
if(palyn(k)) :
        print: "yes"
else:
        print: "no"
"""
######## second code
"""
import string 

def palyndrome(s): 

    return ''.join(c.lower() for c in s if c.isalnum())

def is_palindrome(s): 

 # Clean the string 

    cleaned_palyn = palyndrome(s)

 # For this recursive case, we check first and last characters, and then the substring in between 

    if cleaned_palyn[0] == cleaned_palyn[-1]:

        return is_palindrome(cleaned_palyn[1:-1]) 
    else: return False 

print(palyndrome("kayak")) # True 
print(palyndrome("never odd or even")) # True 
print(palyndrome("Was it a car or a cat I saw?")) # True 
print(palyndrome("hello")) # False
"""


################2.2#################
"""
import os

def list_files_walks(start_path="."):

    for root, dirs,files in os.walk(start_path):
        for file in files:
            print(os.path.join(root, file))

####specifie ou le chemin commence
directory_path = './'
list_files_walks(directory_path)            

"""

#################3.1###############

"""
def funA(s : str, n: int) -> bool:
    s.count_lowercase( 1 for char in s if char.islower)
    print()

def funB(s : str, n: int) -> bool:
    s.count_uppercase( 1 for char in s if char.isupper)
    print()

def funC(s : str, n: int) -> bool:

    for s in str:

        if s.isalpha():
            funC = True
    print()

import re
def funD(s : str, n: int) -> bool:
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if(regex.search(s) == None):
        print("string accepted")

def funE(s : str, n: int) -> bool:
    if s.isdigit:
        funE = True
    print()

"""    
################3.2##################

import re 

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]",password):
        return False
    
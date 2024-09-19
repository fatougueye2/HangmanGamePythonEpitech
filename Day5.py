#numbers = []
#for i in range(1,7):
 #  numbers.append(i)
#numbers.remove(6)
#print(numbers)

###########Task 1.7##############
#my_list = [1,2,3,4,5,6,7,8,9,10]

#sublist = my_list[2:5]

#print(sublist)

##########Task 1.8##########

#old_list = [1,2,3,4,5,6,7,8,9,10]

#def reversed(old_list):
   # newlist = old_list[::-1]
   # return newlist

#print(reversed(old_list))


##############Task 1.9############

#my_list = [1,2,3,4,5,6,7,8,9,10]

#result = my_list[::2]

#print(result)

################1.10###############



###############1.11################

#my_first_list = [4 , 5 , 6]
#my_second_list = [1 , 2 , 3]
#my_first_list . extend ( my_second_list )


#my_first_list = [4 , 5 , 6]
#my_second_list = [1 , 2 , 3]
#my_first_list . extend ( my_second_list )

#print(my_first_list)

#ajoute les elements de ma premiere liste a la seconde et vice-versa

#############"2.1"#################

#### Genere liste de 1 a 10
#my_list = range(1,11)
#print(list(my_list))

#import math
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#result = math.prod(numbers)

#print( result)


#############2.2###############

# print(x + 10 for x in [3, 2, 6, 7, 1, 4])

# On ajoute 10 au resulat de la liste

##############2.3##############
#print(list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4])))

#On declare x comme un elements de la liste, ensuite on ajoute nos expressions( [3, 2, 6, 7, 1, 4]) que l'on passe dans la liste.

###############2.4#############

#print(min([-203,5,9,13,40,150]))

#print(max([-203,5,9,13,40,150]))

################2.5#############

#my_list = [-203,5,7,9,13,40,150]

#smaller = [x for x in my_list if x > 7]

#print(smaller)

##############2.6###############

#my_list = [-203,5,7,9,13,40,150]

#my_list.sort(reverse = True)

#print(my_list)

#############2.7################

#print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])

#Division par 2 si pair, sinon multiplication par deux si impair

###############2.8##############

#print(list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10])))

#filter ici permet de sélectioner les éléments strictement superieur a 10. le resultat est [42, 18]

###############2.9##############

#print([*enumerate([42, 3, 4, 18, 3, 10])])

#La fonction enumerate() ajoute un compteur à un itérable et le renvoie sous la forme d'un objet énumérateur.
#En gros enumerate ajoute un indice a chaque nombre pair. * permet de décompresser pour afficher le resultat

###############2.10#############

#first_name = [" Jackie ", " Bruce ", " Arnold ", " Sylvester "]
"""last_name = [" Stallone ", " Schwarzenegger ", " Willis ", " Chan "]
magic = [* zip ( first_name , last_name [:: -1]) ]
print ( magic [0]) #1er element de la 1ere liste
print ( magic [3]) #4eme element de la liste magique
print ( magic [1][0])
print ( magic [0][1])
print ( magic [2])
"""
#La fonction zip est une fonction qui permet de combiner plusieurs itérateurs en un seul objet.
#En gros le code combine la liste de prenoms avec celles des noms, mais en inversants les noms.
#Les tuples sont comme des listes sauf que l'on ne peut pas modifier ses elements.

###############challenge###########

#startingTime = time.time()

#duration = time.time()- startingTime

###############3.1#################

dictionary = {}

name = ['Camille','Yarong', 'Aida','Fatou']
academic_year = ['2021', '2022', '2023', '2024']

graduation = [* zip ( name , academic_year) ]

print ( graduation[0])

##############3.2#################











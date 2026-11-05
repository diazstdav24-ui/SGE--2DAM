"""
15. Determine si una cadena de texto dada es un isograma, es decir, no se repite ninguna letra. 
Ejemplos válidos de isogramas: 
background 
downstream 
six-year-old 
"""

word = "six-year-old "

letters = list(word)

copy_letters = letters.copy()

bag = []

isograma = True

for letter in letters: 

    if letter.isalpha() in bag:

        isograma = False

        break;

    bag.append(copy_letters.pop(copy_letters.index(letter)))


print("Isograma es:",isograma)
        

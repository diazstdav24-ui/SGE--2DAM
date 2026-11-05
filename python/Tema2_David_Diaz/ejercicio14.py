"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

"""

word = "anita lava la tina"

letters = list("".join(word.split()))

print(letters)

letters_reversed = list(reversed(letters))

print(letters_reversed)

is_palindromo = False

if letters_reversed == letters: 

    is_palindromo = True


print(is_palindromo)

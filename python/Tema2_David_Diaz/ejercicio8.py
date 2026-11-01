"""
8. Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera 
lista los nombres que haya en la segunda lista.

"""


continuar = True

list1 = ["a","b","c"]
list2= ["c","d","f"]
switch = 0

while continuar: 


    word = input('word: ')

    if switch == 0: 
        list1.append(word)
    else:
        list2.append(word) 


    reply = int(input('Do u want continue filling the list? 1.Y/2.N \n'))

    if reply == 2 and switch == 0: 

        print('Next list: ')
        switch = 1

    elif reply == 2 and switch == 1:

        continuar = False 


    


print(','.join(list1))

print(','.join(list2))

copy_list1 = list1.copy()

for word in list1:

    if word in list2:

        copy_list1.remove(word)
 

print('Newest lists: ')

print(','.join(copy_list1))

print(','.join(list2))

    



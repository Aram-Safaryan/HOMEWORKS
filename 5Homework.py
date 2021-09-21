"""DATA STRUCTURES"""

# 1. Write a program to multiply all the items in a list.
# Գրել ծրագիր, որը կբազմապատկի լիստի բոլոր թվերը։



# Lst = [3, 5, 2, 3, 5]
#
# result = 1
#
# for i in Lst:
#     result *= i
# print (result)


# 2. Write a program to count the number of strings where the string length is 2 or more and the first and last
# character are same from a given list of strings.
# Գրել ծրագիր, որը կհաշվի լիստում եղած 2 կամ ավել երկարություն ունեցող լիստերի քանակը, որոնց առաջին և վերջին տառերը
# նույնն են։


# Lst = ['kiuyhk', 'j', 'hygffrh', 'klk', 'jhugh']
#
# total = 0
#
# for i in Lst:
#     if len(i) >= 2 and i[0] == i[-1]:
#         total += 1
# print (total)


# 3. Write a program that will remove duplicates from a list. DO NOT use set() method directly on the list.
# Գրել ծրագիր, որը կջնջի դուպլիկատները լիստից։ ՉՕԳՏԱԳՈՐԾԵԼ set() մեթոդը։


#lst = ['ggg', 'ggg', 'giuyhi', 'yfy', 'h', 'gjjhg', 'h', 'h']
#
#for i in lst:
#    if lst.count(i) != 1:
#        lst.remove(i)
#print (lst)


# 4. Create a list from 5 user inputs.
# Ստեղծել լիստ 5 ներմուծված թվերից


# x = int(input())
# y = int(input())
# z = int(input())
# m = int(input())
# n = int(input())
#
# lst = [x, y, z, m, n]
# print (lst)



# 5. Write a program to print the given list after removing the 2nd, 4th and 5th elements.
# Գրել ծրագիր, որը կջնջի տրված լիստի 2-րդ, 4-րդ և 5-րդ էլեմենտները։



lst = ['Rock', 'Pop', 'Metal', 'Hip-Hop', 'Rap']
# del lst[1]
# del lst[2]
# del lst[2]
#
# print (lst)
#
# lst.remove('Pop')
# lst.remove('Hip-Hop')
# lst.remove('Rap')
#
# print (lst)
#
# lst.pop(1)
# lst.pop(2)
# lst.pop(2)
#
# print (lst)



# 6. Given a list of ints, print True if the array contains a 2 next to a 2 somewhere.
# Գրել ծրագիր, որը կտպի True, եթե տրված լիստում ինչ-որ տեղ 2 թվին 2 է հաջորդում։

# lst = [1, 54, 3, 2, 2, 5, 6, 2, 4]

# for i in lst:
#    if i == 2 and lst[lst.index(i) + 1] == 2:
#        print ('True')


# 7. Given a list of ints, print True if every element is a 1 or a 4, and False otherwise.
# Գրել ծրագիր, որը կտպի True, եթե լիստի բոլոր էլեմենտները 1 կամ 4 են։ Հակառակ դեպքում տպել False:

#լուծված է

# lst = [1, 4, 8, 5, 1]
#
# lst1 = []
#
# for i in lst:
#    if i == 1 or i == 4:
#        lst1.append(i)
# if lst == lst1:
#    print (True)
# else:
#    print ('False')



# 8. Ask for user input and add that input as a key into the dictionary. Assign some arbitrary value to it.
# 8. Ask for user input and add that input as a key into the dictionary. If the key exists, warn the user about it and
# do nothing. Assign some arbitrary value to it.
# Պահանջել ներմուծել բանալի և ավելացնել այդ բանալին dictionary-ի։ Եթե այն արդեն գոյություն ունի, տպել, որ բանալին արդեն
# կա և ոչինչ չանել։ Որպես արժեք տեղադրել պատահական օբյեկտ


# grades = {'key1': 7,
#          'key2': 11,
#          'key3': 10, }
# key = input()
# if input() != grades.keys:
#    grades.update({key: 5})
#    print (grades)
# if input() == grades.keys:
#    print ('already exists')


# 9. Loop through the values of a dictionary and add them to a new list.
# Ցիկլի միջոցով ավելացնել dictionary—ի արժեքները նոր լիստի մեջ։


# grades = { 'key1': 7,
#           'key2': 11,
#           'key3': 10,}
# lst = []
# for i in grades.values():
#    lst.append(i)
# print (lst)


# 10. Write a script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys.
# Գրել ծրագիր, որը կստեղծի և կտպի dictionary, որի բանալիները [1,15] թվերն են, իսկ արժեքները դրանց քառակուսիները։


# dict = {}
#
# for i in [1,15]:
#     key = i
# for j in [1,225]:
#     value = j
#
# dict.update({key: value})
# print(dict)

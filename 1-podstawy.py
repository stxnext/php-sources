
''' OGÓLNY POGLĄD NA SYNTAX '''


print "Witamy w Pythonie!"
num_var = 5
limit_var = 10

def first_function():
    print "Iteracja po " + str(limit_var) + " liczbach" # komentarz!
    for x in range(limit_var):
        if x == num_var:
            print "x równe {}".format(x)
        else:
            print ""
    


''' DEFINICJE FUNKCJI'''


def print_word(word):
    print word
    
 
def print_args(*args):
    for index, value in enumerate(args):
        print '{0}. {1}'.format(index, value)
 
print_args('apple', 'banana', 'cabbage')


def print_kwargs(**kwargs):
    for name, value in kwargs.items():
        print '{0} is {1}'.format(name, value)
    
print_kwargs(apple='fruit', cabbage='vegetable')


def print_default_value(apple, cabbage='vegetable', **kwargs):
    for name, value in kwargs.items():
        print '{0} is {1}'.format(name, value)
        print 'Apple is {}'.format(apple)
        print 'Cabbage is {}'.format(cabbage)
 
print_default_value(apple = 'fruit')
print default_value('fruit')




''' IMPORTOWANIE'''


import math
import sys

from django.forms import *

import our_application.module 




'''CZESTE OPERACJE NA TYPACH DANYCH'''


# program losuje zbiór 6 unikatowych liczb od 1 do 49
from random import choice
wylosowane = set()

while len(wylosowane) < 6:
    wylosowane.add(choice(range(1,50)))
    
for x in wylosowane:
    print x
    
    
# przykład iteracji po słownikach
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}

for val in dishes.values():
    print val
    
for key in dishes.keys():
    print key
    
for key, val in dishes.items():
    print key, val
    
    

# Lista Ocen Studentów przy wykorzystaniu klas
class Student:
    imie = ""
    nazwisko = ""
    ocena = 0.0
    
studenci = []
while True:
    nazwisko = raw_input('Podaj nazwisko studenta (pusta wartosc=koniec): ')
    imie = raw_input('Podaj imie studenta > ')
    ocena = raw_input('Podaj ocene studenta > ')
    
    if not(nazwisko and imie and ocena):
        break
    
    student = Student()
    student.nazwisko = nazwisko
    student.imie = imie
    student.ocena = float(ocena)
    studenci.append(student)
    
for idx, student in enumerate(studenci):
    print '{}. {} {} {}'.format(idx+1, student.nazwisko, student.imie, student.ocena)
    
    
# DEBUGOWANIE

import pdb; pdb.set_trace()

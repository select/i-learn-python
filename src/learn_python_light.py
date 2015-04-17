#!/usr/bin/env python

#///////////////////////////////////////////////////////////////
def levelCodeOrFail(lc=True):
	if lc:
		print '''Please enter the level code as first argument!'''
	else:
		print '''Sorry this is not correct, please try again.'''

#///////////////////////////////////////////////////////////////
def level0(level_code=''):
	if not level_code:
		print '''
To complete this exercise you need to call this function with the 
level code: 8Xsu33Hn
Here is an example:
In [1]: level0('levelcode')
		'''
	elif level_code=='8Xsu33Hn':
		print '''
Hoooray you made it!

You can go to the next level.
The level code is: 9fCkmGsy
You will reach the next level by calling 
level1('9fCkmGsy')
'''
	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
#float
def level1(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='9fCkmGsy':
		if not input:
			print '''
To complete this exercise insert the number 4 as a float.
Here is an example:
In [1]: level1('levelcode',5.1)
'''
		elif isinstance(input, float) and input==4.0:
			print '''
Good! 

You can write either 4.0 or float(4) to make 4 a float.

The next level code is: YXHIY9AF
call level2('YXHIY9AF')
'''
		else:
			levelCodeOrFail(False)
	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
#string
def level2(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='YXHIY9AF':
		if not input:
			print '''
To complete this exercise insert the string:

I like 2 go 2 the next level

Hint: - if you put your string into a variable, you can reuse it in the next level.
here is an example:
In [1]: level2('levelcode','answer string')
'''
		elif input=='I like 2 go 2 the next level':
			print '''
You made it!

The next level code is: L34XSOq9 
call level3('L34XSOq9')
'''
		else:
			levelCodeOrFail(False)
	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
#list (str.split())
def level3(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='L34XSOq9':
		if not input:
			print '''
To complete this exercise insert the string from level 2 as a list of words
here is an example:
In [1]: level3('levelcode',['answer', 'string'])
'''
		elif input==['I', 'like', '2', 'go', '2', 'the', 'next', 'level']:
			print '''
Right on!

The intended way to do it was: my_string.split()

The next level code is: XahS6y6l
call level4('XahS6y6l')
'''
		else:
			levelCodeOrFail(False)
	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
#list[index]
def level4(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='XahS6y6l':
		if not input:
			print '''
To complete this exercise insert only the 3rd element of the list of words from level 3
Hints: 	- you can access list elements with list[index]
	- list start with the index 0
'''
		elif input=='2':
			print '''
Congratulations!

The next level code is: acjYW08p
level5('acjYW08p')
'''
		else:
			levelCodeOrFail(False)
	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
#splicing
def level5(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='acjYW08p':
		if not input:
			print '''
To complete this exercise insert the string from level 2 as an array of words.
This time insert only the first two elements and the last two elements as one list.
Hints: 	- you can extract sub lists by with list[begin:end]
	- you can concatenate lists with the + sign
'''
		elif input==['I', 'like', 'next', 'level']:
			print '''
Phantastic!
                       /
                   ,._/
                  (((6\ 
             _,---) )r`
            ( ( )__))
            ) /// \\\\\ 
              \\\\\\  |\\\ 
              '''  '''
The next level code is: B861yGOX 
level6('B861yGOX')
'''
		else:
			levelCodeOrFail(False)
	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
#Dict
def level6(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='B861yGOX':
		if not input:
			print '''
To complete this exercise put the following codon codes into a dictionary

| Codon | AS |
|============|
|  GCA  | A  |
|  AGU  | S  |
|  UGG  | W  |

'''
		elif input=={'GCA':'A', 'AGU':'S', 'UGG':'W'}:
			print """
Cowabonga!

Fast and easy: my_dict = {'GCA':'A', 'AGU':'S', 'UGG':'W'}

The next level code is: S8MvpTKz 
level7('S8MvpTKz')
"""
		else:
			levelCodeOrFail(False)
	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
#add element to dict
def level7(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='S8MvpTKz':
		if not input:
			print '''
To complete this execise add the Stop-Codon 'UGA' ('UGA': 'Stop') to your dictionary.
'''
		elif input=={'GCA':'A', 'AGU':'S', 'UGG':'W', 'UGA':'Stop'}:
			print '''
All right!

It is easy to add or change an element of your dictionary:
my_dict['UGA'] = 'Stop'
With my_dict.update({'UGA':'Stop'}) you can add or/and change multiple elements at once.

The next level code is: tRT72s8m
level8('tRT72s8m')
'''
		else:
			levelCodeOrFail(False)

	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
#dict.keys
def level8(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='tRT72s8m':
		if not input:
			print '''
To complete this exercise insert the keys of the dictionary from level 7 as a list.
Hint: - In Ipython you will find methods for dictionaries by tabbing.
'''
		elif input==['GCA', 'AGU', 'UGG', 'UGA']:
			print '''
Hoooray!

Yes! my_dict.keys() gave you a list of the keys, while my_dict.values() would give you 
a list of the values (here: ['A', 'S', 'W', 'Stop']).

The next level code is: e82OApRu
level9('e82OApRu')
'''
		else:
			levelCodeOrFail(False)

	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
#dict.items
def level9(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='e82OApRu':
		if not input:
			print '''
To complete this exercise produce a list of (key, value) pairs and insert it into the function.
'''
		elif input==[('GCA', 'A'), ('AGU', 'S'), ('UGG', 'W'), ('UGA', 'Stop')]:
			print '''
Well done!

my_dict.items() produces a list of (key, value) pairs as 2-tuples.

                  ."`".
              .-./ _=_ \.-.
             {  (,(oYo),) }}
             {{ |   "   |} }
             { { \(---)/  }}
             {{  }'-=-'{ } }
             { { }._:_.{  }}
             {{  } -:- { } }
             {_{ }`===`{  _}
            ((((\)     (/))))

The next level code is: Ju22w99B
level10('Ju22w99B')
'''
		else:
			levelCodeOrFail(False)

	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
#range
def level10(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='Ju22w99B':
		if not input:
			print '''
To complete this exercise insert a list of integers from 0 to 941 into this function
here is an example:
In [1]: level10('levelcode',[1,2,3])
'''
		elif input==range(942):
			print '''
Super!

I'm sure you used range(942) instead of typing the whole thing.

The next level code is: jDU0R8Jz
level11('jDU0R8Jz')
'''
		else:
			levelCodeOrFail(False)

	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
#sum
def level11(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='jDU0R8Jz':
		if not input:
			print '''
To complete this exercise insert the sum of the integers from 0 to 941 into this function
Hint: - You can use a loop
here is an example:
In [1]: level11('levelcode',1234)
'''
		elif input==443211:
			print '''
Ace!

In [1]: my_sum = 0

In [2]: for element in range(942):
   ....:     my_sum += element
   ....:     

The next level code is: GUa85gw3
level12('GUa85gw3')
'''
		else:
			levelCodeOrFail(False)

	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
def level12(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='GUa85gw3':
		if not input:
			print '''
Do you find a list method to make the exercise from level 11 shorter and avoid the loop?
Hint: - You can use the sum() function for many python objects.
'''
		elif input==443211:
			print '''
Almost done!

In [1]: sum(range(942))

The next level code is: fu73LcBA
level13('fu73LcBA')
'''
		else:
			levelCodeOrFail(False)

	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
def level13(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='fu73LcBA':
		try:
			if not input:
				print '''
write a function that returns (not prints!) the string 
hello world
insert your function as argument into this functions
In [1]: level13('levelcode',myfunction)
'''
			elif input()=='hello world':
				print '''
One more!

In [1]: def my_function():
   ....:     return 'hello world'
   ....: 


The next level code is: kK8SFqj5
level14('kK8SFqj5')
'''
			else:
				levelCodeOrFail(False)

		except:
			print "\nHint: 	Insert the function not its result!"

	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////
def level14(level_code='',input=''):
	if not level_code:
		levelCodeOrFail()
	elif level_code=='kK8SFqj5':
		try:
			if not input:
				print '''
write a function that takes one input argument
if the input is 42 the function should return the bool True
if the input is any other number larger than zero it should return the bool False
if the input is a number smaler or equal to zero it should not return anything 
insert your function as argument
'''
			elif input(42) and not input(23) and input(0)==None and input(-34)==None:
				print '''
You made it all through!!

In [1]: def my_2nd_function(my_input):
   ....:     if my_input == 42:
   ....:         return True
   ....:     elif my_input > 0:
   ....:         return False
   ....: 


Here is your typing rhino!
  

                        ,       ,
                       /|    |\./'.
                      | |  ,  \|| ,|
                      \  \_(\.-""\//.  _
                    .-'`""``"` _   ` `-.`"""--.._      _..----. __
                    | '~`      o\                `"---"        `. `"-.==,
                     \,.-;    `"`                                |`""`===`
                       (`            /                           |
       .-------.        `-----.____.;          \     |           ;
      _|~~ ~~  |_                   \__         |    \          /
    =(_|_______|_)=                .'         .'      \        ' `,
      |:::::::::|                 /          /         '._        |
      |:::::::[]|                 |    '.---;`-.____.-'`\ `""`;   |
      |o=======.|                 |     _\   \    '.     )   /    \ 
      `"""""""""`                 \-,--( /   /    _/   .'   |_ _ .-)
                                   '----;)__;    (`.-. ;    `-:.;-'
                                                  `""""`

'''
			else:
				levelCodeOrFail(False)

		except:
			print "\n:( this can't be right"
	else:
		print 'wrong level code'
#///////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////
#if __name__=="__main__":
print '''
This module contains excercises in the form of functions.
The functions always expect a level code as input argument.
If you solved the exercise the function will return the level code of the next level.
start with level 0 by calling the function level0

level0()
'''
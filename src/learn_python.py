#!/usr/bin/env python


try:
    import IPython
except ImportError:
    print 'no Ipython available :('
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
To go to the next level you need to call this function with the
level code: 8Xsu33Hn
here is an example:
In [1]: level0('8Xsu33Hn')
        '''
    elif level_code == '8Xsu33Hn':
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


def level1(level_code='',  input=''):
    if not level_code:
        levelCodeOrFail()
    elif level_code == '9fCkmGsy':
        if not input:
            print '''
To complete this exercise insert a list of integers from 0 to 941 into this function
here is an example:
In [1]: level1('9fCkmGsy',[0,1,2,3])

Hint: You can check if your answer is right by printing the result like this
In [2]: [0, 1, 2, 3]<ENTER>
Out[2]: [0, 1, 2, 3]

Please do not try to type this list by hand :D
'''
        elif input == range(4):
            print '''
Ok this is the example now insert a list of ints starting with 0 and ending with 941.
            '''
        elif input == range(941):
            print '''
This is not correct, please print the list and look at the last element in the list!
You should enter a list from 0 to 941!
            '''
        elif input == range(942):
            print '''
Good!
The next level code is: YXHIY9AF
In [1]: level2('YXHIY9AF')
'''
    else:
        levelCodeOrFail(False)
#///////////////////////////////////////////////////////////////


def level2(level_code='',  input=''):
    if not level_code:
        levelCodeOrFail()
    elif level_code == 'YXHIY9AF':
        if not input:
            print '''
To complete this exercise insert the sum of the integers from 0 to 941 into this function
Hint: You can use a "for" loop
here is an example:
In [1]: level2('levelcode',1234)
'''
        elif input == 443211:
            print '''
You made it!
The next level code is: L34XSOq9
In [1]: level3('L34XSOq9')
'''
        else:
            levelCodeOrFail(False)
    else:
        print 'wrong level code'
#///////////////////////////////////////////////////////////////


def level3(level_code='',  input=''):
    if not level_code:
        levelCodeOrFail()
    elif level_code == 'L34XSOq9':
        if not input:
            print '''
To complete this exercise insert the string:

I like 2 go 2 the next level

here is an example:
In [1]: level3('levelcode','answer string')
'''
        elif input == 'I like 2 go 2 the next level':
            print '''
Right on!
The next level code is: XahS6y6l
In [1]: level4('XahS6y6l')
'''
        else:
            levelCodeOrFail(False)
    else:
        print 'wrong level code'
#///////////////////////////////////////////////////////////////


def level4(level_code='',  input=''):
    if not level_code:
        levelCodeOrFail()
    elif level_code == 'XahS6y6l':
        if not input:
            print '''
To complete this exercise insert the string from level 3 as a list of words
here is an example:
In [1]: level4('levelcode',['answer', 'string'])
'''
        elif input == ['I', 'like', '2', 'go', '2', 'the', 'next', 'level']:
            print '''
Congratulations!
The next level code is: acjYW08p
In [1]: level5('acjYW08p')
'''
        else:
            levelCodeOrFail(False)
    else:
        print 'wrong level code'
#///////////////////////////////////////////////////////////////


def level5(level_code='', input=''):
    if not level_code:
        levelCodeOrFail()
    elif level_code == 'acjYW08p':
        if not input:
            print '''
To complete this exercise insert only the 3rd element of the list of words from level 4
Hints:  - you can access list elements with list[index]
    - list start with the index 0
'''
        elif input == '2':
            print '''
Cowabonga!
The next level code is: B861yGOX
In [1]: level6('B861yGOX')
'''
        else:
            levelCodeOrFail(False)
    else:
        print 'wrong level code'
#///////////////////////////////////////////////////////////////


def level6(level_code='', input=''):
    if not level_code:
        levelCodeOrFail()
    elif level_code == 'B861yGOX':
        if not input:
            print '''
To complete this exercise insert the string from level 3 as an array of words.
This time insert only the first two elements and the last two elements as one list.
Hints:  - you can extract sub lists with list[begin:end]
    - you can concatenate lists with the + sign
'''
        elif input == ['I', 'like', 'next', 'level']:
            print '''
Phantastic!
The next level code is: S8MvpTKz
In [1]: level7('S8MvpTKz')
'''
        else:
            levelCodeOrFail(False)
    else:
        print 'wrong level code'
#///////////////////////////////////////////////////////////////


def level7(level_code='', input=''):
    if not level_code:
        levelCodeOrFail()
    elif level_code == 'S8MvpTKz':
        try:
            if not input:
                print '''
write a function that returns (not prints!) the string
hello world
insert your function as argument into this functions
In [1]: level7('levelcode',myfunction)
'''
            elif input() == 'hello world':
                print '''
all right!
The next level code is: tRT72s8m
In [1]: level8('tRT72s8m')
'''
            else:
                levelCodeOrFail(False)

        except:
            print "\nHint:  Insert the function not its result!"
    else:
        print 'wrong level code'

#///////////////////////////////////////////////////////////////


def level8(level_code='', input=''):
    if not level_code:
        levelCodeOrFail()
    elif level_code == 'tRT72s8m':
        try:
            if not input:
                print '''
write a function that takes one input argument
if the input is 42 the function should return the bool True
if the input is any other number larger than zero it should return the bool False
if the input is a number smaller or equal to zero it should not return anything 
insert your function as argument
'''
            elif input(42) and not input(23) and input(0) == None and input(-34) == None:
                print '''
Hoooray!
The next level code is: e82OApRu
In [1]: level9('e82OApRu')
'''
            else:
                levelCodeOrFail(False)

        except:
            print "\n:( this cant be right"
    else:
        print 'wrong level code'
#///////////////////////////////////////////////////////////////


def level9(level_code='', input=''):
    if not level_code:
        levelCodeOrFail()
    elif level_code == 'e82OApRu':
        if not True:
            pass
        else:
            try:
                import myexercise
                reload(myexercise)
            except ImportError:
                print '''
write a module called

myexercise

the module should contain a function called

myfunction

the function should take one input argument and return the input as a string
if you are ready recall this function
In [1]: level9('e82OApRu')
'''
                print "could not import the module myexercise ..yet"
                return
            else:
                try:
                    if myexercise.myfunction(1) == '1' and myexercise.myfunction(1.0) == '1.0' and myexercise.myfunction(True) == 'True' and myexercise.myfunction('a') == 'a':
                        print '''
Almost done!
The next level code is: Ju22w99B
In [1]: level10('Ju22w99B')
'''
                    else:
                        print 'import went well, but the function did not work properly'
                except AttributeError:
                    print '''module imported but I could not find the function myfunction'''
    else:
        print 'wrong level code'

#///////////////////////////////////////////////////////////////


def level10(level_code='', input=''):
    if not level_code:
        levelCodeOrFail()
    elif level_code == 'Ju22w99B':
        if not True:
            pass
        else:
            print '''
modify your module so it contains documentation strings for the module and the function
the function should be modified so it contains a keyword argument called

input

the default value of the argument should be

wimp
----------------------------------------------------------------------
'''
            try:
                import myexercise
                reload(myexercise)
            except ImportError:
                print 'could not import the module myexercise'
                return
            else:
                try:
                    if myexercise.myfunction(input=1) == '1' and myexercise.myfunction(input=1.0) == '1.0' and myexercise.myfunction(input=True) == 'True' and myexercise.myfunction(input='a') == 'a' and myexercise.myfunction() == 'wimp' and myexercise.__doc__ and myexercise.myfunction.__doc__:
                        print '''
Ok one more!
The next level code is: jDU0R8Jz
In [1]: level11('jDU0R8Jz')
'''
                    else:
                        print '''could not find documentation strings
or the default value is wrong
or your functions reacts different than before'''
                except AttributeError:
                    print '''module imported but I could not find the function myfunction'''
                except TypeError:
                    print '''no or incorrect keyword argument'''

    else:
        print 'wrong level code'
#///////////////////////////////////////////////////////////////


def level11(level_code='', input=''):
    if not level_code:
        levelCodeOrFail()
    elif level_code == 'jDU0R8Jz':
        if not True:
            pass
        else:
            print '''
make your module executable
your python script should take one input argument
the input argument should be passed to your function and the result should be printed
you can test your own function with

run myexercise.py Bazinga
----------------------------------------------------------------------
'''
            import os
            if os.popen("./myexercise.py yeah").read() == 'yeah\n':
                print '''
You made it!

Here is your Bunny

                    _ _
                   /_/_      .''. 
                =O(_)))) ...'     `.
                   \_\              `.    .''B'zzzzzzzzzzz
                                      `..'
                
                            /|      __  
                           / |   ,-~ /  
                          Y :|  //  /    
                          | jj /( .^  
                          >-"~"-v"  
                         /       Y    
                        jo  o    |  
                       ( ~T~     j   
                        >._-' _./   
                       /   "~"  |    
                      Y     _,  |      
                     /| ;-"~ _  l    
                    / l/ ,-"~    \  
                    \//\/      .- \  
                     Y        /    Y*  
                     l       I     ! 
                     ]\      _\    /"\ 
                    (" ~----( ~   Y.  )   
            ~~~~~~~~~~~~~~~~~~~~~~~~~~    
'''
            else:
                print 'something went wrong check your module'
    else:
        print 'wrong level code'
#///////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    print '''
This Python module is an interactive game to learn the Python programming language.
You play it by solving little programming exercises.
Once you solve such an exercise you can go to the next level.
Start with level 0 by calling the function level0.
This is how it is done:

In [1]: level0()
    '''
    #from IPython.Shell import IPShellEmbed
    import IPython
    ipshell = IPython.embed()
    ipshell()  # this call anywhere in your program will start IPython

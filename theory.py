course_link = "https://www.youtube.com/watch?v=eWRfhZUzrAc"

#############
# Variables #
#############

chessplayer_name = "Magnus"
chessplayer_birthyear = 1990

# Keywords = if, for, while, import.. and so on

##############################
# Expressions and statements #
##############################

# Expression returns a value
# Statement is an operation with a value
# Program = series a statements

2+2; 2*2 # You can write multiple statements separated by semicolon

##############
# Data types #
##############

type("Check a type of a variable or value")
type(1945) == int # check the type
isinstance(1945, int) # or like this

this_is_a_str = "Hello"
this_is_a_int = 99
this_is_a_float = 1.75

## You can set variable to particular type

this_is_a_float_now = float(99) # this is called casting

## Other types

type_complex = "Complex numbers"
type_bool = "Booleans"
type_list = "Lists"
type_tuple = "Tuples"
type_range = "Ranges"
type_dict = "Dictionaries"
type_set = "Sets"

#############
# Operators #
#############

abc = "Alphabet" # assignment

## Arithmetic operators

9 + 9 == 18 # addition
12 - 5 == 7 # substraction
8 * 8 == 64 # multiplication
15 / 3 == 5 # division
11 % 5 == 1 # modulus (remainder)
3 ** 2 == 9 # exponent (power of)
9 // 2 == 4 # floor division

## Negative numbers

10 + -12 == -2

## Plus can be used to concat

concatenated_by_plus = "Mario likes " + "shrooms"

## We can combine assignment and arithmetic operators

kill_count = 19
kill_count += 2 # kill_count = kill_count + 2

## Comparison operators

junior_salary = 72500
senior_salary = 140000

(junior_salary == senior_salary) == False
(junior_salary != senior_salary) == True
(junior_salary > senior_salary) == False
(junior_salary <= senior_salary) == True

## Boolean operators

is_cheap = True
is_tasty = False

(not is_cheap) == False
(not is_tasty) == True

(not not is_cheap) == True

(is_cheap and is_tasty) == False
(is_cheap or is_tasty) == True

## OR

(0 or 2) == 2
(False or "Truthy") == "Truthy"
("Bonnie" or "Clyde") == "Bonnie"
([] or False) == False
(False or []) == []

## AND

(0 and 1) == 0
(1 and 0) == 0
(False and "Igor") == False
("Igor" and "Evgeny") == "Evgeny"
([] and False) == []
(False and []) == False

## Bitwise (rarely used, nobody knows what it does)

# & performs binary AND
# | performs binary OR
# ^ performs binary XOR operation
# ~ performs binary NOT operation
# << shift left operation
# >> shift right operation

## Is & in operators

# is - identity operator (compares 2 objects, returns true if they are the same)
# in - membership operator (if the value is contained the list/other sequence)

## Ternary operator

def is_adult(age):
    return True if age >= 18 else False

#############################
#############################
chapter_title = "STRINGS"
chapter_timestamp = "1:09:40"
#############################
#############################

double_quotes = "can be in double quotes"
single_quotes = 'or in single quotes'

# As long as quotes match it doesn't matter

concatenated_string = double_quotes + " " + single_quotes

# You can append to a string

song_name = "Nothing"
song_name += " breaks"
song_name += " like"
song_name += " a heart"

release_year = str(2019) # just a reminder

# String can be multi-line

poem = '''Out of the night that covers me,
    Black as the pit from pole to pole,
I thank whatever gods may be
    For my unconquerable soul.

In the fell clutch of circumstance
    I have not winced nor cried aloud.
Under the bludgeonings of chance
    My head is bloody, but unbowed.
'''

# or like this

poem_part_2 = """Beyond this place of wrath and tears
    Looms but the Horror of the shade,
And yet the menace of the years
    Finds and shall find me unafraid.
"""

################################
################################
chapter_title = "STRING METHODS"
chapter_timestamp = "1:12:36"
################################
################################

scream = "no, god, please, no!".upper()
whisper = "NOBODY SHOULD KNOW THIS...".lower()
youtube_title = "typical title formatting usually looks like this".title()

scream.isupper()
whisper.islower()
youtube_title.istitle()

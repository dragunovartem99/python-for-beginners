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

# You can set variable to particular type
this_is_a_float_now = float(99) # this is called casting

# Other types
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

# Arithmetic operators
print()

9 + 9 == 18 # addition
12 - 5 == 7 # substraction
8 * 8 == 64 # multiplication
15 / 3 == 5 # division
11 % 5 == 1 # modulus (remainder)
3 ** 2 == 9 # exponent (power of)
9 // 2 == 4 # floor division

# Negative numbers
10 + -12 == -2

# Plus can be is used to concat

concatenated_by_plus = "Mario likes " + "shrooms"

# We can combine assignment and arithmetic operators
kill_count = 19
kill_count += 2 # kill_count = kill_count + 2

# As a data scientist, you would use it for inserting a title in a graph, show a message or 
# an error, or pass a statement to a funtion.

# Methods for Formatting
#  Positional formating
#  Formatted string literals
#  Template method

# We put placeholders defined by a pair of curly braces in a text. We call the string dot format method. 
# Then, we pass the desired value into the method. The method replaces the placeholders using the values in the order of appearance replace by value:
# String.Format Method
# Synxtax  : 'text{}'.format(value)


# Positional Formatting
print("Machine learning provides {} the ability to learn {}".format("systems", "automatically"))


my_string = "{} rely on {} datasets"
method = "Supervised algorithms"
condition = "labeled"
print(my_string.format(method, condition))

# Reordering Values
print("{} has a friend called {} and a sister called {}". format("Betty", "Linda", "Daisy"))
print("{2} has a friend called {0} and a sister called {1}". format("Betty", "Linda", "Daisy"))

# Name Placeholders
tool="Unsupervised algorithms"
goal="patterns"
print("{title} try to find {aim} in the dataset".format(title=tool, aim=goal))
print(type("{title} try to find {aim} in the dataset".format(title=tool, aim=goal))) # < class 'str'>

# Let's examine this code below. We have defined a dictionary with keys: tool and goal.
my_methods = {"tool": "Unsupervised algorithms", "goal": "patterns"} # dic datatype
print('{data[tool]} try to find {data[goal]} in the dataset'.format(data=my_methods))

# Format Specifier
# -----------------------
# We can also specify the format specifies inside curly braces. This defines how individual 
# values are presented. Here, we’ll use the syntax index colon specifier. One of the most common 
# format specifiers is float represented by f.
#  In the code, we specify that the value passed with the index 0 will be a float.
print("Only {0:f}% of the {1} produced worldwide is {2}!". format(0.5155675, "data", "analyzed"))

# We could also add .2f indicating that we want the float to have two decimals, as seen in the resulting output.
print("Only {0:.2f}% of the {1} produced worldwide is {2}!".format(0.5155675, "data", "analyzed"))

# Formatting datetime
# ----------------------
# Python has a module called datetime that allows us to, for example, to get the time and date for today.
from datetime import datetime
print(datetime.now()) # 2023-04-16 15:07:56.522968

# But since the format returned is very particular, you could use the format specifier such as %y-%m-%d-%h-%m to 
# adjust the format to something more familiar to us!

print("Today's date is {:%y-%m-%d %H:%M}".format(datetime.now())) # Today's date is 23-04-16 15:12

# Interactive Example
# Assign the substrings to the variables
wikipedia_article = 'absbsbsbsbsbsbbbbbbbbbbbbbbbbbbbbbbbbbbjssgsgsgsgsgshhhhhhhhhhhhhhhhhhhhhhhhhh'
dics = {
    'first_post' : wikipedia_article[3:19].lower()
    ,'second_post' : wikipedia_article[21:44].lower()
}
print("first post is {data[first_post]} and second post is : {data[second_post]}".format(data = dics))




















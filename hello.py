print("hello world")
x = 1
y = 2
# youcan aassignvariables in one line
x, y = 1, 2
# thisisthesame asabove
# python is a dynamic languaage meaning that it not neccessary to set type
# and that the variable is set t runtime
# you can use a linter called mypy to acct like a static language
# intergers and strings are immutable
print(id(x))
x = x + 2
print(id(x))
# the 2 diffenrent mem locations in the output shows int are immutable
# lists are immutable
z = [2]
print(id(z))
z.append(3)
print(id(z))
# the ids are the same so it indicates lists are mutable
# for python youcan use negative indexes too


#slicing strings
name =  "joe moe"
print (name [0])
print (name [-2])
print (name [0:4])
print (name [0:])
print (name [:4])
print (name [:])

# the escape key is \ and \n is a new line
# triples quotes results in multiple lines
# to concataneate
first = "joe"
last =  "moe"
myfull = first + " " + last
print (myfull)
# myfull = f"{first} {last}"  # later version?
print (myfull)

print( "joe" in myfull)
print( "joe" not in myfull)
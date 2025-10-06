# string indexing
'''
text = "Hello World" # countin will start 0
print(text[0])
print(text[6])
print(text[6])

'''
# Negative indexing

'''
text = "Hello World" # countin will start 0
print(text[-1])
print(text[-5])

'''
"""text = "Hello World"
print(text[:7])"""

# Stop string slicing
"""text = "Hello World"
print(text[6:])
print(text[0::3])"""

"""name = "ostad "
repeat = name * 3
print(repeat)"""

str1 = "Hello"
str2 = "World"

conbine = str1+":"+","+str2
print(conbine)

com= "".join([str1,str2]) +"!"
print(com)

comb = "{} {} !".format(str1,str2)
print(comb)

combine = "%s %s !" %(str1,str2)
print(combine)
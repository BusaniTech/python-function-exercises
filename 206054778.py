#Student name: Linda Busani
#Student no: 206054778
#Assignment 3: Python

##Problem 1

s= 'fullstackslp' 

# 'f'
print(s[0])

#'p'
print(s[11])

#'stack'
print(s[4:9])

#slp
print(s[9:12])

#'cks'
print(s[7:10])

#Bonus
print(s[::-1])

##Problem 2

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

##Problem 4

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

new_set = set(mylist)
print(new_set)

##Problem 5

age = 45
name = "Kyle"

string = "Hello my dog's name is {} and he looks {} years old".format(name,age)
print(string)

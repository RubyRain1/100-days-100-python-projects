#list comprehension

#new_list = [new_item for item in list] this is a simple format shown in example below INTEGER
#new_list = [letter for letter in name] manipulate strings by letter. STRING

#integer example
numbers = [1,2,3]
new_list = [n+1 for n in numbers] # this is a short hand to show a list looping through and adding one to each number.

# print(numbers)
# print(new_list)

#string example

name = "Ruby"

new_name = [letter.title() for letter in name] #split each letter in string into own and caps them.

# print(new_name)

# num = range(1,5)
# new_num = [n*2 for n in num] in two lines

new_num = [n*2 for n in range(1,5)] #in one line

# print(new_num)

#Conditional list comprehension!!

#new_list = [new_item for item in list if test] only executes if test is met!!

names = ['alex', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']
short_names = [name for name in names if len(name) < 5] #check for if length is less then 5 if so adds to list
upper_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(upper_names)
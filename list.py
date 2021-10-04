old_list = [1,2,3,4,5]
new_list = []

new_list = [i**2 for i in old_list]
print(new_list)

x = [i for i in range(10)]
print(x)

squares = [x**2 for x in range(10)]
print(squares)

list1 = [3,4,5]
multiplied = [i*3 for i in list1 ]
print(multiplied)

listofwords = ['this','is','a','list','of','words' ]
items = [ word[0] for word in listofwords]
print(items)
out = [x.lower() for x in ['A','B','C','D','E','F']]


new_range = [i*i for i in range (5) if i % 2 == 0]
print(new_range)

string= "hello 12345 world"
numbers = [x for x in string if x.isdigit()]
print(numbers)
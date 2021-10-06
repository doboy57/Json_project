old_list = [1, 2, 3, 4, 5]
new_list = []

new_list = [i ** 2 for i in old_list]
print(new_list)

x = [i for i in range(10)]
print(x)

squares = [x ** 2 for x in range(10)]
print(squares)

list1 = [3, 4, 5]
multiplied = [i * 3 for i in list1]
print(multiplied)

listofwords = ["this", "is", "a", "list", "of", "words"]
items = [word[0] for word in listofwords]
print(items)
out = [x.lower() for x in ["A", "B", "C", "D", "E", "F"]]


new_range = [i * i for i in range(5) if i % 2 == 0]
print(new_range)

string = "hello 12345 world"
numbers = [x for x in string if x.isalpha()]
print(numbers)

fn = open("test.txt", "r")
result = [i for i in fn if "line3" in i]
print(result)


def double(x):
    return x * 2


print(double(10))
y = [double(x) for x in range(10)]
print(y)

y = [double(x) for x in range(10) if x % 2 == 0]
print(y)

ans = [x + y for x in [10, 30, 50] for y in [20, 40, 60]]
print(ans)

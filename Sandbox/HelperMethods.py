__author__ ="adam0954"

x = 5

print(id(x))
x = 7
print(id(x))
print(type(x))
print(dir(x))
print(abs(x))
print(type(dir(x)))

test1 = [x * i for i in range(1, 100)] # list comprehension for generation of test information in arrays
for n in test1:
    print(n)


result = lambda a : a * 5 #lambda anonymous function on the fly
print(result(5))

with open('int.txt', 'w') as int_dir_functions:
    for i in dir(x):
        int_dir_functions.writelines(i)
        int_dir_functions.write('\n')


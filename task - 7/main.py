# 1
my_list = [1, 2, 5, 8]
for i in range(1, len(my_list), 2):
    print(my_list[i])

# 2

my_list = [1, 2, 5, 8, 9, 10]
result = []

for num in my_list:
    if num % 2 != 0:
        result.append(num)

print(result)

# 3

my_list = ["яблуко", "банан", "груша", "слива"]
reversed_list = []

for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])

print(reversed_list)

# 4

my_list = [1, 2, 5, 8]
average = sum(my_list) / len(my_list)
result = []

for num in my_list:
    if num < average:
        result.append(num)

print(result)

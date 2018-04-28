# Input
array_size = 1000000
file_name = './numbers/{0}.txt'.format(array_size)

numbers = open(file_name, 'r').read().split(',')
array = []
for number in numbers:
    array.append(int(number))


# Counting Sort implementation
count = [0 for i in range(array_size)]
sorted_array = [0 for i in range(len(array))]

for i in array:
    count[i] += 1

for i in range(len(count)):
    if i != (len(count)-1):
        count[i+1] += count[i] 

for i in range(len(array)):
    sorted_array[count[array[i]]-1] = array[i]
    count[array[i]] -= 1

print(sorted_array)
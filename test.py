# A small example of what this library allows you to do

from ArrayG import Arr

arr1 = Arr(0, int)

while True:
    value = input("Enter an integer value: ")
    if value == '':
        break
    else:
        arr1.add(int(value))

print("The values you entered were: ")
for i in range(arr1.size):
    print(f"Position {i}: {arr1.getValue(i)}")

deletel_pos = int(input("What position will you remove? "))
arr1.remove(deletel_pos)

print("now the array looks like this:")
for i in range(arr1.size):
    print(f"Position {i}: {arr1.getValue(i)}")
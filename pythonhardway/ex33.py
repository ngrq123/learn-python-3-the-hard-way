def while_loop(number, increment):
    i = 0
    numbers = []

    for i in range(0, number, increment):
        print("At the top i is", i)
        numbers.append(i)

        # Increment does not matter now with for-loop as i will be re-assigned at the beginning of the for-loop
        i = i + increment
        print("Numbers now:", numbers)
        print("At the bottom i is", i)

    print("The numbers: ")

    for num in numbers:
        print(num)

while_loop(3, 1)
while_loop(6, 3)
while_loop(309, 10)

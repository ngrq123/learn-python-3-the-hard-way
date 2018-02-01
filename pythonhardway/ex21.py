def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions:")

age = add(30, 5) # 35
height = subtract(78, 4) # 74
weight = multiply(90, 2) # 180
iq = divide(100, 2) # 50

print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# what = add(35, subtract(74, multiply(180, divide(50, 2))))
# what = add(35, subtract(74, multiply(180, 25.0)))
# what = add(35, subtract(74, 4500.0))
# what = add(35, -4426.0)
# what = -4391.0
# what = 35 + (74 - (180 * (50 / 2)))
# what = 35 + 74 - 180 * 50 / 2
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: {} Can you do it by hand?".format(what))

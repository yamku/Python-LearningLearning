# The 'for' Loop
colors = ['red', 'blue', 'green', 'purple']
for color in colors:
    if color == 'red':
        continue
    elif color == 'green':
        print(color)

# %----------------------------------------------------------------------------%

for color in colors:
    if color == 'red':
        continue
    elif color == 'purple':
        break
    print(color)

# %----------------------------------------------------------------------------%

list_of_points = [(1, 2), (2, 3), (3, 4)]
for x, y in list_of_points:
    print(f"x: {x}, y: {y}")

# %----------------------------------------------------------------------------%

ages = {'Kevin': 59, 'Bob': 49, 'Bijay': 21}
for name, age in ages.items():
    print(f"Person Named: {name}")
    print(f"Age of: {age}")

# %----------------------------------------------------------------------------%

points = {(1.5, 2.5, 3.5)}
for x, y, z in points:
    print(f"x: {x}, y: {y}, z: {z}")

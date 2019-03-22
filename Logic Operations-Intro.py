# ------------------------------ The 'not' Operation: ------------------------------

while True:
    name = input("Enter your name:")
    if not name:  # Returns True value if input value is empty
        print("Please enter your name!")
        continue  # returns to name for input until the condition is False or input has some value
    print(f"Hi!, {name}")  # Prints only if input has some value
    break  # Breaks the loop after printing the Name
print(f"Thank You!: {name}")

# ----------------------------- The 'or" Operation ----------------------------------
fname = input("Please enter your First Name")
lname = input("Please enter your Lastname")

if fname or lname:
    print(f"The user has a Fname: {fname} and Lname: {lname}")


# ----------------------------- The 'and" Operation ----------------------------------

if fname and lname:
    print(f"The user have fname: {fname} or lname: {lname}")
elif fname:
    print(f"FirstName: {fname}")
elif lname:
    print(f"LastName: {lname}")
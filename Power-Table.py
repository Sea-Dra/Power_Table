
print("Learn your square adn cubes!")
user_answer = "yes"

while user_answer == "yes":

    num = int(input("Enter a number: "))
    print()
    print("Number\tSquared\tCubed")
    print("======\t======\t======")

    for current_power in range(num):
        current_power += 1
        print(f"{current_power}\t\t{current_power**2}\t\t{current_power**3}")

    print()
    user_answer = input("Continue(yes/no)? ")
print("Goodbye")

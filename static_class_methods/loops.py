

def main():
    #known_people = ["John", "Anna", "Mary"]

    ask_user()
    #person = input("Enter the person you know: ")

    #if person in known_people:
    #    print("You know {}!".format(person))
    #else:
    #    print("You don't {}!".format(person))

    print([n for n in range(10) if n % 2 == 0])


def who_do_you_know():
    # Ask the user for a list of people they know
    people = input("Enter the names of people you know, separated by commas: ")
    # Split the string into a list

    #people_list = people.split(",")
    people_without_spaces = [person.strip().lower() for person in people.split(",")]

    #for person in people_list:
        # remove the blank spaces
    #    people_without_spaces.append(person.strip().lower())
    
    return people_without_spaces


def ask_user():
    # Ask user for a name
    person = input("Please, type in the name of a person:\n")

    # See if their name is in the list of people they know
    if person.lower() in who_do_you_know():
        print("You know {}.".format(person))
    else:
        print("You don't know this person.")
        # Print out that they know the person


if __name__ == "__main__":
    main()

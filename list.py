students = ['bernice', 'aaron', 'cody']

for student in students:
    print("Hello," + student.title() + "!")

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

dog = dogs[0]
dog = dogs[1]
print(dog.title())

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

dog = dogs[-1]
print(dog.title())

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

for dog in dogs:
    print(dog)

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

for dog in dogs:
    print('I like ' + dog + 's.')

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

for dog in dogs:
    print('I like' + dog + 's!\n')
    print('No, I really like' + dog + 's!\n')

print("\nThat's just how i feel about dogs.")

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

print("Results for the dog show are as follows:\n")
for index, dog in enumerate(dogs):
    place = str(index)
    print("Place: " + place + " Dog: " + dog.title())

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

print("Results for the dog show are as follows:\n")
for index, dog in enumerate(dogs):
    place = str(index + 1)
    print("Place: " + place + " Dog " + dog.title())

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

for dog in dogs:
    print(dogs)

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

print(dogs.index('australian cattle dog'))

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

print('australian cattle dog' in dogs)
print('poodle' in dogs)

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dogs.append('poodle')

for dog in dogs:
    print(dog.title() + "s are cool.")

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dogs.insert(1, 'poodle')

print(dogs)

#I think i have alread made a empty list earlier??

usernames = []

usernames.append('bernice')
usernames.append('cody')
usernames.append('aaron')

for username in usernames:
    print("Welcome, " + username.title() + '!')

print("\nThank you for being our very first user, " + usernames[0].title() + '!')
print("And a warm welcome to our newest user, " + usernames[-1].title() + '!')


students = ['bernice', 'aaron', 'cody']

students.sort()

print("Our students are currently in alphabetical order.")
for student in students:
    print(student.title())

students.sort(reverse=True)

print("Our students are now in reverse alphabetical order.")
for student in students:
    print(student.title())


students = ['bernice', 'aaron', 'cody']

print("Here is the list in alphabetical order:")
for student in sorted(students):
    print(student.title())

print("\nHere is the list in reverse alphabetical order:")
for student in sorted(students, reverse=True):
    print(student.title())

print("\nHere is the list in its original order:")
for student in students:
    print(student.title())


students = ['bernice', 'aaron', 'cody']
students.reverse()

print(students)

numbers = [1, 3, 4, 2]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers = [1, 3, 4, 2]

print(sorted(numbers))
print(numbers)


usernames = ['bernice', 'cody', 'aaron']
user_count = len(usernames)

print(user_count)


usernames = []

usernames.append('bernice')
user_count = len(usernames)

print("We have " + str(user_count) + " user!")

usernames.append('cody')
usernames.append('aaron')
user_count = len(usernames)

print("We have " + str(user_count) + " user!")

usernames = ['bernice', 'cody', 'aaron']
user_count = len(usernames)

print("This will work: " + str(user_count))


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
del dogs[0]

print(dogs)


letters = ['a', 'b', 'c', 'a', 'b', 'c']
letters.remove('a')

print(letters)

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
last_dog = dogs.pop()

print(last_dog)
print(dogs)

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
first_dog = dogs.pop(0)

print(first_dog)
print(dogs)

usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']
first_batch = usernames[0:3]

for user in first_batch:
    print(user.title())

usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']
first_batch = usernames[0:3]

for user in usernames:
    print(user.title())

usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']
middle_batch = usernames[1:4]

for user in middle_batch:
    print(user.title())

usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']

copied_usernames = usernames[:]
print("The full copied list:\n\t", copied_usernames)

del copied_usernames[0]
del copied_usernames[0]
print("\nTwo users removed from copied list:\n\t", copied_usernames)

print("\nThe original list:\n\t", usernames)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)

#Odd numbers.
for number in range(1,21,2):
    print(number)


numbers = list(range(1,1000001))

print("The list 'numbers' has " + str(len(numbers)) + " numbers in it.")

print("\nThe last ten numbers in the list are:")
for number in numbers[-10:]:
    print(number)

ages = [23, 16, 14, 28, 19, 11, 38]

youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)

print("Our youngest reader is " + str(youngest) + " years old.")
print("Our oldest reader is " + str(oldest) + " years old.")
print("Together, we have " + str(total_years) + " years worth of life experience.")

squares []

for number in range(1,11):
    new_square = number**2
    squares.append(new_square)

for square in squares:
    print(square)
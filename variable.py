first_name = 'ada'
last_name = 'lovelace'

full_name = first_name + ' ' + last_name

message = full_name.title() + ' ' + "was considered the world's first computer programmer."
print(message)

print("Hello \neveryone!")


name = ' eric '

print('-' + name.lstrip() + '-')
print('-' + name.rstrip() + '-')
print('-' + name.strip() + '-')

print(3+2)
print(3*2)
print(3-2)
print(3/2)
print(3**2)

standard_order = 2+3*4
print(standard_order)
my_order = (2+3)*4
print(my_order)

print(0.1+0.1)
print(0.1+0.2)

#This line is a comment.
print("This line is not a comment, it is code.")

#I learned how to strip whitespace from strings.
name = '\t\teric'
print("I can strip tabs from my name: " + name.strip())
# A list of desserts I like.
desserts = ['ice cream', 'chocolate', 'apple crisp', 'cookies']
favorite_dessert = 'apple crips'

for dessert in desserts:
    if favorite_dessert in dessert:
        # This dessert is my favorite, let's let everyone know!
        print("%s is my favorite dessert!" % dessert.title())
    else:
        #I like these desserts, but they are not my favorite.
        print("I like %s." % dessert)


5 == 5
3 == 5
5 == 3
5 == 5.0
'eric' == 'eric'
'Eric' == 'eric'
'Eric'.lower() == 'eric'.lower()
'5' == 5
'5' == str(5)
3 != 5
5 > 3
5 >= 3
3 < 5

dogs = ['willie', 'hootz', 'peso', 'juno']
if len(dogs) > 3:
    print("Wow, we have a lot of dogs here!")

dogs = ['willie', 'hootz', 'peso', 'juno']
if len(dogs) > 3:
    print("Okay, this is a reasonable number of dogs.")

dogs = ['willie', 'hootz', 'peso', 'monty', 'juno', 'turkey']
if len(dogs) >= 5:
    print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
    print("Wow, we have a lot of dogs here!")
else:
    print("Okay, this is a reasonable number of dogs.")

dogs = []
if len(dogs) >= 5:
    print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
    print("Wow, we have a lot of dogs here!")
else:
    print("Okay, this is a reasonable number of dogs.")

dogs = ['willie', 'hootz']
if 'willie' in dogs:
    print("Hello, Willie!")
if 'hootz' in dogs:
    print("Hello, Hootz!")
if 'peso' in dogs:
    print("Hello, Peso!")
if 'monty' in dogs:
    print("Hello, Monty!")

dogs_we_know = ['willie', 'hootz', 'peso', 'monty', 'juno', 'turkey']
dogs_present = ['willie', 'hootz']
for dog in dogs_present:
    if dog in dogs_we_know:
        print("Hello, %s!" % dog.title())

if 0:
    print("This evaluates to True.")
else:
    print("This evaluates to False.")
if 1:
    print("This evaluates to True.")
else:
    print("This evaluates to False.")
if 1253756:
    print("This evaluates to True.")
else:
    print("This evaluates to False.")
if -1:
    print("This evaluates to True.")
else:
    print("This evaluates to False.")
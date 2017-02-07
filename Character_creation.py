# This script is for character creation.
print ("Welcome to the character wizard creation!")

# Here you will select your race from the list.
race = ["human", "ork", "elf"]
print race
race = raw_input("Please choose your race: ")
print "You have choosen %r" %race

# Here you will select your gender.
gender = ["male", "female"]
print gender
gender = raw_input("Please choose your gender: ")
print "You have choosen %r" %gender

character = {'race': race, 'gender': gender}

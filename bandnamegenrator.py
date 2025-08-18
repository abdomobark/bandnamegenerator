# Print a welcome message to the user
print("Welcome to the Band Name Generator!")

# Ask the user for the name of the city they are from
city = input("Where are you from?\n")

# Ask the user for their pet's name
pet = input("What is your pet's name?\n")

# Combine the city and pet name into one band name
# The .capitalize() makes sure the first letter is uppercase
band_name = city.capitalize() + " " + pet.capitalize()

# Show the generated band name to the user
print("Your band name could be: " + band_name)

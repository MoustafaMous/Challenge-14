# A list in Python is a collection of ordered elements or values, separated by commas, 
# with an index of "zero" for the first element

# Index: 0 = "green", 1 = "blue", 2 = "red", 3 = "purple"
color_hats = ["green", "blue", "red", "purple"]


# Lists commonly hold values of the same data type or different data types
# Lists can even hold other lists

my_favorite_things = ["Chocolate", 9, ["beach", "mountains"], "breakfast_tacos"]

# Create a list of places where our class lives
print("We are a diverse group and come from everywhere...")
where_we_live = [
    "New York, NY",
    "Houston, TX",
    "Denver, CO",
    "Cleveland, OH",
    "Myrtle Beach, SC",
    "Sparta, NJ"
]
print(where_we_live)

# Print where I live using the index
print(where_we_live[0])

# Check using index()
my_city = where_we_live.index("Sparta, NJ")
print(where_we_live[my_city])
print(my_city)

# Set elements from index 2 to index 5 equal to some_of_our_places variable and print
# WHICH CITIES DO YOU THINK THIS WILL PRINT????
some_of_our_places = where_we_live[2:5]
print(some_of_our_places)

# Print every other element
every_other_city = where_we_live[::2]
print(every_other_city)

# Print the last element of the list
last_city = where_we_live[-1]


# Change a specified element within the list at the given index
where_we_live[0] = "Los Angeles, CA"
print(where_we_live)

# Add an element to the end of the list
where_we_live.append("Honolulu, HI")
print(where_we_live)

# Add an element to the end of the list
where_we_live.remove("Honolulu, HI")
print(where_we_live)

# Remove an element from the list based on the given index
cali_index = where_we_live.index("Los Angeles, CA")
where_we_live.pop(cali_index)
print(where_we_live)

# Calculate the number of elements within the list
num_cities = len(where_we_live)
print(num_cities)

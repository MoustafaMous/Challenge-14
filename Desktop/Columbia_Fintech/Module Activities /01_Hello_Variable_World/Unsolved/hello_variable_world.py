"""Hello Variable World."""

# 1. @TODO: Create a variable called `original_price`
# and assign it the value of `198.87`.
original_price = 198.87

# 2. @TODO: Create a variable called `current_price`
# and assign it the value `254.32`.
current_price = 254.32

print(original_price)

# 3. @TODO: Create a variable called `increase` and assign the
# difference between the current price and the original price
increase = current_price - original_price

print(increase)

# 4. @TODO: Divide `increase` by `original_price` and multiply that by 100.
# Then assign the results to the variable called `percent_increase`.
percent_increase = (increase / original_price) *100

# 5. @TODO: Print all of the variables.
print(f"The original price was $ {original_price}")
print(f"The price increase is : {round(increase, 2)}")
print(f"The percentage increase is: {round(percent_increase,2)}")

# Initialize a dictionary containing top traders for each month in 2021
top_traders_2021 = {
    "January": "Karen", 
    "February": "Harold", 
    "March": "Sam",
    "April": "Tom"
}

print(f"Dictionary: {top_traders_2021}")

# Initialize a dictionary
trading_pnl = {
    "title": "Trading Log",
    "03-18-2021": -224,
    "03-19-2021": 352,
    "03-20-2021": 252,
    "03-21-2021": 354,
    "03-22-2021": -544,
    "03-23-2021": -650,
    "03-24-2021": 56,
    "03-25-2021": 123,
    "03-26-2021": -43,
    "03-27-2021": 254,
    "03-28-2021": 325,
    "03-29-2021": -123,
    "03-30-2021": 47,
    "03-31-2021": 321,
    "04-01-2021": 123,
    "04-02-2021": 133,
    "04-03-2021": -151,
    "04-04-2021": 613,
    "04-05-2021": 232,
    "04-06-2021": -311,
}

# Print out dictionary
print(f"Dictionary: {trading_pnl}")

# Print out specific value of a key
print(f"04-01-2021: {trading_pnl['04-01-2021']}")

# Add a new key-value pair
trading_pnl["04-07-2021"] = 432
print(trading_pnl)

# Modify a key value
trading_pnl["04-07-2021"] = 332
print(trading_pnl)



# Access a the value of a key using the get() method
print(trading_pnl.get("04-07-2021"))

# Delete a key-value pair
del trading_pnl["04-07-2021"]
print(trading_pnl)

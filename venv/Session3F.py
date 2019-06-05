# Conditional Constructs
# Where we wish to check some Rules/constraints
total = 10
discount = 40

# Regular if/else
"""
if total >= 500:
    print("Flat 40% Off")
else:
    print("Sorry No Discounts")
"""

# Ladder if/else
if total >=100 and total < 200:
    print("Flat20% Off")
elif total >=200 and total < 500:
    print("Flat30% Off")
elif total >=500:
    print("Flat50% Off")
else:
    print("Please Add valuables of upto 100 for Discounts")

# Nested if/else
isInternetConnected = True
isGPSConnected = False

if isInternetConnected:
    print("You can browse Google Maps")
    if isGPSConnected:
        print("You can Navigate using Google Maps")
    else:
        print("To use Navigation using Google Maps enable GPS")
else:
    print("Please Connect to Internet and Try Again")

if isInternetConnected and isGPSConnected:
    print("You can browse Google Maps and Navigate")
else:
    print("Please Connect Internet/GPS and Try Again")



# Execute Same Code Snippets by taking Amazon/WhatsApp/Zomato as your use case


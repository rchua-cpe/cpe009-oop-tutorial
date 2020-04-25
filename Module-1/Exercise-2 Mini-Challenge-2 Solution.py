# This is a taxi fare computer program

# Get the total distance in km from the user
distance = float(input("Enter the total distance traveled (km): "))
# base fare 40 + additional 13.50 per km
fare = 40 + (13.50 * distance)
# Add the :2.f to signify two decimal places (just for aesthetics)
print(f"Your total fare is: {fare:.2f} php")
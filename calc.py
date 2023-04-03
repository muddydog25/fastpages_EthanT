def calculate_avg_mpg(trip_mileage, fuel_used):
    # Calculate the total mileage and fuel used
    total_mileage = sum(trip_mileage)
    total_fuel_used = sum(fuel_used)
    
    # Calculate the average MPG by dividing total mileage by total fuel used
    return total_mileage / total_fuel_used


def main():
    # Prompt the user to enter the number of entries for their trip
    num_entries = int(input("Enter the number of entries for your trip: "))

    # Initialize empty lists for trip mileage and fuel used
    trip_mileage = []
    fuel_used = []

    # Iterate through the number of entries and prompt the user to enter the distance and fuel used for each entry
    for i in range(num_entries):
        trip_mileage.append(float(input("Enter the distance in miles for entry #{}: ".format(i+1))))
        fuel_used.append(float(input("Enter the fuel amount used in gallons for entry #{}: ".format(i+1))))
    
    # Call calculate_avg_mpg() to calculate the average MPG and store the result in a variable
    average_mpg = calculate_avg_mpg(trip_mileage, fuel_used)
    
    # Display the result to the user
    print("The average MPG for your trip is: {:.2f}".format(average_mpg))


# Call the main function
main()
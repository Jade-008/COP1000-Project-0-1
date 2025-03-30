# Allowed vehicles
def main():
    AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

    print('********************************')
    print('AutoCountry Vehicle Finder v0.1')
    print('********************************')

    while True:
        print('Please Enter the following number below from the following menu:')
        print('1. Print all Authorized Vehicles')
        print('2. Exit')

        user_input = input("Enter your choice: ")

        if user_input == "1":
            print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
            for vehicle in AllowedVehiclesList:
                print(vehicle)
            print("********************************")
            print('AutoCountry Vehicle Finder v0.1')
            print('********************************')
        elif user_input == "2":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input. Please enter 1 or 2.")
if __name__ == "__main__":
        main()

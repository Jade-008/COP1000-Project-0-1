import os

FILE_PATH = 'authorized_vehicles.txt'

def load_vehicles():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w') as file:
            file.write('\n'.join([
                'Ford F-150',
                'Chevrolet Silverado',
                'Tesla CyberTruck',
                'Toyota Tundra',
                'Nissan Titan',
                'Rivian R1T',
                'Ram 1500' 
                ]))
    with open(FILE_PATH, 'r') as file:
            return [line.strip() for line in file.readlines()]
        
def save_vehicles(vehicles):
    with open(FILE_PATH, 'w') as file:
        file.write('\n'.join(vehicles))

def print_all_vehicles(allowed_vehicles_list):
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowed_vehicles_list:
        print(vehicle)

    print("********************************")
    print('AutoCountry Vehicle Finder v0.6')
    print('********************************')

def search_vehicle(allowed_vehicles_list):
    search_vehicle = input("Please Enter the full Vehicle name: ")
    if search_vehicle in allowed_vehicles_list:
         print(f"{search_vehicle} is an authorized vehicle")
    else:
         print(f"{search_vehicle} is not an authorized vehicle. Please check the spelling and try again.")

    print("********************************")
    print('AutoCountry Vehicle Finder v0.6')
    print('********************************')

def add_vehicle(allowed_vehicles_list):
    new_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
    if new_vehicle not in allowed_vehicles_list:
        allowed_vehicles_list.append(new_vehicle)
        save_vehicles(allowed_vehicles_list)
        print(f'You have added "{new_vehicle}" as an authorized vehicle.')
    else:
        print(f'"{new_vehicle}" is already in the Authorized Vehicles List.')

    print("********************************")
    print('AutoCountry Vehicle Finder v0.6')
    print('********************************')  

def delete_vehicle(allowed_vehicles_list):
    delete_vehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
    if delete_vehicle in allowed_vehicles_list:
        confirm = input(f'Are you sure you want to remove "{delete_vehicle}" from the Authorized Vehicles List? (yes/no): ')
        if confirm.lower() == 'yes':
             allowed_vehicles_list.remove(delete_vehicle)
             save_vehicles(allowed_vehicles_list)
             print(f'You have REMOVED "{delete_vehicle}" as an authorized vehicle.')
        else:
             print(f'"{delete_vehicle}" was not removed from the Authorized Vehicles List.')
    else:
         print(f"{delete_vehicle} is not in the Authorized Vehicles List.")


    print("********************************")
    print('AutoCountry Vehicle Finder v0.6')
    print('********************************') 

def main():
    AllowedVehiclesList = load_vehicles()

    print('********************************')
    print('AutoCountry Vehicle Finder v0.6')
    print('********************************')

    while True:
        print('Please Enter the following number below from the following menu:')
        print('1. Print All Authorized Vehicles')
        print('2. Search for Authorized Vehicle')
        print('3. Add Authorized Vehicle')
        print('4. Delete Authorized Vehicle')
        print('5. Exit')

        user_input = input("Enter your choice: ")

        if user_input == "1":
            print_all_vehicles(AllowedVehiclesList)
        elif user_input == "2":
            search_vehicle(AllowedVehiclesList)
        elif user_input == "3":
            add_vehicle(AllowedVehiclesList)
        elif user_input == "4":
            delete_vehicle(AllowedVehiclesList)
        elif user_input == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()

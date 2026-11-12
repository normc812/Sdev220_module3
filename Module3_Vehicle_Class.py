# Author: Norman C Blizard
# Date: 11/12/2026
# 
# file name: Module3_vehicle_Class.py
# URL: https://github.com/normc812/Module-3/tbd
#
# Description: This program creates a supercass called Vehicle which contains attributes
# for vehicle type, and a subclass called Automobile which inherits from Vehicle and adds 
# attributes for year, make, model, doors (2 or 4), roof (solid or sunroof), with error
# checking of inputs.  Note: I added "convertible" to the roof options.  
# The program will prompt the user for input and create an Automobile object with the input data.
# Program will also output data in easy to read and understandable format. 
# Program will also create a list of Automobile objects and output the data for each object in the list.
# Note: Visual Studio Code was used to create this program.  
# The program was run in the terminal using Python 3.11.6.
# Note 2: Copilot was used to assist in the creation of this program.  
# Copilot is an AI tool that can help with coding tasks, 
# but it is not perfect and may require human oversight and correction.  
# The author of this program takes full responsibility for any errors or issues 
# that may arise from the use of Copilot.

 # this is the superclass Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

 # class Automobile inherits from Vehicle class
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        
        # call the superclass constructor to initialize vehicle_type
        super().__init__(vehicle_type)   # or "car" or "truck" or "SUV" etc.
        # use setters to initialize the attributes with error checking
        self.set_year(year)
        self.set_make(make)
        self.set_model(model)
        self.set_doors(doors)
        self.set_roof(roof)

    def get_year(self):
        return self.year

    def set_year(self, year):
        # error checking for year
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if year < 1910 or year > 2027:
            raise ValueError("Year must be between 1910 and 2027")
        self.year = year

    def get_make(self):
        return self.make

    def set_make(self, make):
        # error checking for make
        if not isinstance(make, str):
            raise TypeError("Make must be a string")
        if not make:
            raise ValueError("Make cannot be empty")
        self.make = make

    def get_model(self):
        return self.model

    def set_model(self, model):
        # error checking for model
        if not isinstance(model, str):
            raise TypeError("Model must be a string")
        if not model:
            raise ValueError("Model cannot be empty")
        self.model = model

    def get_doors(self):
        return self.doors

    def set_doors(self, doors):
        if doors in [2, 4]:
            self.doors = doors
        else:
            raise ValueError("Doors must be 2 or 4")

    def get_roof(self):
        return self.roof

    def set_roof(self, roof):
        if roof in ["solid", "convertible", "sunroof"]:
            self.roof = roof
        else:
            raise ValueError("Roof must be 'solid' or 'sunroof'")
            
    def display_info(self):
        print("\nVehicle information:")
        print ("_" * 35)
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Year:         {self.get_year()}")
        print(f"Make:         {self.get_make()}")
        print(f"Model:        {self.get_model()}")
        print(f"Doors:        {self.get_doors()}")
        print(f"Roof:         {self.get_roof()}")

# main calling program
def main():
    print("Welcome to the Vehicle Information Program!")
    print("Enter the details for your vehicle below.\n" )
    
    automobiles = []  # initialize an empty list to store Automobile objects

    while True:
        # Validate vehicle type.
        while True:
            vehicle_type = input("Enter vehicle type (car, truck, SUV, etc.): ").strip()
            # method .strip removes leading and trailing whitespace from the input string
            
            if vehicle_type:
                break

            print("Vehicle type cannot be blank. Please try again.")

        # Validate year using the setter's rules.
        while True:
            try:
                year = int(input("Enter year: "))
                if year < 1910 or year > 2027:
                    raise ValueError
                break
            except ValueError:
                print("Year must be an integer between 1910 and 2027. Please try again.")

        # Validate make.
        while True:
            make = input("Enter make: ").strip()
            if make:
                break
            print("Make cannot be blank. Please try again.")

        # Validate model.
        while True:
            model = input("Enter model: ").strip()
            if model:
                break
            print("Model cannot be blank. Please try again.")

        # Validate doors.
        while True:
            try:
                doors = int(input("Enter number of doors (2 or 4): "))
                if doors not in [2, 4]:
                    raise ValueError
                break
            except ValueError:
                print("Doors must be 2 or 4. Please try again.")

        # Validate roof.
        while True:
            roof = input("Enter roof type (solid, convertible or sunroof): ").strip().lower()

            if roof in ["solid", "convertible", "sunroof"]:
                break

            print("Roof must be 'solid', 'convertible', or 'sunroof'. Please try again.")

        # Create an Automobile object and add it to the list of automobiles.
        automobile = Automobile(vehicle_type, year, make, model, doors, roof)                              
        automobiles.append(automobile)

        print("\nVehicle added successfully!")

        # Ask whether to enter another automobile.
        while True:
            another = input("Would you like to add another vehicle? (y/n): ").strip().lower()

            if another in ["y", "yes", "n", "no"]:
                break

            print("Please enter 'y' or 'n'.")

        if another in ["n", "no"]:
            break

        print()
# done with input loop, now display the list of Automobile objects
    # Display each Automobile object in the list.
    print("\n" + "=" * 40)
    print(f"VEHICLE SUMMARY — {len(automobiles)} vehicle(s)")
    print("=" * 40)

    for number, automobile in enumerate(automobiles, start=1):
        print(f"\nVehicle #{number}")
        automobile.display_info()

    print("\nThank you for using the Vehicle Information Program!")


if __name__ == "__main__":
    main()    
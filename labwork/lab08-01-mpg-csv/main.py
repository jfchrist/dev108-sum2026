## Starting file for Exercise 7.1
import csv

#create filename for .csv file
filename = "trips.csv"

#create file record of mpg trips
def write_trips(trip):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(trip)

def read_trips():
    trips = []
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            trips.append(row)
    return trips

def list_trips(trips):
    print("Distance\tGallons\t\tMPG")
    for i in range(0,len(trips)):
        trip = trips[i]
        print(str(trip[0])+"\t\t"+str(trip[1])+"\t\t"+str(trip[2]))


def get_miles_driven():
    while True:
        miles_driven = float(input("\nEnter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
        
def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    trips = read_trips()
    list_trips(trips)

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()

        #create list of values for these calculations
        trip = []
        trip.append(miles_driven)
        trip.append(gallons_used)
        trip.append(mpg)
        #add list to bigger list
        trips.append(trip)

        write_trips(trip)

        list_trips(trips)
        
        more = input("\nMore entries? (y or n): ")

    

    print("Bye")

if __name__ == "__main__":
    main()


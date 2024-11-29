import os
from booking import RailwayBooking

def main():
    booking_system = RailwayBooking()
    if not booking_system.db.is_connected():
        print("Unable to establish a database connection. Exiting the application.")
        return

    print("Welcome to the Railway Seat Booking System!\n")
    while True:
        print("Enter:")
        print("  1. To enquire about train details.")
        print("  2. To book a seat.")
        print("  3. To check your booking details.")
        print("-------------------------------------------------------")
        choice = int(input("Please Enter your choice: "))
        print("***********************************************\n")
        if choice == 1:
            booking_system.show_trains()
        elif choice == 2:
            passenger_name = input("Enter your name: ")
            train_number = input("Enter train number: ")
            booking_system.book_seat(passenger_name, train_number)
        elif choice == 3:
            passenger_name = input("Enter your name: ")
            booking_system.show_booking_details(passenger_name)
        
        ch = input("Do you want to continue? y/n: ")
        if ch.lower() != 'y':
            print("Thank you for using the Railway Seat Booking System!")
            break
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()

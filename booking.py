# booking.py
from database import Database

class RailwayBooking:
    def __init__(self):
        self.db = Database()

    def show_trains(self):
        query = "SELECT * FROM train_details"
        trains = self.db.fetch_all(query)
        for train in trains:
            print(f"Train Number: {train[0]}, Train Name: {train[1]}")

    def book_seat(self, passenger_name, train_number):
        query = "SELECT seats_available FROM train_details WHERE train_number = %s"
        seats = self.db.fetch_all(query, (train_number,))
        if seats and seats[0][0] > 0:
            new_seat_count = seats[0][0] - 1
            update_query = "UPDATE train_details SET seats_available = %s WHERE train_number = %s"
            self.db.execute_query(update_query, (new_seat_count, train_number))
            insert_query = "INSERT INTO bookings (passenger_name, train_number) VALUES (%s, %s)"
            self.db.execute_query(insert_query, (passenger_name, train_number))
            print("Seat booked successfully!")
        else:
            print("No available seats.")

    def show_booking_details(self, passenger_name):
        query = "SELECT * FROM bookings WHERE passenger_name = %s"
        bookings = self.db.fetch_all(query, (passenger_name,))
        if bookings:
            for booking in bookings:
                print(f"Passenger Name: {booking[0]}, Train Number: {booking[1]}")
        else:
            print("No bookings found for this passenger.")

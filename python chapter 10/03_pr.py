class Train:
    def __init__(self, train_number, total_seats, base_fare):
        self.train_number = train_number
        self.total_seats = total_seats
        self.booked_seats = 0
        self.base_fare = base_fare
    
    def book_ticket(self, number_of_tickets):
        if number_of_tickets <= 0:
            return "Number of tickets should be greater than zero."
        if self.booked_seats + number_of_tickets > self.total_seats:
            return "Not enough seats available."
        self.booked_seats += number_of_tickets
        return f"{number_of_tickets} ticket(s) successfully booked."

    def get_status(self):
        available_seats = self.total_seats - self.booked_seats
        return f"Total seats: {self.total_seats}, Booked seats: {self.booked_seats}, Available seats: {available_seats}"
    
    def get_fare_information(self):
        return f"Base fare per ticket: {self.base_fare} INR"

# Example usage:
train = Train(train_number=12345, total_seats=100, base_fare=500)
print(train.get_status())  # Total seats: 100, Booked seats: 0, Available seats: 100
print(train.book_ticket(5))  # 5 ticket(s) successfully booked.
print(train.get_status())  # Total seats: 100, Booked seats: 5, Available seats: 95
print(train.get_fare_information())  # Base fare per ticket: 500 INR
print(train.book_ticket(200))  # Not enough seats available.

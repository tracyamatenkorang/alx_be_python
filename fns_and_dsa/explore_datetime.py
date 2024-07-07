from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current Date and Time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future Date: {future_date.strftime('%Y-%m-%d')}")

display_current_datetime()
calculate_future_date()
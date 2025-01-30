import calendar

def print_calendar(year):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar()

    # Print the calendar for each month
    for month in range(1, 13):
        print(cal.formatmonth(year, month))

if __name__ == "__main__":
    print_calendar(2025)
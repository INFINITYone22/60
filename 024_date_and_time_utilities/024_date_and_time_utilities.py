import datetime

def date_and_time_utilities():
    now = datetime.datetime.now()
    print("Current date and time:", now)

    today = datetime.date.today()
    print("Today's date:", today)

    yesterday = today - datetime.timedelta(days=1)
    print("Yesterday's date:", yesterday)

    tomorrow = today + datetime.timedelta(days=1)
    print("Tomorrow's date:", tomorrow)

    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    print("Your age:", age)

date_and_time_utilities()

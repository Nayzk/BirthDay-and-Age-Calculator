
from datetime import datetime, date

print("Seperate your date of birth with comma like (yyyy, mm, dd)")
birth_date = datetime.strptime(input("Enter your birthdate : "), "%Y, %m, %d")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(birth_date)

print(age)
































from datetime import datetime, date
f_date = datetime.strptime(input("Enter date : " ), "%Y, %m, %d")
l_date = datetime.strptime(input("Enter date : " ), "%Y, %m, %d")
delta = l_date - f_date
print(delta.days)





































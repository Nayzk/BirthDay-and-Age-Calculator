from datetime import datetime

def get_user_bday():
    year = int(input('Enter your year of birth [YY] :  '))
    month = int(input('Enter your month of birth [MM] : '))
    day = int(input('Enter your day of birth [DD] : '))

    birthday = datetime(2000+year,month,day)
    return birthday

def dates(original_date, now):
    delta1 = datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime(now.year+1, original_date.month, original_date.day)
    
    return ((delta1 if delta1 > now else delta2) - now).days




def main():
    bd = get_user_bday()
    td = datetime.now()
    c = dates(bd, td)
    print(c)

if __name__ == '__main__':
    main()

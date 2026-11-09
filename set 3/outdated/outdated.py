mon=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        s= input('Enter Date:')
        if '/' in s:
            month,day,year=s.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
            if month<=12 and day<=31: 
                print(f'{year:02}-{month:02}-{day:02}')
                break
                
        else:
            month,day,year=s.split(' ')
            if day.endswith(','):
                 day=day.replace(',','')
                 day = int(day)
                 year = int(year)
                 if month in mon:                
                    month=mon.index(month)+1
                    if month<=12 and day<=31:
                        print(f'{year:02}-{month:02}-{day:02}')
                        break

    except ValueError:
        pass
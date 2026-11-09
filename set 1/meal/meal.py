def main():
    time=input('what time is it? ')
    d=convert(time)
    if 7<=d<=8:
        print('breakfast time')
    elif 12<=d<=13:
        print('lunch time')
    elif 18<=d<=19:
        print('dinner time')


def convert(time):
    hours, minutes = time.split(":")
    d=float(hours)+ float (minutes)/60
   
    return d


if __name__ == "__main__":
    main()
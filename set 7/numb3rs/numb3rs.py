import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
   
   if re.search(r'^[\d]+\.[\d]+\.[\d]+\.[\d]+$',ip):
        lis=ip.split('.')
        for num in lis: 
            if len(num) > 1 and num[0] == '0':
                return False     
        for num in lis:
            if int(num)<0 or int(num)>255:
                return False
        return True

   else:
        return False

if __name__ == "__main__":
    main()
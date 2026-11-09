import sys
import csv
from tabulate import tabulate

if len(sys.argv)>2:
    sys.exit('too many args')
elif len(sys.argv)<2:
    sys.exit('too few args')
else:
    if sys.argv[1].endswith('.csv'):
        try:
         with open (sys.argv[1],'r') as file:
            reader=csv.DictReader(file)
           
            print(tabulate(reader,headers='keys',tablefmt='grid'))
        except FileNotFoundError:
                sys.exit("File does not exist")
    else:
        sys.exit("Not a csv file")
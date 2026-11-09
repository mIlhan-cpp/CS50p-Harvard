import sys
import csv

if len(sys.argv)>3:
    sys.exit('too many args')
elif len(sys.argv)<3:
    sys.exit('too few args')
else:
    if sys.argv[1].endswith('.csv') and sys.argv[2].endswith('.csv'):
            try:
             with open (sys.argv[1],'r') as file:
                reader=csv.DictReader(file)
                with open(sys.argv[2],'w') as file:
                    writer=csv.DictWriter(file,fieldnames=["first","last",'house'])
                    writer.writeheader()
                    for line in reader:
                        name=line['name']
                        first,last=name.split(', ')
                        house=line['house']
                        student={'last':last,'first':first,'house':house}
                        writer.writerow({'first':last,'last':first,'house':house})
            except FileNotFoundError:
                    sys.exit("File does not exist")
    else:
        sys.exit("Not a csv file")

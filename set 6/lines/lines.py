import sys

if len(sys.argv)>2:
    sys.exit('too many args')
elif len(sys.argv)<2:
    sys.exit('too few args')

else:
    if sys.argv[1].endswith('.py'):
        try:
            count=0
            with open(sys.argv[1]) as file:
                for line in file:
                    if line.lstrip().startswith('#') or line.strip()=="":
                        continue
                    else:
                        
                        count+=1
            print(count)            
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a python file")
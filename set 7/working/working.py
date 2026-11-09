import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
        match=re.search(r'([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM)',s)
        if match:
            if int(match.group(1)) > 12 or int(match.group(4)) > 12:
                            raise ValueError
            
                        
            if match.group(3)=='AM':
                starthour=int(match.group(1))
                if starthour==12:
                      starthour=0
            elif match.group(3)=='PM':
                starthour=int(match.group(1))+12
                if starthour==24:
                    starthour=12
            startmin=match.group(2)
            if startmin is None:
                startmin=0
            else:
                  startmin=int(match.group(2))
            startzone=match.group(3)
            
           
            if match.group(6)=='AM':
                endhour=int(match.group(4))
                if endhour==12:
                      endhour=0
            elif match.group(6)=='PM':
                endhour=int(match.group(4))+12
                if endhour==24:
                    endhour=12
            endmin=match.group(5)
            if endmin is None:
                endmin= 0
            else:
                  endmin=int(match.group(5))
            if startmin > 59 or endmin > 59:
                                        raise ValueError
            endzone=match.group(6)
            
         
   
            return f"{starthour:02}:{startmin:02} to {endhour:02}:{endmin:02}"     
        else:
            raise ValueError


if __name__ == "__main__":
    main()
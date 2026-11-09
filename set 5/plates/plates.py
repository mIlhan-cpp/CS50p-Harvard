def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
        num=False
        if len(s)>6 or len(s)<2:
            return False
        elif not s[0].isalpha() or not s[1].isalpha():
             return False
             
        for a in s:
            if not a.isalnum():
                 return False
            if not num and a=='0':
                 return False
            if a.isdigit():
                 num=True
            if num and a.isalpha():
                 return False
           
        return True
if __name__ == "__main__":
    main()
                 
                      
            

            




from pyfiglet import Figlet

figlet = Figlet()
import sys

if  len(sys.argv)==1:
    x=input('Input:')
    print(figlet.renderText(x))
elif len(sys.argv)==3:
        if sys.argv[1]=='-f'or sys.argv[1]=='--font':
           
            if sys.argv[2] in figlet.getFonts():
                x=input('Input:')
                figlet.setFont(font=sys.argv[2])
                print(figlet.renderText(x))
            else:
                 sys.exit('Invalid usage')
        else:
             sys.exit('Invalid usage')
else:
     sys.exit('Invalid usage')
from pyfiglet import Figlet
import sys
inputtext=input()
f=Figlet(font='slant')
if sys.argv !=2:
    print(f.renderText(inputtext))

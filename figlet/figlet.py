from pyfiglet import Figlet
import sys,random
def main():
    figlet = Figlet()submit50 cs50/problems/2022/python/figlet
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f","--font"):
        font = sys.argv[2]
        if font not in figlet.getFonts():
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))
main()

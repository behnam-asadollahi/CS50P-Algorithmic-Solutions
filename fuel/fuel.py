def main():
    Fraction = input("Fraction: ")
    while Fraction is None:
        Fraction = input("Fraction: ")
    Fraction = split(Fraction)
    while Fraction is None:
        Fraction = input("Fraction: ")
        Fraction = split(Fraction)
    judge(Fraction)

def split(n):
    try:
        x, y = n.split(sep="/")
        x = int(x)
        y = int(y)
        if x > y or y == 0 or x < 0 :
            raise ValueError
        return round(x / y *100)
    except (ZeroDivisionError, ValueError)  :
        return None

def judge(m):
    if m >= 99:
        print("F")
    elif 1 >= m:
        print("E")
    else:
        print(f"{m}%")
main()

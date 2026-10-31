def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    while True:
        date = input("Date: ").strip()
        try:
            if "/" in date:
                M,D,Y = date.split("/")
                M = int(M)
                D = int(D)
                Y = int(Y)
            else:
                if "," not in date:
                    raise ValueError
                M,D,Y = date.split(" ")
                D = D.replace(",","")
                M = months.index(M) + 1
                D = int(D)
                Y = int(Y)
            if 1 <= M <= 12 and 1 <= D <= 31:
                print(f"{Y:04}-{M:02}-{D:02}")
                break
        except (ValueError,IndexError):
            pass
main()


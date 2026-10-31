def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
def convert(time):
    if "a.m." in time or "p.m." in time:
        time, period = time.split(" ")
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
        if period == "p.m." and hours != 12:
            hours += 12
        elif period == "a.m." and hours == 12:
            hours = 0
    else:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
    return hours + minutes / 60
if __name__ == "__main__":
    main()

def convert(mass):
    Energy = (mass*90000000000000000)
    return Energy

def main():
    mass = int(input("m: "))
    Energy = convert(mass)
    print(Energy)

main()


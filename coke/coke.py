def main():
    due = 50
    while due > 0:
        print(f"Amount Due: {due}")
        amount = int(input("Insert coin: "))
        if amount in [25, 10, 5]:
            due -= amount
    print(f"Change Owed: {abs(due)}")
main()

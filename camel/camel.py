def main():
    case = input("camelCase: ")
    snake = ""
    for letter in case:
        if letter.isupper():
            snake += "_" + letter.lower()
        else:
            snake += letter
    print(snake)

main()

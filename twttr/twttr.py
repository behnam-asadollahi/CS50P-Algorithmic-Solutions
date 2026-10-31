def main():
    full = input("Input: ").strip()
    short = ""
    for letter in full:
        if letter.lower() not in "aeiou":
            short += letter
    print(f"Output: {short}")

main()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")S
def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    if not s[0:2].isalpha():
        return False
    number_started = False
    for character in s[2:]:
        if character.isdigit():
            if not number_started and character == "0":
                return False
            number_started = True
        elif number_started:
            return False
    return True
main()

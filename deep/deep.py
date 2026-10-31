def main():
    deep = input("What is the Answer to the Greatest Question of Life, the Universe, and Everything? ").strip().lower()
    if deep in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")
main()

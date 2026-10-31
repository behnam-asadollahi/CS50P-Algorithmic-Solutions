def main():
    grocery = {}
    while True:
        try:
            Item = input().upper()
            if Item in grocery:
                grocery[Item] += 1
            else:
                grocery[Item] = 1
        except EOFError:
            for Item in sorted(grocery):
                print(grocery[Item],Item)
            break
main()

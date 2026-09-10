import sys


def main() -> None:
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file ’{sys.argv[1]}’")
        try:
            f = open(sys.argv[1], "r")
            print(f"---\n\n{f.read()}\n---")
            f.close()
            print(f"File ’{sys.argv[1]}’ closed.")
        except FileNotFoundError as e:
            print(f"Error opening file '{sys.argv[1]}': ", e)
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': ", e)
    else:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()

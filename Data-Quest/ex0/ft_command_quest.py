import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    len_argv = len(sys.argv)
    if len_argv != 1:
        print("Arguments received: ", len_argv - 1)
        count = 1
        for i in sys.argv[1:]:
            print(f"Argument {count}: ", i)
            count += 1
    else:
        print("No arguments provided!")
    print("Total arguments: ", len(sys.argv))


if __name__ == "__main__":
    main()

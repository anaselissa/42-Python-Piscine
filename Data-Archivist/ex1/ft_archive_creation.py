import sys


def main() -> None:
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file ’{sys.argv[1]}’")
        try:
            f = open(sys.argv[1], "r")
            f_read = f.read()
            print(f"---\n\n{f_read}\n---")
            f.close()
            print(f"File ’{sys.argv[1]}’ closed.\n")
            print("Transform data: \n---\n")
            new = f_read.split("\n")
            new_str = ""
            for line in new:
                new_str = new_str + line + "#\n"
            print(new_str)
            print("---")
            file_name = input("Enter new file name (or empty):")
            if not file_name:
                print("Not saving data.")
            else:
                new_file = open(file_name, "w")
                print(f"Saving data to ’{file_name}’")

                new_file.write(new_str)
                new_file.close()
                print(f"Data saved in file ’{file_name}’.")
        except FileNotFoundError as e:
            print(f"Error opening file '{sys.argv[1]}': ", e)
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': ", e)
    else:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()

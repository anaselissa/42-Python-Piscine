def secure_archive(file_name: str, read_write: str = "r",
                   content_to_write: str = "Hi 42") -> tuple[bool, str]:
    try:
        bool_status = True
        if read_write == "r":
            with open(file_name, read_write) as file:
                ret_txt = file.read()
        elif read_write == "w":
            with open(file_name, "w") as file:
                file.write(content_to_write)
                ret_txt = "Content successfully written to file"
        else:
            ret_txt = "invalid input (enter w or r )"
            bool_status = False
    except (PermissionError, FileNotFoundError) as e:
        ret_txt = e.__str__()
        bool_status = False

    return ((bool_status, ret_txt))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("Using ’secure_archive’ to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))

    print("Using ’secure_archive’ to read from a nonexistent file:")
    print(secure_archive("/etc/shadow", "r"))

    print("Using ’secure_archive’ to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "r"))

    print("Using ’secure_archive’ to write previous content to a new file:")
    print(secure_archive("new_file", "w", "Hi 42"))

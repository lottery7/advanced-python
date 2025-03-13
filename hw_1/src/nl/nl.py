import os
import sys

FORMAT = "{:6}  {}"


def enumerate_stdin() -> None:
    line_num = 1
    try:
        while line := input():
            print(FORMAT.format(line_num, line))
            line_num += 1
    except EOFError:
        pass


def enumerate_file(file_path: str) -> None:
    if not os.path.exists(file_path):
        raise ValueError(f"File {file_path} doesn't exist")

    with open(file_path) as input_file:
        for i, line in enumerate(input_file, start=1):
            print(FORMAT.format(i, line), end="")


if __name__ == "__main__":
    match (len(sys.argv)):
        case 1:
            enumerate_stdin()
        case 2:
            enumerate_file(sys.argv[1])
        case _:
            raise ValueError("Invalid args")

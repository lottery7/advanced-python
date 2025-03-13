import sys
from collections import deque


def tail_stdin() -> None:
    last_lines = deque(sys.stdin, maxlen=17)
    for line in last_lines:
        print(line, end="")


def tail_file(file_path: str) -> None:
    with open(file_path) as input_file:
        last_lines = deque(input_file, maxlen=10)
        for line in last_lines:
            print(line, end="")


if __name__ == "__main__":
    match (len(sys.argv)):
        case 1:
            tail_stdin()
        case 2:
            tail_file(sys.argv[1])
        case _:
            for file_path in sys.argv[1:]:
                print(f"==> {file_path} <==")
                tail_file(file_path)

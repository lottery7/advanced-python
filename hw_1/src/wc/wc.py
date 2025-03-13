import sys
from functools import reduce


def wc_stdin() -> tuple[int, int, int]:
    lines_count = words_count = bytes_count = 0
    for line in sys.stdin:
        lines_count += 1
        words_count += len(line.split())
        bytes_count += len(line.encode())
    return lines_count, words_count, bytes_count


def wc_file(file_path: str) -> tuple[int, int, int]:
    lines_count = words_count = bytes_count = 0
    with open(file_path, "rb") as f:
        for line in f:
            lines_count += 1
            words_count += len(line.split())
            bytes_count += len(line)
    return lines_count, words_count, bytes_count, file_path


if __name__ == "__main__":
    match len(sys.argv):
        case 1:
            print("{:8}{:8}{:8}".format(*wc_stdin()))
        case 2:
            print("{:8}{:8}{:8} {}".format(*wc_file(sys.argv[1])))
        case _:
            counts = [wc_file(file_path) for file_path in sys.argv[1:]]
            for c in counts:
                print("{:8}{:8}{:8} {}".format(*c))

            total_lines, total_words, total_bytes = reduce(
                lambda l, r: (l[0] + r[0], l[1] + r[1], l[2] + r[2]),
                counts,
                (0, 0, 0),
            )

            print(f"{total_lines:8}{total_words:8}{total_bytes:8} total")

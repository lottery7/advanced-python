# 1. Запуск без аргументов:

```
poetry run python src/tail/tail.py
```

Пример ввода:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```

Пример вывода:

```
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```

# 2. Запуск с одним аргументом

```
poetry run python src/tail/tail.py src/tail/tail.py
```

Вывод:

```
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
```

# 3. Запуск с более, чем одним аргументом:

```
poetry run python src/tail/tail.py src/tail/tail.py src/nl/nl.py
```

Вывод:

```
==> src/tail/tail.py <==
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
==> src/nl/nl.py <==


if __name__ == "__main__":
    match (len(sys.argv)):
        case 1:
            enumerate_stdin()
        case 2:
            enumerate_file(sys.argv[1])
        case _:
            raise ValueError("Invalid args")
```

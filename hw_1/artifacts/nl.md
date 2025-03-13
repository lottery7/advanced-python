# 1. Запуск без аргументов:

```
poetry run python src/nl/nl.py
```

Пример ввода-вывода:

```
Hello
     1  Hello
World
     2  World
```

# 2. Запуск с одним аргументом

```
poetry run python src/nl/nl.py src/nl/nl.py
```

Вывод:

```
     1  import os
     2  import sys
     3  
     4  FORMAT = "{:6}  {}"
     5  
     6  
     7  def enumerate_stdin() -> None:
     8      line_num = 1
     9      try:
    10          while line := input():
    11              print(FORMAT.format(line_num, line))
    12              line_num += 1
    13      except EOFError:
    14          pass
    15  
    16  
    17  def enumerate_file(file_path: str) -> None:
    18      if not os.path.exists(file_path):
    19          raise ValueError(f"File {file_path} doesn't exist")
    20  
    21      with open(file_path) as input_file:
    22          for i, line in enumerate(input_file, start=1):
    23              print(FORMAT.format(i, line), end="")
    24  
    25  
    26  if __name__ == "__main__":
    27      match (len(sys.argv)):
    28          case 1:
    29              enumerate_stdin()
    30          case 2:
    31              enumerate_file(sys.argv[1])
    32          case _:
    33              raise ValueError("Invalid args")
```


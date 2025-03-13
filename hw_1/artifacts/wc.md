# 1. Запуск без аргументов:

```
poetry run python src/wc/wc.py
```

Пример ввода:

```
Hello, world!
```

Пример вывода:

```
       1       2      14
```

# 2. Запуск с одним аргументом

```
poetry run python src/wc/wc.py src/wc/wc.py
```

Вывод:

```
      41     125    1336 src/wc/wc.py
```

# 3. Запуск с более, чем одним аргументом:

```
poetry run python src/wc/wc.py src/wc/wc.py pyproject.toml README.md
```

Вывод:

```
      41     125    1336 src/wc/wc.py
      23      60     464 pyproject.toml
       0       0       0 README.md
      64     185    1800 total
```

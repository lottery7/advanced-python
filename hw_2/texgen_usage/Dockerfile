FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-latex-base texlive-fonts-recommended texlive-latex-extra \
    texlive-xetex texlive-lang-cyrillic ghostscript \
    python3-pip python3-venv pipx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pipx install poetry && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --only main

COPY res ./res
COPY src ./src

CMD ["poetry", "run", "python", "src/app/main.py"]

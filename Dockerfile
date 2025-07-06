FROM python:3.9.23-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /lepidex_backend

COPY pyproject.toml uv.lock ./

RUN uv lock && uv sync

COPY . .

EXPOSE 8000

CMD ["uv", "run", "main.py"]

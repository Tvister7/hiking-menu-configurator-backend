FROM python:3.11-slim-bullseye

ENV PYTHONPATH /app/src/
ENV PATH /app/src/:$PATH
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.3.2

WORKDIR /app

RUN pip3 install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml ./
RUN poetry install --only main --no-root

COPY . /app

EXPOSE 8000

ENTRYPOINT []

CMD []

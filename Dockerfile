FROM python:3.11
ENV PYTHONUNBUFFERED=1
RUN pip install poetry
WORKDIR /code/
COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false && poetry install
COPY . /code/
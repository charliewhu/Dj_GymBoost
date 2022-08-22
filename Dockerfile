# Pull base image
FROM python:3.10

# update and install curl
RUN apt-get update && apt-get install -y curl

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install Poetry
ENV POETRY_VERSION=1.1.13
RUN curl -sSL https://install.python-poetry.org | python3 - --version "$POETRY_VERSION"

# add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set work directory
WORKDIR /code

# Install dependencies
COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.in-project true --local
RUN poetry install --no-dev

# Copy project
COPY . /code/

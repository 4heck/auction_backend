FROM python:3.7.5

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -yq install binutils libproj-dev gdal-bin

WORKDIR /app
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip poetry==1.0.5

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry config virtualenvs.create false && poetry install
COPY . .
RUN chmod +x deploy/wait-for-it.sh

CMD poetry run python src/manage.py migrate && \
    poetry run uwsgi --ini deploy/python/uwsgi.ini

RUN poetry run python src/manage.py collectstatic
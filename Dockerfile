FROM python:3.9.15-alpine


ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  CRYPTOGRAPHY_DONT_BUILD_RUST=1 \
  # poetry:
  POETRY_VERSION=1.1.12

WORKDIR /app
EXPOSE 8000
RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev git\
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi\
  # Lock cryptography version
  && pip install --no-cache-dir cryptography==3.4.8 \
  # Translations dependencies
  && apk add gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add postgresql-client \
  && pip install "poetry==$POETRY_VERSION"
# Requirements are installed here to ensure they will be cached.
COPY ./poetry.lock ./pyproject.toml ./

RUN  poetry config virtualenvs.create false \
  && poetry install $(test "$DJANGO_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . .

ARG VERSION
RUN echo $VERSION >> .version

CMD ["./start"]

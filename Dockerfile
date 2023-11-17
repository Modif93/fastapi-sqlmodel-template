FROM python:3.11-bullseye

ENV PYTHONUNBUFFERED=1
ENV HOST=0.0.0.0
ENV PORT=8000
ENV WORKERS=4

WORKDIR /code
COPY . /code/

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

CMD gunicorn webapp.main:app --workers ${WORKERS} --worker-class uvicorn.workers.UvicornWorker --bind ${HOST}:${PORT} --log-config log.ini

FROM python:3.10.6 as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ShareAndPark/requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

FROM python:3.10.6

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir "$APP_HOME"
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME


RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
#  --chown=app:app
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*


#COPY entrypoint.sh .
#
#RUN chmod +x $APP_HOME/entrypoint.sh
#RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh

# copy project
COPY ShareAndPark/entrypoint.sh .
RUN chmod +x $APP_HOME/entrypoint.sh
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh

# copy project
COPY ./ShareAndPark $APP_HOME
ENTRYPOINT ["bash", "/home/app/web/entrypoint.sh"]
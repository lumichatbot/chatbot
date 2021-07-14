FROM rasa/rasa:latest-full

USER root

COPY . /app/

WORKDIR /app/nlu-engine

RUN rasa train
ENTRYPOINT ["rasa", "run", "--enable-api", "--debug"]

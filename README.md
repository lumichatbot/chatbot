# Lumi Chatbot NLU

This project is part of the Lumi Chatbot initiative.
Natural Language Understanding (NLU) module and chatbot interface.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project consideres only Unix based OSes, running **Python 3.7.6** as the default Python version.
A different version of Python might cause the requirements installation to fail.
The rest of these instructions will consider the use of `Linux Ubuntu 16.04`.
Follow the steps below to install the required packages to run the project.

1. Install Pip, Venv and Git

```
sudo apt-get update && sudo apt-get install -y python3-pip python3-venv git
```

2. Install Poetry

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Installing

Please follow the step by step series of instructions below to get the development environment ready.

1. Clone repository

```
git clone git@github.com:lumichatbot/chatbot.git lumi-chatbot
```

2.  Install project dependencies

```
cd lumi-chatbot
poetry install
```

2.  Activate project virtual environment

```
poetry shell
```

### Training

The project comes with an initial training dataset for the demo, but after cloning the repo, you must train the model before running it.

```
cd nlu-engine
rasa train
```

### Running

After installing and training the NLU model, use the command below to expose a Rest API for the frontend.

```
cd nlu-engine
rasa run --enable-api --debug
```

To access the NLU parse API you can use the command below.

```
curl -XPOST localhost:5005/model/parse -d '{ "text": "Hey Lumi, please block traffic for all students." }'
```

Alternatively, you can run the command below to test the trained NLU model locally

```
cd nlu-engine
rasa shell
```

## Deployment

The steps below describe how to easily run a deployment environment of the NIKSUN NLU Demo using [Docker](https://www.docker.com). The Docker container created automatically trains a new version of the model and runs it.

1. Install [Docker](https://docs.docker.com/engine/install/ubuntu/).

-   Alternatively, you may run the **install.sh** script in the project root.

2. Build docker container from image.

```
cd lumi-chatbot
docker build -t "lumi-chatbot" .
```

3. Run docker container (and remove any old versions running).

```
cd lumi-chatbot
docker ps -a -q --filter "name=lumi-chatbot" | grep -q . && docker stop lumi-chatbot && docker rm -fv lumi-chatbot
docker run --name "lumi-chatbot" -d -p 5005:5005 --restart unless-stopped "lumi-chatbot"
```

4. Check logs to see if its running properly.

```
docker logs lumi-chatbot --follow
```

## Built With

-   [RASA](https://rasa.com) - The NLU framework used
-   [Poetry](https://python-poetry.org) - Python Dependency Management
-   [Docker](https://www.docker.com) - Used for deployment

## Authors

-   **Arthur Jacobs** - _Initial work_ - [asjacobs92](https://github.com/asjacobs92)


## Citing Lumi
```
@inproceedings{Jacobs2021,
    author = {Arthur S. Jacobs and Ricardo J. Pfitscher and Rafael H. Ribeiro and Ronaldo A. Ferreira and Lisandro Z. Granville and Walter Willinger and Sanjay G. Rao},
    title = {Hey, Lumi! Using Natural Language for Intent-Based Network Management},
    booktitle = {2021 {USENIX} Annual Technical Conference ({USENIX} {ATC} 21)},
    year = {2021},
    isbn = {978-1-939133-23-6},
    pages = {625--639},
    url = {https://www.usenix.org/conference/atc21/presentation/jacobs},
    publisher = {{USENIX} Association},
    month = jul,
}
```

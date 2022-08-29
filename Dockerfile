# base image
# a little overkill but need it to install dot cli for dtreeviz
FROM python:3.10-buster

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
# making directory of app
WORKDIR /streamlit-docker

RUN mkdir -p /root/.streamlit && mkdir -p /streamlit-docker/files && mkdir -p /streamlit-docker/logs && mkdir -p /streamlit-docker/data

# copy over requirements
RUN apt update && apt install -y gcc python3-dev make git

RUN pip3 install poetry

COPY poetry.lock pyproject.toml /streamlit-docker/

RUN poetry install --no-dev --no-interaction
RUN poetry run spacy download pt_core_news_lg

# copying all files over
COPY . .
RUN chmod +x entrypoint.sh

# streamlit-specific commands for config
COPY .streamlit /root/.streamlit
ENV PYTHONPATH="/streamlit-docker/functions:/streamlit-docker/rules:/streamlit-docker/pages:/streamlit-docker/src:/streamlit-docker/src/pages:/streamlit-docker"

# cmd to launch app when container is run
ENTRYPOINT [ "./entrypoint.sh" ]
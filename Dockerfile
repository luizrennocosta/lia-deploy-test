# base image
# a little overkill but need it to install dot cli for dtreeviz
FROM python:3.7

# ubuntu installing - python, pip, graphviz
# RUN apt-get update &&\
#     apt-get install python3.7 -y &&\
#     apt-get install python3-pip -y &&\
#     apt-get install graphviz -y

# exposing default port for streamlit
EXPOSE 8501

# making directory of app
WORKDIR /streamlit-docker

# copy over requirements
RUN apt update && apt install -y gcc python3-dev make git

ARG EXTERNAL_REPOSITORY_SSH_KEY

RUN mkdir /streamlit-docker/files
RUN mkdir -p /root/.ssh
RUN echo $EXTERNAL_REPOSITORY_SSH_KEY | base64 -d >> /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa
RUN ssh-keyscan -T 60 bitbucket.org >> /root/.ssh/known_hosts

RUN pip3 install poetry && \
    poetry config virtualenvs.create false

COPY . .

RUN poetry install --no-dev --no-interaction

# copying all files over
COPY . .

# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableXsrfProtection = false\n\
" > /root/.streamlit/config.toml'

# cmd to launch app when container is run
CMD poetry run streamlit run app.py --server.address=*

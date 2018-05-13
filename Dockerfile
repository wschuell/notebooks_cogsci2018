
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install --yes --force-yes apt-utils build-essential python-dev liblzo2-dev liblzma-dev libsqlite3-dev python3-tk tmux
RUN pip install numpy matplotlib scipy psycopg2 codecov coverage jupyter
RUN pip install -e git+https://github.com/flowersteam/naminggamesal.git@49c5f057fc76bb74305de2d262eace56faacbc11#egg=naminggamesal
RUN python3 -m ipykernel install
RUN mkdir /naminggamesal
WORKDIR /naminggamesal

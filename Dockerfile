
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install --yes --force-yes apt-utils build-essential python-dev liblzo2-dev liblzma-dev libsqlite3-dev python3-tk tmux
RUN pip install numpy matplotlib scipy psycopg2-binary codecov coverage jupyter
RUN pip install -e git+https://github.com/flowersteam/naminggamesal.git@defc0c615ba9b8120e586358067cb32147db2a21#egg=naminggamesal
RUN pip install -e git+https://github.com/wschuell/experiment_manager.git@20c47ffa63fec9f1face69a578501449d7b92f12#egg=experiment_manager
RUN python3 -m ipykernel install
RUN mkdir /naminggamesal
WORKDIR /naminggamesal

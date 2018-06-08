
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install --yes --force-yes apt-utils build-essential python-dev liblzo2-dev liblzma-dev libsqlite3-dev python3-tk tmux
RUN pip install numpy matplotlib scipy psycopg2-binary codecov coverage jupyter
RUN pip install -e git+https://github.com/flowersteam/naminggamesal.git@707ba80388bb81b6895580397866e6af272fb7db#egg=naminggamesal
RUN pip install -e git+https://github.com/wschuell/experiment_manager.git@90e79ced4582a9bd980a5a0e549bc42039db1363#egg=experiment_manager
RUN python3 -m ipykernel install
RUN mkdir /naminggamesal
WORKDIR /naminggamesal

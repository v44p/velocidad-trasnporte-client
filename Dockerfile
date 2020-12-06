FROM python:3.8

COPY . /tmp/code/

RUN cd /tmp/code/ \
    && pip install -r requeriments.txt \
    && pip install -e .


CMD ["python3", "-m", "velocidad_trp"]

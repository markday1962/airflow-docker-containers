FROM python:3.8-slim

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY scripts/s3-sync.py /usr/local/bin/s3-sync
RUN chmod +x /usr/local/bin/s3-sync

ENTRYPOINT ["/usr/local/bin/python3"]
CMD ["/usr/local/bin/s3-sync"]

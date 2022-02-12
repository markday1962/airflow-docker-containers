FROM python:3.8-slim

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip --no-cache-dir install --upgrade awscli

COPY scripts/s3-sync.sh /usr/local/bin/s3-sync
RUN chmod +x /usr/local/bin/s3-sync

ENTRYPOINT ["/usr/local/bin/s3-sync"]

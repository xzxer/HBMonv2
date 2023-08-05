FROM python:alpine3.18

COPY entrypoint-proxy /entrypoint

RUN adduser -D -u 54001 hbmon && \
        apk update && \
        apk add git gcc musl-dev libffi-dev libssl-dev cargo && \
        pip install --upgrade pip && \
        pip cache purge && \
        cd /opt && \
        git clone https://github.com/ShaYmez/HBMonv2.git && \
        cd /opt/HBmonv2 && \
        pip install --no-cache-dir -r requirements.txt && \
        apk del git gcc musl-dev && \
        chown -R radio: /opt/HBMonv2

USER hbmon

ENTRYPOINT [ "/entrypoint" ]

FROM python:3.7-alpine
LABEL maintainer="fredyalmenares@gmail.com"
ADD ["./src/*.txt", "./src/*.py", "/app/src/"]
RUN apk update  && \
 apk add bash && \
 pip3 install --upgrade pip && \
 cd /app/src && \
 pip3 install -r requirement-dev.txt && \
 echo "**** Python deps installed ****"

ENTRYPOINT tail -f /dev/null
WORKDIR /app/src

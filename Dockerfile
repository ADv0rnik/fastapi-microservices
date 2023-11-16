FROM ubuntu:latest
LABEL authors="alex-dvornik"

ENTRYPOINT ["top", "-b"]
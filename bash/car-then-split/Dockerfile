FROM golang:1.19

RUN go install github.com/ipld/go-car/cmd/car@latest
RUN go install github.com/alanshaw/go-carbites@latest
RUN go install github.com/filecoin-project/go-fil-commp-hashhash/cmd/stream-commp@latest

COPY ./car-then-split.sh /bin/
COPY ../utils /utils/

ENV PATH=/bin:$PATH

WORKDIR /car-files


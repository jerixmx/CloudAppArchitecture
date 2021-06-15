FROM golang:alpine
LABEL description="Udacity sample for Docker walkthrough"
WORKDIR /go/src/app
COPY . /go/src/app
# Required during build attempt
# For tracking code dependencies
RUN go mod init 

RUN go build -o helloworld
EXPOSE 6111/tcp
EXPOSE 6111/udp
CMD ["helloworld"]
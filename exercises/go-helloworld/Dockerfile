FROM golang:alpine
LABEL description="Udacity sample for Docker walkthrough" \
    version="2.0.0"
WORKDIR /go/src/app
COPY . .
# Required during build attempt
# For tracking code dependencies
RUN go mod init 

RUN go build -o helloworld
EXPOSE 6112
CMD ["./helloworld"]

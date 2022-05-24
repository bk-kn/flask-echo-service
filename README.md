# flask-echo-service

- A simple echo service implemented in Flask
- Its intended for learning purposes

## Quick start

- start the docker container
  - command: `docker run --rm -it --name pyEcho -p 5000:5000 bkkn/flask-echo-service:0.1.0`
  - Flask now starts to run inside the container and listens on port 5000

## Usage

### via Browser

- The root page (localhost:5000/) would bring up a Form where you can enter the details like:
  - Your name
  - Your user id
  - Any message
- When you click on the "Submit" button, your input would be forwarded to the echo service (localhost:5000/echo) and it echoes back your input in a Table.

### via curl

- It is also possible to directly post your input data to the echo service, via the curl command
- `curl -X POST -F name=xyz -F id=bk-kn -F comment=awesome -F any-key=any-value http://localhost:5000/echo`
- The above curl command echoes back with a html response that contains a Table with all your input data (key-value pairs)

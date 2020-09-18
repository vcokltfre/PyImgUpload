# vcokltfre/PyIngUpload

## A simple Python program to upload images to a server and return the URL with token based authentication

#### Setup

First, clone the repo and change directory to it.

Next, in `docker-compose.yml` edit the `HOST` environment variable to be the IP or domain name of your server, without 'http://', and change the `TOKEN` variable to be your token. Don't make it easy to guess.

Now run `sudo docker-compose up -d` to run the server
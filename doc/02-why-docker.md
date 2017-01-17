# Chapter 2 - Why Docker

### Goals

- be able to explain to someone why you use Docker
- be able to publish an Nginx image that returns a custom HTML file

## Examples of Applications shipped also with Docker

- [library/postgres](https://hub.docker.com/_/postgres/) the Postgres database
- [library/jenkins](https://hub.docker.com/_/jenkins/) the Jenkins build system
- [yajo/cupsd](https://hub.docker.com/r/yajo/cupsd/) a printer management system
- [mikesir87/aws-cli](https://hub.docker.com/r/mikesir87/aws-cli/) the AWS command-line client

## Exercise 2.1 Write, build and publish your own Nginx image

Install and configure Nginx on your Macbook's and Linux systems...

... only joking!

**End-goal:** We want an Nginx image published on Docker Hub with our own username, a bit like this [one](https://hub.docker.com/r/1science/nginx/) but without all the nice documentation. The only criteria is that, when we run it, it serves our HTML file.

- 1) Navigate to the `./exercises/chapter2/nginx` directory in your command-line

`Choice Time:` Pick an operating system you want to install Nginx on. Most common: CentOS, Ubuntu, ArchLinux. Unknown territory: Microsoft's [Nanoserver](https://hub.docker.com/r/microsoft/nanoserver/)
- 2) Find a Docker image on Docker Hub that **is** that operating system.
- 3) Fill in the `FROM` step in the `Dockerfile` with that image name
- 4) Find the installation instructions for Nginx, for that particular operating system
- 5) Fill in the `RUN` steps in the `Dockerfile` with those instructions
- 6) Find the command that **runs** Nginx on your chosen operating system
- 7) Fill in the `CMD` step in the `Dockerfile` with that command
- 8) Build your `Dockerfile` into an `image`

`Hint:` This is where you start looking at `docker help` and what you can do with it.
- 9) Run a new container using that image!

`Hint:` When running it, you need to expose Nginx's internal port (port 80) to a host port of your choosing.
- 10) Make sure you can see the HTML page in your browser!

`Hint:` If not, is the container running? What are the container's logs showing?
- 11) Push your Docker image to Docker Hub!

`Hint:` You will find that a 1-part image name like `mynginx` is not enough context to publish the image. You'll need a full name like `<your username>/nginx` in order to publish.

## Some philosophies

Docker reduces the developer’s consideration overhead to the bare minimum of TCP/UDP communication and dealing with a simple service manager `docker [start|stop|rm|kill]`.

It's there for easily distributing reusable artifacts across different environments. See this endless list of package formats and service managers. However, how should Docker stretch our understanding of a service manager? We musn't forget what we said in Chapter 1, Docker containers are immutable and ephemeral runnables.

## Conclusion

Hopefully you see how using Docker has, near effortlessly, made your creation portable to all the popular platforms out there, and you only needed to learn how to install and configured it on one of them!

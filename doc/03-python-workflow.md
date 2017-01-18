# Chapter 3 - Getting a basic Python workflow (Partially complete)

### Goals

- be able to dockerize a Python-based web server

## Exercise 3.1 Develop a basic Python workflow

Whenever you work with a dockerized application it's less obvious that, at some point in the past, someone
put in place the groundwork on which you're executing your day-to-day work. This exercise looks at that groundwork
specifically for a Python application.

**End-goal:** Write the Dockerfile for this Python application such that, when you build and run it, you see the response 'Hello world' via the browser. In addition, fill in the build and run scripts so that the next person that comes along can find
an easy workflow to work with, when developing this Python app.

- 1) Navigate to the `./exercises/chapter3/python-basic` directory in your command-line

`Choice Time:` Pick an operating system you want to install your Python application on. Most common: CentOS, Ubuntu, ArchLinux.
- 2) Find a Docker image on Docker Hub that is that operating system.
- 3) Fill in the `FROM` step in the `Dockerfile` with that image name
- 4) Fill in the `COPY` steps in the `Dockerfile`, with the files you need to run your application
- 5) Fill in the `RUN` steps that you need in the `Dockerfile`

`Hint:` If you're unsure what commands you need and are feeling a bit lost, why not try the approach mentioned [in the previous chapter](./02-why-docker.md#a-trick-to-help-with-the-dockerfile-writing-part).
- 6) Fill in the command that **runs** the application in the `CMD` step
- 7) Build your `Dockerfile` into an `image`
- 8) Run a new container using that image!

`Debugging hint:` This is where you start looking at `docker help` and what you can do with it.
`Network hint:` When running it, you need to expose Flask's port to a host port of your choosing.
- 9) Make sure you can see the 'Hello world' in your browser!

`Hint:` If not, is the container running? What are the container's logs showing? `docker help` is your friend again for these questions.
- 10) With the build and run commands that you used, now fill in the `build` and `run` Bash scripts that already exist in the directory.
- 11) Now, if someone is developing the Python code, what are the steps they would take to see their updates in the browser?

### Food for thought

- Does your Docker container automagically reload the Python code when you change it? Why not?

## Hints for next time

Which base Docker image did you use? Which installation steps did you have to run
before running your Python application? Coudl those steps have been avoided by
using a different, more specific, base image?

### Conclusion

...

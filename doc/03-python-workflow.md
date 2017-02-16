# Chapter 3 - Getting a basic Python workflow

## Goals

- be able to dockerize a Flask web server
- come up with the steps that developers will use on a regular basis

## Exercise 3.1 Develop a basic Python workflow

Whenever you work with a dockerized application it's less obvious that, at some point in the past, someone
put in place the groundwork on which you're executing your day-to-day work. Now there are some very critical
parts in that groundwork that would make a normal workflow near impossible.

This exercise looks at that groundwork specifically for a Flask application.

**End-goal:** Write the Dockerfile for this Python application and come up with the workflow steps for an engineer to be able to pick it up and iterate on this application effectively.

### Milestone 1

- 1) Navigate to the `./exercises/chapter3/python-basic` directory in your command-line

`Choice Time:` Think about what base image we need. What are we looking for our environment to have, given the service we want to run on it?
- 2) Find a Docker image on Docker Hub that is what you're looking for.
- 3) Fill in the `FROM` step in the `Dockerfile` with that image name
- 4) Fill in the `COPY` steps in the `Dockerfile`, with the files you need to run your application
- 5) Fill in the `RUN` steps that you need in the `Dockerfile`

`Hint:` If you're unsure what commands you need and are feeling a bit lost, why not try the approach mentioned [in the previous chapter](./02-why-docker.md#a-trick-to-help-with-the-dockerfile-writing-part).
- 6) Fill in the command that **runs** the application in the `CMD` step
- 7) Build your `Dockerfile` into an `image`
- 8) Run a new container using that image!

`Debugging hint:` This is where you start looking at `docker help` and what you can do with it.
`Network hint:` When running it, you need to expose Flask's port to a host port of your choosing.
- 9) Make sure you can see the usage instructions on http://localhost:9000 in your browser and you're able to play with the API.

`Hint:` If not, is the container running? What are the container's logs showing? `docker help` is your friend again for these questions.
- 10) With the build and run commands that you used, now fill in the `build` and `run` placeholder scripts that already exist

- 11) Now, if someone is developing the Python code, what are the steps they would take to see their updates in the browser?

### Food for thought

- Which base Docker image did you use? What installation steps did you have to run before running your Python application? Could those steps have been avoided by using a different, more specific, base image?

- Does your Docker container automagically reload the Python code when you change it? Why not?

Let's get some automagic-ness in our next steps!

### Milestone 2

- 12) Make Flask reload when files change
- 13) Change the configuration of your `docker run` call to make sure that as you change the Python files with your IDE, the changes get reflected in your running Python application automagically. Time for a docker volume!! :tada: 
- 14) Given file changes now get reflected inside the container, change the query text passed to the Giphy API to always append the word `scotland` to whatever the user is searching for. Test the effectiveness of your changes!
- 14) Provided you've tested the steps yourself, fill in the missing instructions in `scripts/help` so that new joiners will find their way around!

## Conclusion

There's a dual achievement to what we've done here, even though we only intended for the developer workflow part of it.

For the developer workflow it's fairly obvious why this is beneficial, but regardless let's take a moment to list why this is better than just running the Python application without Docker:

- we did not install any system-wide or even user-wide dependencies on our host system, based on what our Python application requires.

I.e. imagine if we're installing geocoding OS libraries, PDF generation ones and so on, and we've have to manage those versions somehow, as well as make sure all these libraries exist on OS X + Ubuntu... eek!

- we've got complete control and isolation of our libraries, Python version and Pip dependencies.

I.e. there's no way installing another dependency on our host system is going to affect our application's dependencies by overwriting it, removing it, breaking it. And the manifest for managing these is all in one place, the Dockerfile.

The second achievement here and extremely important as well, is that we've suddenly created our [package](https://github.com/lystable/learning-docker/blob/master/doc/01-concepts.md#image), as we called it in our initial introduction to Docker, which is the Docker image. The value out of that, we should not forget, is that it's cross-platform, distributable and deployable service, where the user is completely agnostic of what it's written in and what dependencies it may have. It is just an HTTP port to them.

### More food for thought

- What system dependencies does one need to install, besides the IDE, in order to work on this application?

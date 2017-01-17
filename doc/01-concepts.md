# Chapter 1 - Concepts

### Goals

- be able to name and place the basic concepts of the Docker ecosystem within the areas of package management and service management
- be able to name at least one equivalent concept for each
- be able to conceptualise the flow of operations from a bare package specification until we get a running service in another environment

## Intro

For the sake of placing and using Docker in the software development world, we are going to look at it as a system for two things:

- package management
- service management

## Dockerfile

The `Dockerfile` is your package manifest or specification. It describes how your package will be built.

Similarly, RPM or Debian packages have the `.spec` spec file that describes how the `rpmbuild` application is going to build them into an `.rpm` package.

Once you've built your `Dockerfile` you end up with your package, or in this case the Docker `image`.

## Image

Building your `Dockerfile` results in a package we refer to as `image`.

There are many [popular equivalent concepts](https://en.wikipedia.org/wiki/List_of_software_package_management_systems#Windows) including Debian packages `.deb`, RPM packages `.rpm` or Windows executables `.exe`.

Contrary to those known concepts, we don't have direct access to the file that **is** the Docker image. Instead, we download, publish, delete or do any other operation via the Docker API, and by default we use the command-line client to talk to that.

## Container

Now, in order to form our perspective, the Docker `container` concept is where we stretch our understanding of packages and services a little, as here we enter the grounds of virtualisation.

#### Creation / Deletion

**Creating** a `container` is the equivalent of creating a virtual machine, with its own operating system, filesystem and process manager.

**Deleting** a `container`, also, will get rid of this operating system and any state that it may have created in its filesystem.

#### Starting / Stoping

The Docker `container` does indeed contain a started and running service, as an equivalent [service management system](https://en.wikipedia.org/wiki/Operating_system_service_management) like the [Windows service manager](http://tools.sysprogs.org/srvman/) or Linux's [upstart](http://upstart.ubuntu.com/) would take care of doing for you.

**Starting** the `container` will start your service, which is running as the process with PID 1 and **stopping** the `container` will stop your service.

#### Docker's disruptive nature

Now the implications of Docker's ease and speed at which it spins up isolated environments for us has:

- made us so agnostic of this virtual machine and all its internals, that we end up looking at it more as a **service**. At least this is the case when we're simply using it and bulding on top of it.
- successfully solidified the boundaries that running services should have with their surrdounding environment, by demanding immutability from these packages, making them only customisable via input parameters which are given at initialisation time of the `container` or... as we should rather think of it, the `service`

## Daemon & Client

The Docker `deamon` runs on your machine from the point of installation. It is the server, that you issue commands to when you manipulate your images and containers.

We interact with the `daemon` using the command-line `client` which is installed by default, the `docker` tool.

## Docker Hub

[Docker Hub](http://hub.docker.com/) is your publically available Docker `image` registry, the equivalent of an [APT repo](https://www.ubuntuupdates.org/ppa/canonical_partner) for Debian packages, or a [YUM repo](http://dl.fedoraproject.org/pub/epel/) for RPM packages.

Contrary to APT / YUM repos, you don't need to install any references in order to talk to Docker Hub, you can just publish (known as `push`) and download (known as `pull`) images using the `docker` tool from the point of installation.

## Conclusion

Aligning the Docker concepts with these existing ones, you should hopefully easily be able to conceptualise that to get a package running on a remote system the flow is:

- [Local] Write a `Dockerfile`
- [Local] Build the `image` from that `Dockerfile`
- [Local] Publish the `image` on Docker Hub
- [Remote] Pull the `image` from Docker Hub
- [Remote] Start a `container` from that `image`

Provided the Local and the Remote machines both have Docker installed and access to the internet.

That's the most theory we'll ever go over in a single chapter, promise! We just had to get some fundamental things out of the way. Now, don't be afraid to cycle back and take a look at some of these again if you need to!

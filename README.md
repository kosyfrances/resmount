# Resmount
(Code Challenge)

Resmount is a small http server in Python that returns a json response with the list of mount points. Resmount gets its information from `/proc/self/mountinfo`.

### Tech
Resmount is written in Python3.

### Setup (With Docker)
To use Resmount, be sure to have [docker](https://docs.docker.com/engine/installation/) installed and set up on your machine first.

* Check if you have [jq](https://stedolan.github.io/jq/) installed by typing ` which jq` on the commandline. Install it if you get an empty response.

* Clone this repo
    ```
    $ git clone https://github.com/kosyfrances/resmount.git
    ```

* cd into resmount directory

* Build Resmount docker image by running
    ```
    $ docker build -t resmount .
    ```
    NOTE: If you get an error like this `Got permission denied while trying to connect to the Docker daemon socket at ...` then run the docker commands with `sudo`.

* Now run Resmount app in the background in detached mode
    ```
    $ docker run -d -p 5555:5555 resmount
    ```
* View mount points on the docker container by running
    ```
    $ curl -sS localhost:5555 | jq -r .
    ```
*  The output will be something like this:
    ```
    {
      "mount_points": [
        "/sys",
        "/proc",
        "/dev",
        "/dev/pts",
        "/run",
        "/",
        ....
      ]
    }
    ```
* To stop the running docker container, check the abbreviated container ID with
    ```
    $ docker container ls
    ```
* Copy the CONTAINER ID and use it to stop the container by running
    ```
    $ docker stop CONTAINER_ID
    ```

### Setup on a Linux machine (Without Docker)
* Be sure to have python3 set up
* Check if you have [jq](https://stedolan.github.io/jq/) installed by typing `which jq` on the commandline. Install it if you get an empty response.
* Clone this repo
    ```
    $ git clone https://github.com/kosyfrances/resmount.git
    ```
* cd into resmount directory and run
    ```
    $ python3 server.py
    ```
* View mount points commandline by running
    ```
    $ curl -sS localhost:5555 | jq -r .
    ```
* The output will be something like this:
    ```
    {
      "mount_points": [
        "/sys",
        "/proc",
        "/dev",
        "/dev/pts",
        "/run",
        "/",
        ....
      ]
    }
    ```
``
    {
      "mount_points": [
        "/sys",
        "/proc",
        "/dev",
        "/dev/pts",
        "/run",
        "/",
        ....
      ]
    }
    ```

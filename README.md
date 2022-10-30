# cert-auth

[![Docker Image CI (build, tag, push)](https://github.com/ilDug/cert-auth/actions/workflows/docker-image.yaml/badge.svg)](https://github.com/ilDug/cert-auth/actions/workflows/docker-image.yaml)

certificate authority managment

# Pull docker image
please refer to Github Container Registry: [cert-auth docker image](https://github.com/ilDug/cert-auth/pkgs/container/cert-auth)

```
docker pull ghcr.io/ildug/cert-auth:<VERSION>
```

# Run Certificate Authority

You can choose two solution: 
- A. create a new root certificate and an empty PKI
- B. use an existing root Authority (crt and key), importing them.

## A). Create New root and PKI

Create a folder named ```PKI```. where the Infrastructure will be built.

In your folder run the container and execute the aplication.

```bash
# on MacOs
docker run -it --rm -v "$PWD/PKI":"/PKI" ghcr.io/ildug/cert-auth:<VERSION>

# on Windows
docker run -it --rm -v ${pwd}/PKI:/PKI ghcr.io/ildug/cert-auth:<VERSION>
```
Below the common commands.


## B). Import root certificate and crete PKI

- create a folder named ```PKI```. where the Infrastructure will be built
- create a folder named ```import``` and  place your existing root certificate (with .crt extension) and the related private key (with .key extension). Please no put other files into it.

run these command: 
```
docker run -it --rm -v ${pwd}/PKI:/PKI -v ${pwd}/import:/import ghcr.io/ildug/cert-auth:<VERSION>
```

# Commands

By default application disply help message. In order to run properly, add selected command at previous one:

## ```install```

create the PKI infrastructure. All files into PKI directory will be removed.

## ```import```

create the PKI infrastructure and add your certificate and key. All files into PKI directory will be removed.

## other commands
please, explore all possible command using ```--help``` option.


docker run -it --rm  -v ${pwd}/app:/app -v ${pwd}/PKI:/PKI ildug/cert-auth

docker run -it --rm -v ${pwd}/PKI:/PKI ildug/cert-auth
docker run -it --rm -v ${pwd}/PKI:/PKI ghcr.io/ildug/cert-auth:v1.1.11


docker run -it --rm -v ${pwd}/PKI:/PKI -v ${pwd}/import:/import ildug/cert-auth

docker build -t ildug/cert-auth:dev .

docker build -t ildug/cert-auth:1.1.1 .




# GH Container Registry
export GHCR_TK=

echo $GHCR_TK | docker login ghcr.io -u @ilDug --password-stdin


docker push ghcr.io/ilDug/cert-auth:latest
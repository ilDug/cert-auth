docker run -it --rm  -v ${pwd}/app:/app -v ${pwd}/PKI:/PKI ildug/cert-auth

docker run -it --rm -v ${pwd}/PKI:/PKI ildug/cert-auth

docker run -it --rm -v ${pwd}/PKI:/PKI -v ${pwd}/import:/import ildug/cert-auth

docker build -t ildug/cert-auth:dev .

docker build -t ildug/cert-auth:1.1.1 .

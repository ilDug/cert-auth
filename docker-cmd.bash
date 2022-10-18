docker run -it --rm  -v ${pwd}/app:/app -v ${pwd}/PKI:/PKI cert-auth

docker run -it --rm -v ${pwd}/PKI:/PKI cert-auth

docker build -t cert-auth .
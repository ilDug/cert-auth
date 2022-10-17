from dataclasses import dataclass
from pathlib import Path
from string import Template


PRIV_KEY_GEN = Template("openssl genrsa -out $keypath $bits")
# print(GEN_PRIV_KEY.substitute(keypath=None,bits=2048'))

REQ_GEN = Template(
    "openssl req -config $configpath -new -sha256 -verbose -batch -key $keypath -out $csrpath"
)
# GEN_REQ.substitute(configpath=None, kaypath=None, csrpath=None)

REQ_PRINT = Template("openssl req -text -noout -in $crspath")
# REQ_PRINT.substitute(csrpath=None)


CERT_GEN = Template(
    "openssl ca -config $confpath -notext -md sha256 -days $days -verbose -batch -extfile $extpath -extensions req_ext -passin file:'$passphrsepath' -in $crspath -out $crtpath"
)
# CERT_GEN.substitute(
#     confpat=None, days=365, extpath=None, passphr=None, crspath=None, crtpath=None
# )

CERT_PRINT = Template("openssl x509 -noout -text -in $crtpath")
# CERT_PRINT.substitute(crtpath=None)

CERT_VERIFY = Template("openssl verify -CAfile $capath $crtpath")
# CERT_VERIFY.substitute(capath=None, crtpath=None)


PUB_KEY_GEN = Template("openssl x509 -pubkey -noout -in $crtpath -out $pubkypath")
# CA_PUB_KEY.substitute(crtpath=None,pubkypath=None)

CA_KEY_GEN = Template(
    "openssl genrsa -aes256 -passout file:$passphrasepath -out $cakeypath 4096"
)
# CA_KEY_GEN.substitute(passphrasepath=None, cakeypath=None)

CA_CRT_GEN = Template(
    "openssl req -config $configpath -new -x509 -nodes -days $days -sha256 -extensions v3_ca -passin file:$passphrasepath -key $cakeypath -out $cacrtpath"
)
# CA_CRT_GEN.substitute(configpath=None,days=365,passphrasepath=None,cakeypath=None, cacrtpath=None)

CA_PUB_KEY_GEN = Template("openssl x509 -pubkey -noout -in $cacrtpath -out $pubkeypath")
# CA_PUB_KEY_GEN.substitute(cacrtpath=None, pubkeypath=None)


PASSPHRASE_GEN = Template("openssl rand -base64 -out '$passphrasepath' $length")
# PASSPHRASE_GEN = Template("openssl rand -base64  $length")
# PASSPHRASE_GEN.substitute(passphrasepath=None, length=24)

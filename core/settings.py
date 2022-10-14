from decouple import config
from pathlib import Path
import uuid

# PKI
###############################
PKI_PATH = Path(__file__).parents[1] / "PKI"
KEYS_PATH = PKI_PATH / 'private'
REQS_PATH = PKI_PATH / 'reqs'
CONFIGS_PATH = PKI_PATH  / 'configs'
CERTS_PATH= PKI_PATH / 'certs'

CA_CERT_PATH =CERTS_PATH / 'ca.crt'
CA_KEY_PAT = KEYS_PATH / 'ca.key'

CNF_DEFAULT = Path(__file__).parents[0] / 'config/default.cnf'
CNF_OPENSSL = Path(__file__).parents[0] / 'config/openssl.cnf'
PASSPRHASE = config("PASSPRHASE")


# ACTIVATION_KEY_LENGTH = config("ACTIVATION_KEY_LENGTH", cast=int)
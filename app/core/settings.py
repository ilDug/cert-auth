from decouple import config
from pathlib import Path
import uuid

# PKI
###############################
# PKI_PATH = Path(__file__).parents[1] / "PKI"
PKI_PATH = Path("/PKI")
KEYS_PATH = PKI_PATH / "private"
REQS_PATH = PKI_PATH / "reqs"
CONFIGS_PATH = PKI_PATH / "configs"
CONFIG_FILE = CONFIGS_PATH / "openssl.cnf"
CERTS_PATH = PKI_PATH / "certs"
PASSPRHASE_PATH = PKI_PATH / "private/_passphrase"
PUBLIC_PATH = PKI_PATH / "public"

CA_CRT_PATH = CERTS_PATH / "ca.crt"
CA_KEY_PATH = KEYS_PATH / "ca.key"
CA_PUB_PATH = PUBLIC_PATH / "ca.pub.pem"

CNF_BASE_DEFAULT = Path(__file__).parents[0] / "config/default.cnf"
CNF_BASE_OPENSSL = Path(__file__).parents[0] / "config/openssl.cnf"

# PASSPRHASE = config("PASSPRHASE")


# ACTIVATION_KEY_LENGTH = config("ACTIVATION_KEY_LENGTH", cast=int)

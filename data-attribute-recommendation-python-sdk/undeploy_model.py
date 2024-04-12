import json
import logging
import pprint

from sap.aibus.dar.client.model_manager_client import ModelManagerClient

# Show some output while the script is working
logging.basicConfig(level=logging.INFO)

MODEL_NAME = "bestbuy-category-prediction"

# Read file with service key
with open('darservicekey.json', 'r') as sk_file:
    sk_data = sk_file.read()

# Load from file
json_data = json.loads(sk_data)

mm_client = ModelManagerClient.construct_from_credentials(
    dar_url=json_data['url'],
    clientid=json_data['uaa']['clientid'],
    clientsecret=json_data['uaa']['clientsecret'],
    uaa_url=json_data['uaa']['url'],
)

mm_client.ensure_model_is_undeployed(MODEL_NAME)

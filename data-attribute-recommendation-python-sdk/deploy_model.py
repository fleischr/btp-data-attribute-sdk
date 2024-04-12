import json
# Show some output while the script is working
import logging
import pprint

from sap.aibus.dar.client.model_manager_client import ModelManagerClient

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

deployment_resource = mm_client.create_deployment(MODEL_NAME)
deployment_id = deployment_resource["id"]
print("Created Deployment for model '%s' with deployment ID '%s'" % (
    MODEL_NAME, deployment_id))

pprint.pprint(deployment_resource)

print("Waiting for Deployment to succeed.")
updated_deployment_resource = mm_client.wait_for_deployment(deployment_resource['id'])
print("Deployment finished. Final state:")
pprint.pprint(updated_deployment_resource)

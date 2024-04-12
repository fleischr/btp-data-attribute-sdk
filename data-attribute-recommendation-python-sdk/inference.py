import json
import logging
import pprint

from sap.aibus.dar.client.inference_client import InferenceClient

# Show some output while the script is working
logging.basicConfig(level=logging.INFO)

MODEL_NAME = "bestbuy-category-prediction"

# Read file with service key
with open('darservicekey.json', 'r') as sk_file:
    sk_data = sk_file.read()

# Load from file
json_data = json.loads(sk_data)

inference_client = InferenceClient.construct_from_credentials(
    dar_url=json_data['url'],
    clientid=json_data['uaa']['clientid'],
    clientsecret=json_data['uaa']['clientsecret'],
    uaa_url=json_data['uaa']['url'],
)

# The code passes two objects to be classified. Each object
# must have all features described in the DatasetSchema used
# during training.
objects_to_be_classified = [
    {
        "objectId": "optional-identifier-1",
        "features": [
            {"name": "manufacturer", "value": "Energizer"},
            {"name": "description", "value": "Alkaline batteries; 1.5V"},
            {"name": "price", "value":  "5.99"},
        ],
    },
    {
        "objectId": "optional-identifier-2",
        "features": [
            {"name": "manufacturer", "value": "Sony"},
            {"name": "description", "value": "Unravel a grim conspiracy at the brink of Revolution"},
            {"name": "price", "value":  "19.99"},
        ],
    },
    {
        "objectId": "optional-identifier-3",
        "features": [
            {"name": "manufacturer", "value": "Sony"},
            {"name": "description", "value": "A raunchy adventure set in the early 2000s rising pop punk scene"},
            {"name": "price", "value":  "14.99"},
        ],
    },
    {
        "objectId": "optional-identifier-4",
        "features": [
            {"name": "manufacturer", "value": "Fitbit"},
            {"name": "description", "value": "Invigorate your workouts with up to the second heart rate tracking and body fat monitoring"},
            {"name": "price", "value":  "179.99"},
        ],
    },
]

inference_response = inference_client.create_inference_request(
    model_name=MODEL_NAME,
    objects=objects_to_be_classified
)

pprint.pprint(inference_response)

from sap.aibus.dar.client.workflow.model import ModelCreator
import json
import pprint

# Show some output while the script is working
import logging
logging.basicConfig(level=logging.INFO)

MODEL_NAME = "bestbuy-category-prediction"

# Read file with service key
with open('darservicekey.json', 'r') as sk_file:
    sk_data = sk_file.read()

# Load from file
json_data = json.loads(sk_data)

# Create a ModelCreator instance by passing the credentials
# to the ModelCreator.construct_from_credentials class method
creator = ModelCreator.construct_from_credentials(
    dar_url=json_data['url'],
    clientid=json_data['uaa']['clientid'],
    clientsecret=json_data['uaa']['clientsecret'],
    uaa_url=json_data['uaa']['url'],
)

# Define the DatasetSchema which describes the CSV layout.
new_schema = {
    "features": [
        {"label": "manufacturer", "type": "CATEGORY"},
        {"label": "description", "type": "TEXT"},
        {"label": "price", "type": "NUMBER"},
    ],
    "labels": [
        {"label": "level1_category", "type": "CATEGORY"},
        {"label": "level2_category", "type": "CATEGORY"},
        {"label": "level3_category", "type": "CATEGORY"},

    ],
    "name": "bestbuy-category-prediction",
}

# Load training data
training_data_stream = open("bestBuy.csv", mode="rb")

# Upload data and train model
final_api_response = creator.create(
    model_template_id="d7810207-ca31-4d4d-9b5a-841a644fd81f",
    dataset_schema=new_schema,
    model_name=MODEL_NAME,
    data_stream=training_data_stream,
)

pprint.pprint(final_api_response)

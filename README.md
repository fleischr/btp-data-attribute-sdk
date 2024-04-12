# SAP BTP Data Attribute Recommendations SDK

Info:
- Based on https://developers.sap.com/tutorials/cp-aibus-dar-sdk-usage.html
- Maintain the service key in darservicekey.json
- quick mod in the SDK

Got this bugfix from chatgpt because of an error I got earlier

"The error you're encountering is related to the usage of the deprecated method_whitelist argument in the Retry class from the urllib3 library. This argument has been deprecated and replaced with allowed_methods.

Here are the steps to fix the error:

Update the library code:

Locate the file causing the error (as indicated in the traceback, the file http_transport.py in the sap\aibus\dar\client\util directory).
Open this file and search for the usage of Retry.
Replace method_whitelist with allowed_methods.
Here is an example of how the updated code might look:
python
Copy code
retry = Retry(
    total=num_retries,
    backoff_factor=backoff_factor,
    status_forcelist=status_forcelist,
    allowed_methods=allowed_methods  # Changed from method_whitelist
)"


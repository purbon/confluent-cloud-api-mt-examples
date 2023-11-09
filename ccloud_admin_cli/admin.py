
from ccloud import openapi_client


class CCloudAdminClient:

    def __init__(self, api_key, api_secret):
        self.configuration = openapi_client.Configuration(
            username=api_key,
            password=api_secret
        )
# token.py

import os
import base64

def get_token():
    # Simulate secure retrieval
    token = os.getenv("PROD_SECRET_TOKEN", "not_set")
    return base64.b64decode(token.encode()).decode()
# TODO: add unit tests

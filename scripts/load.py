import json
import pandas as pd
import os

def load_data():
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    file_path = os.path.join(
        base_dir,
        "data",
        "raw",
        "mock_subscription_api_500_users.json"
    )
    
    with open(file_path) as f:
        data = json.load(f)
    records = data["data"]["subscriptionData"]
    df = pd.json_normalize(records)

    return df


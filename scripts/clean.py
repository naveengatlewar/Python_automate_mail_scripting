import pandas as pd


def clean_data(df):
    df["date_created"] = pd.to_datetime(df["date_created"])
    df["startDate"] = pd.to_datetime(df["startDate"], unit="s")
    df["endDate"] = pd.to_datetime(df["endDate"], unit="s")
    df["subscription_type"] = df["First_Period"].map({
    "Yes": "NEW",
    "No": "RENEWAL"
})
    return df



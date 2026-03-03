import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    df.fillna({
        "Cuisines": "Unknown",
        "Price range": df["Price range"].mode()[0],
        "Aggregate rating": df["Aggregate rating"].mean()
    }, inplace=True)

    df = df[df["Aggregate rating"] > 0]
    df.reset_index(drop=True, inplace=True)

    return df
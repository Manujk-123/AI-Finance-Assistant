import pandas as pd

def load_and_prep(df):
    """
    Preprocess training DataFrame.
    Expects df with columns: ['text', 'label']
    """

    # Validate columns
    if "text" not in df.columns or "label" not in df.columns:
        raise ValueError("CSV must contain 'text' and 'label' columns.")

    # Clean text
    df["text"] = (
        df["text"]
        .astype(str)
        .str.lower()
        .str.strip()
    )

    # Ensure labels are string
    df["label"] = df["label"].astype(str)

    X = df["text"]     # Inputs
    y = df["label"]    # Target labels

    return X, y

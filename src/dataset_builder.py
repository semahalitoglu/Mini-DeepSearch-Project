import pandas as pd

def build_dataset(df, mapping, target="math score"):
    mapped_cols = list(mapping.values())
    final_cols = mapped_cols + [target]
    return df[final_cols]

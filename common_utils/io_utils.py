import os

import pandas as pd


def load(obj_name: str, obj_dir: str, type: str) -> pd.DataFrame:
    path = os.path.join(obj_dir, f"{obj_name}.{type}")
    print(path)

    loaders = {
        "parquet": pd.read_parquet,
        "csv": pd.read_csv,
    }

    try:
        load_func = loaders[type]
    except KeyError:
        raise ValueError(
            f"Unsupported file type: '{type}'. Choose from {list(loaders)}."
        )

    return load_func(path)

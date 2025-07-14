import json
import os
from typing import Optional

import pandas as pd

import periodic
from config import DataGen, Function
from dotenv import load_dotenv


load_dotenv()



GENERATOR_CLASS_MAP = {
    Function.SINE: periodic.Sine
}


def get_hashed_metadata(path: Optional[str] = None):
    """
    Returns the metadata for any previously generated datasets
    """
    METADATA_FILE = "metadata.json"

    if not path:
        path = os.getenv("DATA_ROOT")
        if not path:
            raise RuntimeError(
                "DATA_ROOT is not set. Please provide the path explicitly or set the DATA_ROOT environment variable."
            )
    meta_path = os.path.join(path, METADATA_FILE)
    with open(meta_path, "r") as f:
        metadata = json.load(f)

    return metadata

def create_metadata():

    pass


def main():
    synth_configs = DataGen.build().configs
   
    for config in synth_configs:
        print(config)
        func_name = Function(config.function)

        cls = GENERATOR_CLASS_MAP[func_name]
        gen = cls(name=config.name)

        data = gen.generate(
            size=config.size,
            start=config.start,
            stop=config.stop,
            noise_scale=config.noise_scale,
            add_noise=config.add_noise
        )

        data_dir = os.getenv("DATA_ROOT")
        data_path = os.path.join(data_dir, f"{config.name}.parquet")
        data.to_parquet(data_path)


        print(f"Created '{config.name}' with shape: {data.shape}")



if __name__ == "__main__":
    main()

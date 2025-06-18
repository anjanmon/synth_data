import json
import os
from typing import Optional

import periodic
from config import DataGen, FunctionType
from dotenv import load_dotenv

load_dotenv()


GENERATOR_CLASS_MAP = {
    FunctionType.PERIODIC: periodic.Periodic,
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


def main():
    synth = DataGen.build()


#  configs = synth.configs


if __name__ == "__main__":
    main()

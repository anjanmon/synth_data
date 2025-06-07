import os
from dataclasses import dataclass, field
from typing import Generator, List, Optional

import yaml
from dotenv import load_dotenv

load_dotenv()

config = None


@dataclass
class DataGen:
    "Class for keeping track of all the data generators"

    datasets: dict = field(default_factory=dict)
    configs: List["Config"] = field(default_factory=list)

    @property
    def num_configs(self):
        return len(self.config[self.datasets])


@dataclass
class Config:
    name: str
    type: str
    size: Optional[int] = 100
    start: Optional[int] = 0
    stop: Optional[int] = 1
    add_noise: bool = True
    noise_scale: Optional[float] = 0.1


def get_config() -> Generator["Config"]:
    global config
    path = os.getenv("CONFIG_PATH")
    if not config:
        with open(path, "r") as file:
            config = yaml.safe_load(file)
    return config


if __name__ == "__main__":
    config = get_config()
    config = DataGen(config)
    print(config)

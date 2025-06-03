from typing import Generator
import yaml

_config = None

def check_existence():
    pass


def read_config()->Generator:
    with open("configs/generator.yml", "r") as file:
        config = yaml.safe_load(file)
    
    for item in config["datasets"]:
        yield item
    




def run():
    config_gen = read_config()
    
    for data_config in config_gen:
        print(data_config)

    









if __name__=="__main__":
    run()
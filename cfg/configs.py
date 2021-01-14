import yaml

with open('./cfg/conf.yaml') as config:
    cfg = yaml.load(config, Loader=yaml.FullLoader)
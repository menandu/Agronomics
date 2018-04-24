from uaLib import *

with open('config.yaml') as yfl:
    cfg=yaml.load(yfl)

datastore=cfg['datastore']
dataset=cfg['dataset']
dpath=dataset['path']

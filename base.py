from uaLib import *

thisModule='regression/'
p.options.display.width=180

with open('config.yaml') as yfl:
    cfg=yaml.load(yfl)

datastore=cfg['datastore']
dataset=cfg['dataset']
dpath=dataset['path']

datum=dpath+thisModule+'base.csv'
dataset=p.read_csv(datum)

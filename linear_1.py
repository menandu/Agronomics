from uaLib import *

thisModule='regression/linear_1/'
p.options.display.width=180

with open('config.yaml') as yfl:
    cfg=yaml.load(yfl)

datastore=cfg['datastore']
dataset=cfg['dataset']
dpath=dataset['path']
f_train=dpath+thisModule+'train.csv'
f_tst=dpath+thisModule+'tst.csv'

train_set=p.read_csv(f_train)
tst_set=p.read_csv(f_tst)

train_set.dropna(inplace=True)
tst_set.dropna(inplace=True)

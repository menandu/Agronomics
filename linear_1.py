from uaLib import *

thisModule='regression/linear_1/'
p.options.display.width=180

with open('config.yaml') as yfl:
    cfg=yaml.load(yfl)

datastore=cfg['datastore']
dataset=cfg['dataset']
dpath=dataset['path']
f_train=dpath+thisModule+'train.csv'
f_tst=dpath+thisModule+'test.csv'

train_set=p.read_csv(f_train)
tst_set=p.read_csv(f_tst)

train_set.dropna(inplace=True)
tst_set.dropna(inplace=True)

x_train_set=train_set.as_matrix(['x'])
y_train_set=train_set.as_matrix(['y'])
x_tst_set=tst_set.as_matrix(['x'])
y_tst_set=tst_set.as_matrix(['y'])

print('Mean of X Training set: ',n.mean(x_train_set))
print('Mean of Y Training set: ',n.mean(y_train_set))
print()
print('Median of X Training set: ',n.median(x_train_set))
print('Median of Y Training set: ',n.median(y_train_set))
print()
print('S-Dev of X Training set: ',n.std(x_train_set))
print('S-Dev of Y Training set: ',n.std(y_train_set))

# Linear Regression

from uaLib import *

thisModule='uHousing'
p.options.display.width=180

def heart():
	getConfig()
	dataframes()

def getConfig():
	global ffile
	with open('config.yaml') as yfl:
		cfg=yaml.load(yfl)
	datastore=cfg['datastore']
	dataset=cfg['dataset']
	dpath=dataset['path']
	delimits=dataset['delimiters'][thisModule]
	ffile=dpath+thisModule+'/price_paid_records.csv'
	return ffile

def dataframes():
	global hdf
	c=['ttuid','price','tdate','ptype','isnew','duration','city','district','county','ppd_category','recordstatus']
	dates=['tdate']
	dataTypes={'ttuid':'str','price':'int','tdate':'str','ptype':'str','old_new':'str','duration':'str','city':'str','district':'str','county':'str','ppd_category':'str','recordstatus':'str'}
	ss={'N':False,'Y':True}
	hdf=p.read_csv(ffile,header=0,names=c,dtype=dataTypes,parse_dates=dates)
	hdf['isnew']=hdf.isnew.map(ss)
	return 0

def panel():
	print('51. Number of days involved in the dataset')
	print('hdf.tdate.max()-hdf.tdate.min()')
	print('52. Drop records which show invalueble data')
	print('hdf.drop(hdf[hdf.price<100].index,inplace=True)')
	print('53. Fetch the property record with highest and lowest price')
	print('hdf.loc[hdf.price==hdf.price.max()]')
	print('hdf.loc[hdf.price==hdf.price.min()]')
	print('54. Number of records with price equal less than 11000')
	print('len(hdf[hdf.price<11000])')
	print('How many new properties are listed in the dataset')
	print('hdf[hdf.isnew==True]')

heart()
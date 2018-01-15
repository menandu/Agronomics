from uaLib import *

eng='python'
thisModule='movieLens'
p.options.display.width=180

def heart():
	print('Fetching CONFIG files...')
	print('Framing...')
	getConfig()
	dataFrames()
	wrangler()
	print(reserve())
	return 'HEART CONSTRUCTED'

def reserve():
	print('Reserved keywords...')
	d=dir()
	t=[x for x in d if not x.startswith('_')]
	if(len(t)==0):
		return d
	else:
		return t

def getConfig():
	global ffl,mfl,ufl,delimits
	with open('config.yaml') as cFile:
		cfg=yaml.load(cFile)
	datastore=cfg['datastore']
	dataset=cfg['dataset']
	dpath=dataset['path']
	delimits=OrderedDict(dataset['delimiters'])[thisModule]
	ufl=dpath+thisModule+'/users.dat'
	ffl=dpath+thisModule+'/ratings.dat'
	mfl=dpath+thisModule+'/movies.dat'
	return 0

def dataFrames():
	global factFrame,usrFrame,movFrame
	factFrame=p.read_table(ffl,sep=delimits[0],engine=eng)
	usrFrame=p.read_table(ufl,sep=delimits[0],engine=eng)
	movFrame=p.read_table(mfl,sep=delimits[0],engine=eng)
	return movFrame,usrFrame,factFrame

def wrangler():
	global movFrame,f0f
	print('Wrangling Data...')
	ss=movFrame['genre'].str.split(delimits[1]).apply(p.Series,1).stack()
	ss.index=ss.index.droplevel(-1)
	ss.name='genre'
	del movFrame['genre']
	ziz(5)
	movFrame=movFrame.join(ss)
	f0f=factFrame.merge(movFrame,on='mid',how='inner')
	f0f=f0f.merge(usrFrame,on='uid',how='inner')
	return f0f

heart()

def panel():
	print('Advanced:')
	print('Think of 3-D')
	print('Increment the crosstab')
	print('Basic:')

	print('51. Display total audience of each genre for all age groups in a new column "TT"')
	print("p.crosstab([f0f.genre,f0f.ranks,f0f.gender],f0f.age,margins=True,margins_name='TT')")

	print("52-a.Drop data for few genre's")
	print("cst.drop(['Childrens','Documentary','Film-Noir','Musical','Western'],level='genre',inplace=True)")
	print("52-b.Drop data for an age group")
	print("del cst['56']")

	print('53. Different kind of orders i.e. using genre or gender or agegroup')
	
	print('54. Best or Worst movie watched by gender and age group')
	
	print('55. Best or Worst movie watched by gender and age group for a selected genre')
	print('55-a. Normalize the entire frame')
	print("p.crosstab([f0f.genre,f0f.gender],f0f.age,normalize=True)")
	print('55-b. Normalize on the column values')
	print("p.crosstab([f0f.genre,f0f.gender],f0f.age,normalize='columns')")
	print('55-c. Normalize on the row values')
	print("p.crosstab([f0f.genre,f0f.gender],f0f.age,normalize='index')")
	return 0

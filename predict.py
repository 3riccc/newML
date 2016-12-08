#encoding:utf-8
def do(value,x_train,y_train):
	record = [0,0,0,0,0,0,0,0,0,0]
	for index,x in enumerate(x_train):
		caculateDistance(value,x)
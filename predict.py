#encoding:utf-8
# 核心函数：预测
def do(value,x_train,y_train,lableNum):
	# 平均数方法
	# record = [0,0,0,0,0,0,0,0,0,0]
	# for index,x in enumerate(x_train):
	# 	record[int(y_train[index])] += caculateDistance(value,x)
	# for i in range(len(record)):
	# 	record[i] = record[i] / lableNum[i]
	# record1 = sorted(record)
	# for i in range(len(record)):
	# 	if record[i] == record1[0]:
	# 		return i

	# 最邻近方法
	# 最短距离
	dis = 10000000
	# 最可能的数
	number = 0
	for index,x in enumerate(x_train):
		temp = caculateDistance(value,x)
		if temp < dis:
			dis = temp
			number = y_train[index]
	return number




# 计算距离的函数
def caculateDistance(vec0,vec1):
	# 曼哈顿距离
	dis = 0
	for i in range(len(vec0)):
		dis += abs(vec0[i]-vec1[i])
	return dis
# 绝对值函数
def abs(x):
	if x < 0:
		return (-1)*x
	else:
		return x
#encoding:utf-8
# 对二维数组归一化
def doAll(X):
	# 归一化参数
	para = [0.0,0.0,0.0,0.0,0.0,0.0]
	# 选取最大值，准备归一
	for vec in X:
		for i in range(len(vec)):
			if para[i] < vec[i]:
				para[i] = vec[i]
	# 开始归一
	for vec in X:
		for i in range(len(vec)):
			vec[i] = vec[i]/float(para[i])
	return X,para
# 对一维向量归一化
def doOne(vec,para):
	for i in range(len(vec)):
		vec[i] = vec[i]/float(para[i])
	return vec

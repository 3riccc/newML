#encoding:utf-8
# 获取训练样本
def getFile():
	import os
	fileList = os.listdir("./testDigits/")
	files = []
	lables = []
	for file in fileList:
		files.append(file)
		lables.append(file[0])
	return files,lables
# 训练集合测试集分开,接受参数为训练集样本比率
def getFileSeperate(rate):
	import os
	import random
	fileList = os.listdir("./testDigits/")
	filesTrain = []
	lablesTrain = []
	filesTest = []
	lablesTest = []
	for file in fileList:
		if random.random() < rate:
			filesTrain.append(file)
			lablesTrain.append(file[0])
		else:
			filesTest.append(file)
			lablesTest.append(file[0])
	return filesTrain,lablesTrain,filesTest,lablesTest
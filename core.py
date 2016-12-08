#encoding:utf-8
# 核心
import fillStructure as fs
# 文件操作
import operator
# 生成结构
import generateStructure as gs
# 生长
import grow as grow
# 评估
import assess as assess
# 获取训练原料
import getFiles as gf

# 获取样本并训练
filesTrain,Y_train,filesTest,Y_test = gf.getFileSeperate(0.8)


# 训练样本评估
X_train = []
for file in filesTrain:
	# 即将被填充的数组
	arr = []
	# 读取文件并填充到数组中
	f = open("testDigits/"+file);
	for line in f.readlines():
		# 去掉末尾的换行符
		line = line.strip("\n").strip("\r")
		# 每一行的数组
		row = []
		for letter in line:
			row.append(letter)
		arr.append(row)
	f.close()
	# 生成结构
	struct = gs.generate(len(arr))
	# 填充结构
	fs.fillStructure(arr,struct)
	# 生长
	struct = grow.grow(struct)

	# 评估结果
	X_train.append(assess.do(struct))
print len(X_train)




# 测试样本评估
X_test = []
for file in filesTest:
	# 即将被填充的数组
	arr = []
	# 读取文件并填充到数组中
	f = open("testDigits/"+file);
	for line in f.readlines():
		# 去掉末尾的换行符
		line = line.strip("\n").strip("\r")
		# 每一行的数组
		row = []
		for letter in line:
			row.append(letter)
		arr.append(row)
	f.close()
	# 生成结构
	struct = gs.generate(len(arr))
	# 填充结构
	fs.fillStructure(arr,struct)
	# 生长
	struct = grow.grow(struct)

	# 评估结果
	X_test.append(assess.do(struct))

# 训练和测试样本的归一化，以后做
# import normalization

# 查看精确度
import predict
# 正确和错误数量
right = 0
wrong = 0
for index,value in enumerate(X_test):
	res = predict.do(value,X_train,Y_train);
	if res == Y_test[index]:
		print "预测准确"
		right += 1
	else:
		print "错误：原为："+Y_test[index]+"，预测结果为："+res
print "准确率为"+ right/(right+wrong)
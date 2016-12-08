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
# 用训练结果预测
import predict
# 归一化
import normalization as norm


# 获取样本并训练
filesTrain,Y_train,filesTest,Y_test = gf.getFileSeperate(0.8)

# 生成结构
struct = gs.generate(32)
# 训练样本评估
X_train = []
for file in filesTrain:
	print "正在训练样本"+file
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
	struct = gs.clearStructure(struct)
	# 填充结构
	fs.fillStructure(arr,struct)
	# 生长
	struct = grow.grow(struct)

	# 评估结果
	X_train.append(assess.do(struct))


# 归一化
print "训练完毕，已训练样本"+str(len(X_train))+"个"
print "开始进行归一化..."
X_train,normPara = norm.doAll(X_train)

print "归一化完毕，开始进行数据测试..."

# 查看精确度

# 正确和错误数量
right = 0
wrong = 0
# 计算一下训练集中各类标签数量，过会会用到
lableNum = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(Y_train)):
	lableNum[int(Y_train[i])] += 1

print "训练完毕，开始对测试样本进行读取"
# 测试样本评估
X_test = []
for i in range(len(filesTest)):
	# 即将被填充的数组
	arr = []
	# 读取文件并填充到数组中
	f = open("testDigits/"+filesTest[i]);
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
	struct = gs.clearStructure(struct)
	# 填充结构
	fs.fillStructure(arr,struct)
	# 生长
	struct = grow.grow(struct)

	# 评估结果
	result = assess.do(struct)
	# 对评估结果归一化
	result = norm.doOne(result,normPara)
	# X_test.append(result)

	res = predict.do(result,X_train,Y_train,lableNum);
	if str(res) == str(Y_test[i]):
		print "读图正确"
		right += 1
	else:
		print "错误：原为："+str(Y_test[i])+"，预测结果为："+str(res)
		wrong += 1
print "全部样本数："+str(right+wrong)+"，读图正确数："+str(right)+"，读图错误数："+str(wrong)
print "准确率为："+ str(float(right)/(float(right)+float(wrong)))


# 训练和测试样本的归一化，以后做
# import normalization


# for index,value in enumerate(X_test):
# 	res = predict.do(value,X_train,Y_train,lableNum);
# 	if res == Y_test[index]:
# 		print "预测准确"
# 		right += 1
# 	else:
# 		print "错误：原为："+Y_test[index]+"，预测结果为："+res

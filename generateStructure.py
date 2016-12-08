#encoding:utf-8
# 生成结构
# 用于生成的函数，接受参数:一条边上的元素数量
def generate(x):
	# 高度
	height = 2 * x - 1;
	# 结果
	res = []
	# 第一层对象
	layer0 = {}
	# 生成第一层
	for i in range(x):
		for j in range(x):

			layer0[makeAxes(i,j,0)] = 0
	res.append(layer0)
	# 生成剩下的层
	for n in range(1,height):
		# 新生成的一层
		thisLayer = {}
		# 上一层
		lastLayer = res[n-1]
		# 奇数层，横着生成
		if n%2 == 1:
			for k,v in lastLayer.items():
				# 能和当前点共同激活下一层的点是否存在（也就是横坐标不变，纵坐标+1的点是否存在）
				x = getX(k)
				newY = getY(k) + 1
				z = getZ(k)
				if makeAxes(x,newY,z) in lastLayer:
					# 确认存在，就生成新的点
					newPoint = makeAxes(x,float(2*newY-1)/2,z+1)
					thisLayer[newPoint] = 0
		else:
			# 偶数层，纵向生成
			for k,v in lastLayer.items():
				# 这一层就纵着来，方法同上
				newX = getX(k)+1
				y = getY(k)
				z = getZ(k)
				if makeAxes(newX,y,z) in lastLayer:
					# 生成新的点
					newPoint = makeAxes((2*newX-1)/2,y,z+1)
					thisLayer[newPoint] = 0
		res.append(thisLayer)
	return res
# 从完整坐标中获取纵坐标
def getY(full):
	return float(full.split("-")[1])
# 从完整坐标中获取横坐标
def getX(full):
	return float(full.split("-")[0])
# 从完整坐标获取树坐标
def getZ(full):
	return float(full.split("-")[2])
# 用xyz生成坐标
def makeAxes(x,y,z):
	return str(float(x))+"-"+str(float(y))+"-"+str(float(z))
# 打印输出结果
def printRes(res):
	for index,layer in enumerate(res):
		print "第"+ str(index) +"层"

		print len(layer)
# 展示某一层
import sys
def showLayer(layer):
	# 获取所有单独坐标
	xs = []
	ys = []
	zs = []
	for k,v in layer.items():
		if getX(k) not in xs:
			xs.append(getX(k))
		if getY(k) not in ys:
			ys.append(getY(k))
	zs.append(getZ(k))
	# 排序
	xs = sorted(xs)
	ys = sorted(ys)
	# 展示
	for i in xs:
		for j in ys:
			if str(layer[makeAxes(i,j,zs[0])]) == "0" or str(layer[makeAxes(i,j,zs[0])]) == "2":
				sys.stdout.write(" ")
			else:
				sys.stdout.write(str(layer[makeAxes(i,j,zs[0])]))
		print "\n"
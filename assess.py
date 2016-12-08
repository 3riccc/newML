#encoding:utf-8
# 评估一个生长结果
# 引入自己写的模块
import generateStructure as gs
# 引入numpy用于计算方差和均值
import numpy as np
# 开始执行评估
def do(struct):
	# 由值为1的点的坐标组成的数组
	points = []
	for layer in struct:
		for k,v in layer.items():
			if v == "1":
				x = gs.getX(k)
				y = gs.getY(k)
				z = gs.getZ(k)
				# 将这些坐标收集起来
				points.append([x,y,z])
	# 横坐标，纵坐标，数坐标分开统计
	xs = []
	ys = []
	zs = []
	# 循环计入
	for point in points:
		xs.append(point[0])
		ys.append(point[1])
		zs.append(point[2])
	# 计算均值和方差
	xs = np.array(xs)
	ys = np.array(ys)
	zs = np.array(zs)
	# 计算并填入结果
	res = []
	res.append(xs.mean())
	res.append(ys.mean())
	res.append(zs.mean())
	res.append(xs.var())
	res.append(ys.var())
	res.append(zs.var())
	return res
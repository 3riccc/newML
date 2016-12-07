#encoding:utf-8
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
			layer0[""+str(i)+"-"+str(j)+""] = 0
	res.append(layer0)
	# 生成剩下的层
	for n in range(1,height):
		thisLayer = {}
		for i in range()
	return res
print generate(2)


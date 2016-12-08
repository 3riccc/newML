#encoding:utf-8
# 填充结构
import fillStructure as fs
# 文件操作
import operator
# 生成结构
import generateStructure as gs

# 即将被填充的数组
arr = []
# 读取文件并填充到数组中
f = open("testDigits/1_1.txt");
for line in f.readlines():
	# 去掉末尾的换行符
	line = line.strip("\n").strip("\r")
	# 每一行的数组
	row = []
	for letter in line:
		row.append(letter)
	arr.append(row)
# 生成结构
struct = gs.generate(len(arr))
# 填充结构
fs.fillStructure(arr,struct)


# 生长
def grow(struct):
	# 层数
	height = len(struct)
	# 每一层的循环,n代表层数，从零开始
	for n in range(height):
		# 一层中每个元素的循环，看看是否能生长
		print n
		if n%2 == 0:
			# 偶数层，横向生长
			for k,v in struct[n].items():
				if struct[n][k] == '1' or struct[n][k] == "2":
					# 获取这个元素的坐标
					x = gs.getX(k)
					y = gs.getY(k)
					z = gs.getZ(k)
					
					# 下一个点是否有值，有的话共同激活
					if gs.makeAxes(x,y+1,z) in struct[n] and str(struct[n][gs.makeAxes(x,y+1,z)]) != '0':
						print x,y,z
						# 激活下一层
						struct[n+1][gs.makeAxes(x,(2*y+1)/2,z+1)] = '1'
						# 改变自身状态
						struct[n][gs.makeAxes(x,y,z)] = '2'
						struct[n][gs.makeAxes(x,y+1,z)] = '2'
		else:
			# 奇数层，纵向生长
			for k,v in struct[n].items():
				if struct[n][k] == '1' or struct[n][k] == "2":
					# 获取这个元素的坐标
					x = gs.getX(k)
					y = gs.getY(k)
					z = gs.getZ(k)
					# 下一个点是否有值，有的话共同激活
					if gs.makeAxes(x+1,y,z) in struct[n] and str(struct[n][gs.makeAxes(x+1,y,z)]) != '0':
						# 激活
						struct[n+1][gs.makeAxes((2*x+1)/2,y,z+1)] = '1'
						# 改变自身状态
						struct[n][gs.makeAxes(x,y,z)] = '2'
						struct[n][gs.makeAxes(x+1,y,z)] = '2'
grow(struct)
for i in range(len(struct)):
	print "-----------------------------第"+str(i)+"层---------------------------------"
	gs.showLayer(struct[i])
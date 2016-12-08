# encoding:utf-8
# 填充结构
import operator
# 即将被填充的数组
arr = []
# 读取文件并填充到数组中
f = open("testDigits/0_0.txt");
for line in f.readlines():
	# 去掉末尾的换行符
	line = line.strip("\n").strip("\r")
	# 每一行的数组
	row = []
	for letter in line:
		row.append(letter)
	arr.append(row)
# 获取结构
import generateStructure as gs
struct = gs.generate(len(arr))
# 将数组填充到结构中
def fillStructure(arr,struct):
	# 边长
	side = len(arr)
	for i in range(side):
		for j in range(side):
			# 找到要填充的地方
			if arr[i][j] == '1':
				struct[0][gs.makeAxes(i,j,0)] = "1"
	return struct
fillStructure(arr,struct)
gs.showLayer(struct[0])
# encoding:utf-8
import generateStructure as gs
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
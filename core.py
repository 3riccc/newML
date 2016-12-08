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

# 即将被填充的数组
arr = []
# 读取文件并填充到数组中
f = open("testDigits/newtry.txt");
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
struct = grow.grow(struct)

# 评估结果
assessRes = []
assessRes = assess.do(struct)
print assessRes
# for i in range(len(struct)):
# 	print "-----------------------------第"+str(i)+"层---------------------------------"
# 	gs.showLayer(struct[i])
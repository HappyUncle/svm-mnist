#coding:utf8
#!/usr/bin/env python

import struct
import numpy as np
import matplotlib.pyplot as plt
import os

def read_image(filename, saveImage):
	
	#判断文件夹是否存在
	if not os.path.exists(saveImage):
		os.mkdir(saveImage)

	#读取文件内容
	f = open(filename, 'rb')
	buf = f.read()
	f.close()

	#解析文件内容
	index = 0
	#读取前四行
	magic, images, rows, columns = struct.unpack_from('>IIII' , buf , index)
	#偏移位置
	index += struct.calcsize('>IIII')

	#保存图片
	for i in range(images):
	
		im = struct.unpack_from('>784B', buf, index)
		index += struct.calcsize('>784B')
		im = np.array(im)
		im = im.reshape(28, 28)				
		
		plt.imsave(saveImage + '/' + str(i) + '.png', im)
		print 'save ' + str(i+1) + 'image'
	
	print 'save image finish'

def read_label(filename, saveFilename):

	#读入文件内容
	f = open(filename, 'rb')
	buf = f.read()
	f.close()

	#解析文件内容
	index = 0
	#读取前两行
	magic, labels = struct.unpack_from('>II' , buf , index)
	index += struct.calcsize('>II')

	labelArr = [0] * labels

	save = open(saveFilename, 'w')
	for x in range(labels):
		labelArr[x] = int(struct.unpack_from('>B', buf, index)[0])
		index += struct.calcsize('>B')

		save.write(str(labelArr[x]))
		save.write('\n')
		print 'write ' + str(x+1) + 'lable and the ans is ' + str(labelArr[x])
	save.close()

	print 'save labels finish'


if __name__ == '__main__':
	read_image('train_img', 'train_image')
	read_label('train_lab', 'train_lab.txt')
	read_image('test_img', 'test_image')
	read_label('test_lab', 'test_lab.txt')


#coding:utf8
#!/usr/bin/env python

import struct
import numpy as np

def read_image(filename):

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

	#保存数据到images
	imgList = [0] * images
	for i in range(images):
		im = struct.unpack_from('>784B', buf, index)
		index += struct.calcsize('>784B')
		im = np.array(im)
		imgList[i] = im;
		print 'load image ' + str(i+1)
	
	return imgList

def read_label(filename):

	#读入文件内容
	f = open(filename, 'rb')
	buf = f.read()
	f.close()

	#解析文件内容
	index = 0
	#读取前两行
	magic, labels = struct.unpack_from('>II' , buf , index)
	index += struct.calcsize('>II')

	#保存数据到labelList
	labelList = [0] * labels
	for x in range(labels):
		labelList[x] = int(struct.unpack_from('>B', buf, index)[0])
		index += struct.calcsize('>B')
		print 'load ' + str(x+1) + 'lable'
	
	return labelList

def saveFile(filename, images, labels):
	
	#打开文件
	fd = open(filename, 'w')
	line = len(images)
	for i in range(line):
		im = images[i]
		feature = ''
		for j in range(len(im)):
			feature += ' ' + str(j+1) + ':' + str(im[j]) 
		print 'write ' + str(i+1) + ' image to file'
		fd.write( str(labels[i]+1) + feature + '\n')
	
	fd.close()

	print 'save file success'

if __name__ == '__main__':
	trainImage = read_image('train_img')
	trainLabel = read_label('train_lab')	
	saveFile('train.dat', trainImage, trainLabel)

	testImage = read_image('test_img')
	testLabel = read_label('test_lab')
	saveFile('test.dat', testImage, testLabel)


# svm-mnist
use struct svm to learn mnist

# 说明
1. 本代码运行在Ubuntu16.04上
2. 使用的编程语言有：shell, Python 2.7, C
3. 训练样本图片为6w张，测试图片为1w张

# 使用步骤
1. 如果您没有mnist数据图片，请在data目录下，运行`downloadImage.sh` (实际上，train_lab,train_img,test_lab,test_img，就是下载好的数据集)
2. 然后执行`bin2img.py`，把下载到的二进制文件转换成`png`图片和label文本（可省略，此步骤只是用来形式化展示，没有什么积极意义）
3. 执行`bin2data.py`， 由于struct svm对数据格式有特定的要求，这一步不可省略
4. 在根目录下执行`run.sh`运行程序
```shell
./run.sh train #训练样本
./run.sh test #测试
````

# 补充
- 本人下载的是[SVM multiclass](http://www.cs.cornell.edu/People/tj/svm_light/svm_multiclass.html)源码
- 其实，源码是编译不过的，存在一些问题。
> 1. 在`Makefile`中，把`gcc`修改为`g++`
> 2. 在`svm_light`中添加`prloqo`文件夹，里面放的是`pr_loqo.h,pr_loqo.c`文件。（这个问题，[在官网有说明](http://www.cs.cornell.edu/People/tj/svm_light/index.html)，[下载链接](http://www.kernel-machines.org/code/prloqo.tar.gz)）
- 经过上面的修改就可以编译成功了





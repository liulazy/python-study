#注意：在开发时，应该把模块中的所有全局变量定义在
# 所有函数上方
#就可以保证所有的函数都能够正常的访问到每一个全局变量了
num=10

def demo():
    print("%d" % num)
    print("%s" % title)
#
title="黑马"
demo()

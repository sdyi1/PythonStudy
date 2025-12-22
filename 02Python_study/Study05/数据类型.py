
#如何理解图片的那句话

name="张三"

#这里获取的是name对应的数据的数据类型，而不是name这个变量的数据类型
#像java 我们创建变量是 String name = 张三   这个时候name这个变量的数据类型就固定是String了
s = type(name)
print(s)

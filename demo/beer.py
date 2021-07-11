# beer.py
import sys

n = 100
if sys.argv[1:]:
    n = int(sys.argv[1])

print(n)
## 「argv」是「argument variable」参数变量的简写形式，
## 一般在命令行调用的时候由系统传递给程序。这个变量其实是一个 List 列表，argv [0] 一般是被调用的脚本文件名或全路径，和操作系统有关，argv [1] 和以后就是传入的数据了。
## 作者：7sDream
## 链接：https://www.zhihu.com/question/23711222/answer/26173004

## sys.argv是什么？ - 磨斯的回答 - 知乎
## https://www.zhihu.com/question/23711222/answer/386159073

def bottle(n):
    if n == 0: return "no more bottles of beer"
    if n == 1: return "one bottle of beer"
    return str(n) + " bottles of beer"

for i in range(n, 0, -1):
    print(bottle(i), "on the wall,")
    print(bottle(i) + ".")
    print("Take one down, pass it around,")
    print(bottle(i-1), "on the wall.")

# range(start, stop[, step])


## 注意：用命令行指令在本文件目录中执行 $python beer.py 
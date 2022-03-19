import os,sys

# sys.path[0]、sys.argv[0]、os.getcwd()、os.path.abspath(__file__)、os.path.realpath(__file__)
# argv[0]：执行脚本运行时的绝对路径
print(sys.argv[0])
# sys.path[0]:执行脚本运行目录
print(sys.path[0])
# os.getcwd()同sys.path[0]
print(os.getcwd())
# os.path.abspath(__file__):脚本的绝对路径,__file__等于argv[0]
print(os.path.abspath(__file__))
print(os.path.abspath(sys.argv[0]))

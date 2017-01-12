from xmlrpc.client import ServerProxy

proxy = ServerProxy('http://localhost:8000/')
#a = proxy.file_reader('/tmp/secret.txt')

# 下面是windows的路径写法
a = proxy.file_reader('./WebSnapshot.py')
print(a) # 打印出文件内容
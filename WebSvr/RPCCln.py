from xmlrpc.client import ServerProxy

proxy = ServerProxy('http://localhost:8000/')
a = proxy.file_reader('./WebSnapshot.py')
print(a) # 打印出文件内容
import os
def mkdir(path):

    path=path.strip()

    path=path.rstrip("\\")
    path=os.path.abspath(path)

    isExists=os.path.exists(path)

    if not isExists:
        # 如果不存在则创建目录,创建目录操作函数
        '''
        os.mkdir(path)与os.makedirs(path)的区别是,当父目录不存在的时候os.mkdir(path)不会创建，os.makedirs(path)则会创建父目录
        '''
        #此处路径最好使用utf-8解码，否则在磁盘中可能会出现乱码的情况
        os.makedirs(path)

        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在

        return False

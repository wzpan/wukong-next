import os

def check_and_delete(fpath):
    """
    检查文件是否存在，并且删除该文件
    """
    if os.path.exists(fpath):
        os.remove(fpath)
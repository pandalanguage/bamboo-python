import os
from pathlib import Path

code = input("请输入您的代码文件名：")
with open(code, 'r') as f:
    data = f.readlines()[0]
    language = data.replace('#语言 = ', "")
    language = language.replace('\"', "")
    print(language)
    data = f.readlines()[0]
    import_package = data.replace('导入 ', "")
    pkg_status =os.popen('xhpkg status '+import_package)
    pkg_status = pkg_status.read()
    if pkg_status == 'not':
        print('正在安装'+import_package+'...')
        os.system('xhpkg install '+import_package)
        print('安装完成！')
    else:
        src_path = Path(code)
        dst_path = Path(os.getcwd()+'/temp/'+"python.py")
        src_path.copy(dst_path)
        data.replace('导入 '+import_package, pkg_status)
    
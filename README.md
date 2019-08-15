# cli mstsc

一个可以直接输入ip地址和用户名称及其密码来打开远程连接的命令行工具



## 使用

1. 去[发布页](https://github.com/cxwithyxy/mstsc/releases)下载程序
2. 用打开 **cmd**，**cd** 到 **cli_mstsc.exe** 目录下（要是把环境变量设置成该目录就不用这么麻烦了）
3. 键入命令 **cli_mstsc.exe ip地址 用户名 密码** 然后回车即可

例如:

```bat
cli_mstsc.exe 127.0.0.1 administrator abc12345
```



## 开发

> 注：建议使用 virtualenv ，虚拟环境能避免各种项目依赖包和系统的依赖包搞乱

#### 安装依赖

```
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

#### 打包EXE

```
pyinstaller index.spec
```
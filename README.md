# ClickX3 Pytest Template

## 安装依赖

```shell
python3 -m pip install poetry -i https://mirrors.aliyun.com/pypi/simple/
cd clickx3-toolkit/
python3 -m poetry install
```

## 虚拟环境添加myproject.pth

在目录`.cache/virtualenvs/xxx/Lib/site-packages/`下新增`myproject.pth`文件，内容如下：

```text
abs/path/to/project
```

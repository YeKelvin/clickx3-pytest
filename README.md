# ClickX3 Pytest Template

## 新建工作空间

选择一个喜欢的位置新建一个目录

```shell
mkdir xxx-uitest/
cd xxx-uitest/
# 克隆ui依赖库
git clone https://github.com/YeKelvin/clickx3-toolkit
# 克隆uitest模板
git clone https://github.com/YeKelvin/clickx3-pytest-template
```

## 安装依赖

```shell
python3 -m pip install poetry -i https://mirrors.aliyun.com/pypi/simple/
cd clickx3-pytest-template/
rm -rf .git/
python3 -m poetry install
```

## 虚拟环境添加myproject.pth

在`clickx3-pytest-template/.cache/virtualenvs/xxx/Lib/site-packages/`下新增`myproject.pth`文件，内容如下：

```text
absolute/path/to/clickx3-pytest-template/
```

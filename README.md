# Base编码自动解码脚本

## 简介
这是一个Python脚本，用于自动检测并解码base家族（base16, base32, base64, base85）的编码。脚本能够自动执行多轮解码，直至无法解码为止，适用于多层base编码的字符串。

## 功能
- 自动检测并解码base家族编码。
- 支持直接解码字符串或从文件中读取字符串进行解码。
- 能够处理多层base编码。

## 安装
无需安装，只需确保你的系统已安装Python。

## 使用方法

### 解码字符串
```bash
python base.py -m "SGVsbG8gV29ybGQh"
```
### 解码文件
```bash
python base.py -r 1.txt
```
## 注意
确保传递给 -m 的字符串或者文件中的内容是有效的base编码。
脚本会尝试所有支持的base编码方式，并返回最终解码结果。
## 支持的编码
base64
base32
base16
base85


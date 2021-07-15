# block-coordinate-split

将矿产资源勘查规划区块坐标数据拆分为单区域区块坐标数据。仅支持csv格式的输入和输出。


## 用法
修改代码中的输入参数：

```python
# 输入文件
INPUT_PATH = "./demo-input.csv"
# 输出文件
OUTPUT_PATH = "./output.csv"
# 唯一标识符字段
ID_FIELD = "A"
# 拐点数据字段
DATA_FIELD = "ZB"
# 新生成的唯一ID字段名，为空则不生成
GENERATED_ID = None
```

执行程序：
`python3 main.py`

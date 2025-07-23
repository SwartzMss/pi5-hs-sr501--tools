# pi5-hs-sr501--tools

本仓库提供树莓派 5 (Pi5) 搭配 HS-SR501 红外人体感应传感器的基本示例代码。

## 硬件连接
1. **VCC** 接树莓派 5 的 `5V` 供电引脚。
2. **GND** 接树莓派 5 的 `GND` 引脚。
3. **OUT** 接树莓派 5 的 `BCM 18` (物理引脚 12)，或根据需要选择其他 GPIO 引脚。

## 运行示例
确保系统中安装了 [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) 模块，然后执行：

```bash
python3 main.py [--pin GPIO编号]
```

其中 `--pin` 用于指定传感器 OUT 引脚连接的 BCM 编号，默认值为 `18`。
脚本会在终端中打印“Motion detected!”来表示检测到人体红外信号。


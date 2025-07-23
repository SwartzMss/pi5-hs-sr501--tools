# pi5-hs-sr501--tools

本仓库提供树莓派 5 (Pi5) 搭配 HS-SR501 红外人体感应传感器的基本示例代码。

<img src="doc/device.jpg" alt="Device" width="300" />

## 硬件连接
1. **VCC** 接树莓派 5 的 `5V` 供电引脚。
2. **GND** 接树莓派 5 的 `GND` 引脚。
3. **OUT** 接树莓派 5 的 `BCM 18` (物理引脚 12)，或根据需要选择其他 GPIO 引脚。

## 调节灵敏度
HS-SR501 模块板上带有用于设定探测范围和触发间隔的两个电位器。
标记为 `SENS` 的旋钮用于改变红外感应距离：
顺时针旋转时灵敏度增加，感应范围变大；逆时针则降低灵敏度。
另一枚 `TIME` 旋钮控制从检测到动作到再次可触发之间的延迟，
顺时针旋转延迟时间变长，逆时针缩短时间。

## 运行示例
确保系统中安装了 [gpiozero](https://pypi.org/project/gpiozero/) 模块（在官方 Raspberry Pi OS 中默认已提供），然后执行：

```bash
python3 main.py [--pin GPIO编号]
```

其中 `--pin` 用于指定传感器 OUT 引脚连接的 BCM 编号，默认值为 `18`。脚本会在终端中打印“Motion detected!”来表示检测到人体红外信号。

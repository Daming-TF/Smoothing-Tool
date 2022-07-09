# Data Smoothing Tool
```Introduction```:该项目主要演示三种不同数据平滑处理的操作

## Savitzky-Golay滤波
```问题描述```：在寻找曲线的波峰、波谷时，由于数据帧数多的原因，导致生成的曲线图噪声很大，不易寻找规律，处理前后对比如下：

![image](https://github.com/Daming-TF/Smoothing-Tool/blob/master/output/demo-SavGolFilter.jpg)

####运行演示
```angular2html
cd scripts
python demo_savitzky_golay.py
```

## 插值法

![image](https://github.com/Daming-TF/Smoothing-Tool/blob/master/output/demo-InterpFilter.jpg)

####运行演示
```angular2html
cd scripts
python demo_interpolate.py
```

## 滑动平均滤波

![image](https://github.com/Daming-TF/Smoothing-Tool/blob/master/output/demo-ConvolveFilter.jpg)

####运行演示
```angular2html
cd scripts
python demo_convolve.py
```
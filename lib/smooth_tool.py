import numpy as np
from scipy.signal import savgol_filter
from scipy.interpolate import make_interp_spline


# Savitzky Golay滤波器
class SavGolFilter:
    def __init__(self):
        print("This is >>Savitzky-Golay<< Smoothing Method")

    def __call__(self, x, y, window_length, k):
        """
        window_length越大平滑效果越明显，k越大和初始曲线越接近
        :param y: need smooth data
        :param window_length: smoothing window length(< data length)
        :param k: The order of the polynomial used to fit the samples
        :return: smoothed data
        """
        x_smooth = x
        y_smooth = savgol_filter(y, window_length, k, mode='nearest')

        return x_smooth, y_smooth


# 插值法
class InterpFilter:
    def __init__(self):
        print("This is >>Interpolation<< Smoothing Method")

    def __call__(self, x, y, num=None):
        """

        :param x: ——x(original data)
        :param y: need smooth data ——y(original data)
        :param num: Interpolation number
        :return: smoothed data
        """
        if num is None:
            if not isinstance(x, list):
                x = list(x)
            num = len(x) * 100
        x = np.array(x)
        x_smooth = np.linspace(x.min(), x.max(), num)
        y_smooth = make_interp_spline(x, y)(x_smooth)

        return x_smooth, y_smooth


# 滑动平均滤波
class ConvolveFilter:
    def __init__(self):
        print("This is >>Numpy.Convolve<< Smoothing Method")

    def __call__(self, x, y, window_length):
        """

        :param y: need smooth data ——y(original data)
        :param window_length: smoothing window length
        :return:
        """
        window = np.ones(int(window_length)) / float(window_length)
        x_smooth = x
        y_smooth = np.convolve(y, window, 'same')

        return x_smooth, y_smooth

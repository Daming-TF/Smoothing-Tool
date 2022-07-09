import numpy as np
import os
from lib.smooth_tool import ConvolveFilter
from lib.visualization_tool import VisTion


def main():
    x = np.linspace(-4, 4, 100)
    y = np.sin(x) + np.random.randn(len(x)) * 0.1

    my_plot = VisTion()
    my_filter = ConvolveFilter()

    # processing
    x_s, y_s = my_filter(x, y, 10)
    my_plot(x, y, label='Raw data')
    my_plot(x_s, y_s, label='Smooth data')
    my_plot.set_label('x label', 'y label', 'ConvolveFilter')
    my_plot.show(grid_flag=False, save_path=save_path)


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(path, r'../output/demo-ConvolveFilter.jpg')
    main()

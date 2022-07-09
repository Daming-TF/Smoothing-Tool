import numpy as np
import os
from lib.smooth_tool import InterpFilter
from lib.visualization_tool import VisTion


def main():
    x = np.array([6, 7, 8, 9, 10, 11, 12])
    y = np.array([1.53E+03, 5.92E+02, 2.04E+02, 7.24E+01, 2.72E+01, 1.10E+01, 4.70E+00])

    my_plot = VisTion()
    my_filter = InterpFilter()

    # processing
    x_s, y_s = my_filter(x, y, 300)
    my_plot(x, y, label='Raw data')
    my_plot(x_s, y_s, label='Smooth data')
    my_plot.set_label('x label', 'y label', 'InterpFilter')
    my_plot.show(grid_flag=False, save_path=save_path)


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(path, r'../output/demo-InterpFilter.jpg')
    main()

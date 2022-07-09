import numpy as np
import os
from lib.smooth_tool import SavGolFilter
from lib.visualization_tool import VisTion


def main():
    size = 100
    x = np.linspace(1, size, size)
    np.random.seed(0)
    y = np.random.randint(1, size, size)

    my_plot = VisTion()
    my_filter = SavGolFilter()        # M1

    # processing
    x_s, y_s = my_filter(x, y, 5, 3)      # M1-SavGolFilter
    my_plot(x, y, label='Raw data')
    my_plot(x_s, y_s, label='Smooth data')
    my_plot.set_label('x label', 'y label', 'SavGolFilter')
    my_plot.show(grid_flag=False, save_path=save_path)


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(path, r'../output/demo-SavGolFilter.jpg')
    main()

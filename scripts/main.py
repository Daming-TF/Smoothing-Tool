import numpy as np
from lib.smooth_tool import SavGolFilter, InterpFilter, ConvolveFilter
from lib.visualization_tool import VisTion


def main():
    size = 100
    x = np.linspace(1, size, size)
    np.random.seed(0)
    y = np.random.randint(1, size, size)

    my_plot = VisTion()
    # my_filter = SavGolFilter()    # M1
    # my_filter = InterpFilter()    # M2
    my_filter = ConvolveFilter()

    # processing
    # x_s, y_s = my_filter(x, y, 5, 3)      # M1-SavGolFilter
    # x_s, y_s = my_filter(x, y, 300)       # M2-InterpFilter
    x_s, y_s = my_filter(x, y, 10)
    my_plot(x, y, label='Raw data')
    my_plot(x_s, y_s, label='Smooth data')
    my_plot.set_label('x label', 'y label', 'Simple Test')
    my_plot.show(grid_flag=False)


if __name__ == '__main__':
    main()

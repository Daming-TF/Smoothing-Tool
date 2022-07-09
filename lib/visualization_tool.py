from matplotlib import pyplot as plt


class VisTion:
    def __init__(self):
        self._fig, self._ax = plt.subplots()

    def set_label(self, x_label, y_label, title_label):
        self._ax.set_xlabel(x_label)  # 设置x轴名称 x label
        self._ax.set_ylabel(y_label)  # 设置y轴名称 y label
        self._ax.set_title(title_label)  # 设置图名为Simple Plot

    def __call__(self, x, y, label):
        self._ax.plot(x, y, label=label)

    def show(self, grid_flag=True, save_path=None):
        self._ax.legend()  # 自动检测要在图例中显示的元素，并且显示
        plt.grid(grid_flag)
        if save_path is not None:
            plt.savefig(save_path)
        plt.show()


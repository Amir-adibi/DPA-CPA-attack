import matplotlib.pyplot as plt
import numpy as np

class Plot:

    def __init__(self, traces, plotting=True, number_of_samples=370_000, start_offset=44700, end_offset=330_300):
        self.traces = traces
        self.plotting = plotting

        self.number_of_samples = number_of_samples
        self.start_offset = start_offset
        self.end_offset = end_offset

    def plot(self):
        if self.plotting:
            y1 = np.array(self.traces[0])
            traces = y1.reshape((1, self.number_of_samples))
            x1 = np.arange(self.number_of_samples)
            fig = plt.figure(figsize=(19.2, 10.8))
            ax1 = fig.add_subplot(4, 1, 1)
            ax1.plot(x1, y1)

            y2 = y1[self.start_offset:self.start_offset+800]
            x2 = np.arange(self.start_offset, self.start_offset+800)
            ax2 = fig.add_subplot(4, 1, 2)
            ax2.plot(x2, y2)

            y3 = y1[self.end_offset-800:self.end_offset]
            x3 = np.arange(self.end_offset-800, self.end_offset)
            ax3 = fig.add_subplot(4, 1, 3)
            ax3.plot(x3, y3)

            plt.show()

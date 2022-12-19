import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


class Animate():
    def __init__(self):
        # Create figure for plotting
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = []
        self.ys = []
        self.readings = 30

    # This function is called periodically from FuncAnimation
    def _update(self,i):
        #temp_c = random.random()
        # Add x and y to lists
        self.xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        self.ys.append(random.random())

        # Limit x and y lists to 20 items
        self.xs = self.xs[-self.readings:]
        self.ys = self.ys[-self.readings:]

        # Draw x and y lists
        self.ax.clear()
        self.ax.plot(self.xs, self.ys)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        #self.ax.set_ylabel(self.sensor)

    def start(self):
        print('Starting')
        # Set up plot to call animate() function periodically
        self.anim = animation.FuncAnimation(self.fig, self._update,interval=50)
        plt.show()

if __name__ == "__main__":
    while True:
        rand = Animate()
        rand.start()


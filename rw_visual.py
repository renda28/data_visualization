import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:

    # change figure dimensions
    plt.figure(figsize=(10, 6))

    # Make a random walk and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(50000))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues, edgecolor='none', s=1)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='red', edgecolors='none', s=100)

    # Remove the axes.
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.axis('off')

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

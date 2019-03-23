import uuid

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import matplotlib as mpl


class Visualiser:
    def __init__(self, prefix=""):
        self.order = 0
        self.prefix = prefix
        pass

    def visualise_space(self, array, save=False):
        colors = ['white', 'black', 'orange', 'blue', 'green', 'purple', 'red', 'yellow', 'grey']
        bounds = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        cmap = mpl.colors.ListedColormap(colors)
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        im = plt.imshow(array, interpolation='none', cmap='Paired', norm=norm)
        values = np.unique(array.ravel())
        # get the colors of the values, according to the
        # colormap used by imshow
        colors = [im.cmap(im.norm(value)) for value in values]
        # create a patch (proxy artist) for every color
        patches = [mpatches.Patch(color=colors[i], label="Třída {l}".format(l=values[i])) for i in range(len(values))]
        # put those patched as legend-handles into the legend
        plt.legend(handles=patches, loc='upper center', bbox_to_anchor=(0.5, -0.05),
                   fancybox=True, shadow=True, ncol=len(values))

        plt.show()

        if save:
            plt.savefig("visualisations/" + self.prefix + str(self.order) + ".png")
            self.order += 1

    def visualise_probabilities(self, array, save=False):
        plt.imshow(array, interpolation="none")
        plt.colorbar()
        plt.show()

        if save:
            plt.savefig("visualisations/" + self.prefix + str(self.order) + ".png")
            self.order += 1
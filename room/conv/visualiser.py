import uuid

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


class Visualiser:
    def visualise_array(self, array, save=False):
        im = plt.imshow(array)
        values = np.unique(array.ravel())
        # get the colors of the values, according to the
        # colormap used by imshow
        colors = [im.cmap(im.norm(value)) for value in values]
        # create a patch (proxy artist) for every color
        patches = [mpatches.Patch(color=colors[i], label="Object {l}".format(l=values[i])) for i in range(len(values))]
        # put those patched as legend-handles into the legend
        plt.legend(handles=patches, loc='upper center', bbox_to_anchor=(0.5, -0.2),
                   fancybox=True, shadow=True, ncol=len(values))

        plt.show()

        if save:
            plt.savefig("visualisations/" + str(uuid.uuid4()) + ".png")

from keras.layers import Input, Dense
from keras.models import Model, Sequential
from keras.utils import plot_model
import numpy as np
from PIL import Image, ImageFile
from matplotlib.pyplot import imshow
from io import BytesIO

img = np.asarray(Image.open('model.png'))
rows = img.shape[0]
cols = img.shape[1]

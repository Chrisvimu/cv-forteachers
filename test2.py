import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage import io
from skimage import data
from skimage.filters import threshold_otsu, threshold_local, try_all_threshold
from matplotlib.backends.backend_pdf import PdfPages

image = io.imread('resources/imageimage.jpeg')

def test():
    n = try_all_threshold(image, figsize=(15, 8), verbose=False)
    
    return n

#plt.teste = try_all_threshold(image, figsize=(7, 8))

#plt.savefig(pp, format='pdf')
#fig.savefig('test.png')

#io.imsave('output.png', newimage)
#newimage.plt.savefig('foo.png')
#newimage.plt.savefig('foo.pdf')
#plt.savefig('foo.png')
#fig = plt.figure(newimage)
#test for the image


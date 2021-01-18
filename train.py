import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import keras
import pathlib
import PIL
from PIL import Image
from imgaug import augmenters as iaa
from keras.applications.xception import Xception
from keras.models import Model
import tensorflow as tf
from tensorflow.keras import layers
import tensorflow_datasets as tfds
import pandas as pd
from IPython.display import display

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
image_dir = os.path.join(BASE_DIR, "awe")

current_id = 0
label_ids = {}
y_labels = []
X_train = []
# iterate trough images
for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png"):
            path = os.path.join(root, file)
            label = os.path.basename(root)
            print(path, label)
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            print(label_ids)

            # y_labels # some number
            # x_train # verify this image and convert to gray
            pil_image = Image.open(path).convert("L")  # grayscale
            image_array = np.array(pil_image, "uint8")

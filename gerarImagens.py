#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
 
# definir caminhos da imagem original e diretório do output
IMAGE_PATH = "/home/weslley/Downloads/Projeto tcc/bike.jpg"
OUTPUT_PATH = "/home/weslley/Downloads/Projeto tcc/"
 
# carregar a imagem original e converter em array
image = load_img(IMAGE_PATH)
image = img_to_array(image)
 
# adicionar uma dimensão extra no array
image = np.expand_dims(image, axis=0)
 
# criar um gerador (generator) com as imagens do
# data augmentation
imgAug = ImageDataGenerator(rotation_range=0, width_shift_range=0.1,
                            height_shift_range=0.1, zoom_range=0.25,
                            fill_mode='nearest', horizontal_flip=True)
imgGen = imgAug.flow(image, save_to_dir=OUTPUT_PATH,
                     save_format='jpg', save_prefix='t27_')
 
# gerar 10 imagens por data augmentation
counter = 0
for (i, newImage) in enumerate(imgGen):
    counter += 1
 
    # ao gerar 10 imagens, parar o loop
    if counter == 10:
        break


# In[ ]:





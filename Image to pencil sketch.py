#!/usr/bin/env python
# coding: utf-8

# # Lets Grow More(LGMVIP)
# ## Task 4: Image to Pencil sketch with Python
# ### Author: Omkar Sanjay Chavan

# In[1]:


pip install opencv-python


# In[2]:


import cv2
from PIL import Image
from IPython.display import display


# ### Reading image in RGB format

# In[3]:


image=cv2.imread("D:\Omkar\download.jpeg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
display(Image.fromarray(image))


# ### Convert the original image to greyscale

# In[4]:


gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
display(Image.fromarray(gray_image))


# In[ ]:





# In[5]:


inverted_image=cv2.bitwise_not(gray_image)
display(Image.fromarray(inverted_image))


# ### Convert negative image to blurry image

# In[6]:


blurred_image=cv2.GaussianBlur(inverted_image,(21,21),0)
display(Image.fromarray(blurred_image))


# In[7]:


inverted_blurred=cv2.bitwise_not(blurred_image)
pencil_sketch=cv2.divide(gray_image,inverted_blurred,scale=250.0)
display(Image.fromarray(pencil_sketch))


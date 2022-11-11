# Study-on-Low-Light-Enhancement-Machine-Learning-Method-

In this repository, we investigate the data-driven method (machine learning) for implementing low-light image enhancement. We first employ a dehazing algorithm [1][2] to remove haze in the inverted image. We then invert the image once again to gain the image with regular exposure. Notably, many deep learning methods merely handle homogeneous dehazing problems. In [1], the authors adopt a two-branch neural network to realize ***ensemble learning***, which can engage nonhomogeneous dehazing issues. Hence, the performance of dehazing is improved. We utilize [1] and invert low-light images to enhance the low-light image. The result below shows the algorithm is valid. 


![33](https://user-images.githubusercontent.com/108604868/201390433-c129e7df-601c-41a0-84c6-81f518ab626b.jpg)

![8](https://user-images.githubusercontent.com/108604868/201390376-13586cc9-e1cb-4dfb-862e-adf7cbc5b5a1.png)


# Reference
[1] Yankun Yu, Huan Liu, Minghan Fu, Jun Chen, Xiyao Wang, and Keyan Wang, A Two-branch Neural Network for Non-homogeneous Dehazing via Ensemble Learning, 2021.  
[2] [liuh127/NTIRE-2021-Dehazing-Two-branch](https://github.com/liuh127/NTIRE-2021-Dehazing-Two-branch)

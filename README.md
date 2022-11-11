# Study-on-Low-Light-Enhancement-Machine-Learning-Method-

In 

在本 repository 中，我們探討利用data driven based machine learning 方法 來實現低光源增強演算法。我們的主要的演算步驟是利用 dehazing 演算法 來將低光源的負片影像做去haze，接著再做一次負片來得到增加曝光的影像。 值得一提的是，大部分deep learning 的 dehazing 演算法 只能針對 homogeneous dehazing problem 做處理。而在 [?]中，作者透過two-branch neural network 來實現ensemble learning。此種方式可以應付 nonhomogeneous dehazing problem，使得dehazing 的性能可以提升。我們將此演算法與負片做結合，可以得到低光源增強效果。結果顯示非常好。 


在此，我們利用 dehazing 演算法 [3] 來將負片中黑色部分



![33](https://user-images.githubusercontent.com/108604868/201390433-c129e7df-601c-41a0-84c6-81f518ab626b.jpg)

![8](https://user-images.githubusercontent.com/108604868/201390376-13586cc9-e1cb-4dfb-862e-adf7cbc5b5a1.png)


# Reference
[1] Yankun Yu, Huan Liu, Minghan Fu, Jun Chen, Xiyao Wang, and Keyan Wang, A Two-branch Neural Network for Non-homogeneous Dehazing via Ensemble Learning, 2021.  
[2] [liuh127/NTIRE-2021-Dehazing-Two-branch](https://github.com/liuh127/NTIRE-2021-Dehazing-Two-branch)

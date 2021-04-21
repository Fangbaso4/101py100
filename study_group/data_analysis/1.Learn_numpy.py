#!/usr/bin/env python
# coding: utf-8

# In[76]:


import numpy as np
from matplotlib import pyplot as plt 


# In[13]:


# task1 用 numpy 创建一个 2 * 2 的二维数组 ndarray，指定元素类型为 float，命名为 arr1
arr1 = np.array([[1,2],[3,4]], dtype=float)
arr1


# In[36]:


# q2 生成元素全为 0 的 6 * 6 矩阵 arr2；元素全为 1 的 6 * 6 矩阵 arr3；以及 6 * 6 的单位矩阵 arr4
arr2 = np.zeros((6,6))
arr3 = np.ones_like(arr2)  
arr4 = np.eye(5,dtype=int)
arr4


# In[38]:


# np.arange(10, 20).reshape((2, 5))  
# np.empty((6, 6))


# In[41]:


# q3 运用 arange 函数生成生成 [0, 10) 区间内，步长为 2 的整数序列 arr5
arr5 = np.arange(0, 10, 2)
arr5


# In[49]:


# q4 生成 0~10 间的等差数列 arr6，元素个数为 6
arr6 = np.linspace(0,10,6,dtype=int)
arr6


# In[61]:


# q5 创建一个长度为 10 的随机数组（每个元素都是整数）并将最大值替换为 0
arr7 = np.random.randint(1,100,[1,10])
print(arr7)
print(arr7.argmax())
arr7[0][arr7.argmax()]


# In[68]:


# q6 计算数组 x = np.array([1,2,3,2,3,4,3,4,5,6]) 和数组 y = np.array([7,2,10,2,7,4,9,4,9,8]) 之间的欧式距离
x = np.array([1,2,3,2,3,4,3,4,5,6]) 
y = np.array([7,2,10,2,7,4,9,4,9,8])
# 欧氏距离直白写法
dist = np.sqrt(np.sum(np.square(x - y)))
print(dist)
# 内置函数求欧式距离
dist1 = np.linalg.norm(x - y)
dist1


# 欧式距离公式：
# $$
# dist(X,Y)=\sqrt{\sum_{i=1}^n(x_i-y_i)^2}
# $$

# In[81]:


# q7 利用 seed 生成一组固定的随机数 np.random.seed(1) ，并用此组成模拟的资金价值曲线 values = np.random.randn(1000).cumsum()

np.random.seed(1)
values = np.random.randn(1000).cumsum()
values
# 请利用 matplotlib 作出该资金价值曲线图
y =  values
x = np.arange(0, 1000)
plt.plot(x,y) 
plt.show()


# In[85]:


# q8 计算 任务7 中资金价值的最大回撤 https://blog.csdn.net/weixin_38997425/article/details/82915386
max_drawdown = np.max(np.maximum.accumulate(values) - values)
max_drawdown


# 最大回撤计算公式：
# $$
# d = \mathop{min}\limits_{i\leq j}(x_j - x_i) = \mathop{min}\limits_{j}(x_j - \mathop{max}\limits_{i\leq j}x_i)
# $$

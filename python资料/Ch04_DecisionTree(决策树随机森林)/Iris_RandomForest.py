#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@创建日期：2017.8.11

@作者: 李军
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


iris_feature_E = 'sepal length', 'sepal width', 'petal length', 'petal width'
iris_feature = u'花萼长度', u'花萼宽度', u'花瓣长度', u'花瓣宽度'
iris_class = 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica'


if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    data = pd.read_csv('iris.data', header=None)
    x = data[range(4)]
    y = pd.Categorical(data[4]).codes   #将字符串转数字
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, random_state=1)
    
    # 随机森林参数估计 n_estimators:决策树的个数至少100左右
    model = RandomForestClassifier(n_estimators=10, criterion='gini', min_samples_split=5, min_samples_leaf=10)
    model.fit(x_train, y_train)
    y_pred_train = model.predict(x_train)    # 训练数据预测
    y_pred_test = model.predict(x_test)      # 测试数据预测
    acc_train = np.mean(y_pred_train == y_train)
    acc_test = np.mean(y_pred_test == y_test)
    print '训练数据预测准确度: %.2f%%' % (100 * acc_train)
    print '测试数据预测准确度: %.2f%%' % (100 * acc_test)
    
    
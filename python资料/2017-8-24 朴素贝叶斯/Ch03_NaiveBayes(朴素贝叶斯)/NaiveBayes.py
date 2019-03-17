# -*- coding: utf-8 -*-


import os
import numpy as np
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB

#数据预处理
def make_Dictionary(train_dir):
    emails = [os.path.join(train_dir, f) for f in os.listdir(train_dir)]    
    all_words = []       
    for mail in emails:    #遍历所有文件
        with open(mail) as m:
            for i, line in enumerate(m):
                    words = line.split()
                    for j in words:
                        if j.isalpha() == True and len(j)>1:   #去掉不是单词或标点符号
                            all_words.append(j)
    
    dictionary = Counter(all_words)  #统计每个单词的数量
    dictionary = dictionary.most_common(100)   #取top100单词
    return dictionary
    
#构造训练样本矩阵
def extract_features(mail_dir): 
    files = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    features_matrix = np.zeros((len(files), 100))   #初始化 文件个数行 * 100列（因为上面取了100个关键单词） 的矩阵
    docID = 0;
    for fil in files:
      with open(fil) as fi:
        for i, line in enumerate(fi):
            words = line.split()
            for word in words:
              wordID = 0
              for i, d in enumerate(dictionary):
                if d[0] == word:
                  wordID = i
                  features_matrix[docID, wordID] = words.count(word) #索引「ij」处的值将是第 i 个文件中词典的第 j 个词的出现次数
        docID = docID + 1     
    return features_matrix

if __name__ == "__main__":
    train_dir = 'data\\part1'   #训练数据文件
    dictionary = make_Dictionary(train_dir)
    train_labels = np.zeros(289)  #默认对289个文件都标注为0
    train_labels[241:] = 1   #样本标记类别1到241个文件是正常邮件，标记为0；242到289个文件是垃圾邮件，标记为1
    train_matrix = extract_features(train_dir)  #构造训练样本矩阵
    
    #model = MultinomialNB()  #多项式朴素贝叶斯模型
    #model = BernoulliNB()   #伯努利朴素贝叶斯模型
    model = GaussianNB()   #高斯朴素贝叶斯模型
    model.fit(train_matrix, train_labels)  #样本训练
    
    test_dir = 'data\\part2'   #测试数据文件
    test_labels = np.zeros(289)
    test_labels[241:] = 1
    test_matrix = extract_features(test_dir)   #构造测试样本矩阵
    
    test_result = model.predict(test_matrix)    #预测测试样本
    #train_result = model.predict(train_matrix)    #预测训练样本
    print(test_labels)
    print(test_result)
    #print('训练样本准确度：%.2f%%' % (100*np.mean(train_result == train_labels)))
    print('测试样本准确度：%.2f%%' % (100*np.mean(test_result == test_labels)))
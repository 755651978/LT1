import numpy as np
import smallworld as sw
import networkx as nx
import matplotlib.pyplot as plt

#邻接矩阵
a = sw.a
#节点度数, 1/b是其他节点对该节点的影响力
b = sw.b
#节点阀值
beta = sw.beta
#原激活节点
origin = sw.origin

#超过beta（如50%）的邻接节点处于激活状态，该节点才会进入激活状态

def lt_(a, b, origin, beta):
    #节点数
    n = a.shape[0]
    #控制符
    judge = 1
    #未激活节点
    s = np.arange(n)
    s = np.delete(s, origin)
    #激活节点
    i = origin
    while judge == 1:
        #该轮激活节点
        temp_i = []
        #激活节点个数
        m = len(i)
        for j in range(0, m):
            node = int(i[j])
            asd = []
            for k in range(0, n):
                if a[node, k] == 1:
                    asd.append(k)
            #找到相邻的未激活节点
            asd2 = np.intersect1d(asd, s)
            asd_final = []
            for k in range(0,len(asd2)):
                num = 0
                #该未激活节点相邻的激活节点个数
                for t in range(0, m):
                    if a[int(i[t]), asd2[k]] == 1:
                        num = num + 1
                if 1 / b[asd2[k]] * num >= beta:
                    asd_final.append(asd2[k])
            temp_i = np.union1d(temp_i, asd_final)
            s = np.setdiff1d(s, asd_final)
        #将新激活节点合并到原激活节点中
        i = np.union1d(i, temp_i)
        #如果该轮没有新激活节点，那之后都不会再有，跳出循环
        if len(temp_i) == 0:
            judge = 0
    #输出新的网络状况
    color = []
    for j in range(0, n):
        color.append('b')
    for j in range(0, len(i)):
        color[int(i[j])] = 'r'
    g = nx.from_numpy_matrix(a)
    nx.draw(g, with_labels=True, node_color=color)
    plt.show()


lt_(a, b, origin, beta)
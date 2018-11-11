'''

分类器
特征选择测试

author:Kris_goGOzZZ

'''
import os
import copy
import math
import jieba
import re
from operator import itemgetter


Temp = []
temp = ""
trainingSet = []
historyClassifierText = []
classifierWords = []
typeClassifierText = []
classifierDictionary1 = []
classifierDictionary2 = []
classifierDictionary3 = []
classifierDictionary4 = []
classifierDictionary5 = []
classifierDictionary = []


def progress_bar(num,k):
 
    q1 = "#"; q2 = "=";
 
 
 
    q1 += "#"; q2 += "="; s = ("█" * int(k/288)) + ("▓" * int(num - k/288))
    os.system('cls')
    #print(int(i/num*100), end='%\r')
    #print('%.2f' % (i/num*100), end='%\r')
    #print('%.2f' % (i*100/num), end='%\r')
    #print('complete percent:', time.strftime("%Y-%m-%d %H:%M:%S", \
    #        time.localtime()), int((i/num)*100), end='%\r')
    #print(str(int(i/num*100)) + '% ' + j + '->', end='\r')
    #print(k + ">" + str(int(i/num*100)), end='%\r')
    #print("[%s]" % t[i%4], end='\r')
    #print("[%s][%s][%.2f" % (t[i%4], k, (i/num*100)), "%]", end='\r')
    print("\n"*12+"[学习进度][%s][%.2f" % ( s, (int(k/288)/num*100)), "%]", end='\r')
 
 
    print()



for i in range(50):
    file = open("classifier_text\\training"+str(i+1)+".txt",'r')
    trainingSet.append(file.read())
    trainingSet[i] = trainingSet[i].strip()
    trainingSet[i] = trainingSet[i].split('。')
    for j in range(len(trainingSet[i])):
        trainingSet[i][j] = trainingSet[i][j].strip()
        Temp = (re.findall(r"[\w’]+",trainingSet[i][j]))
        for u in range(len(Temp)):
            temp += Temp[u]
            trainingSet[i][j] = temp
#        print(trainingSet[i][j])
        temp = ""
        Temp = []
        trainingSet[i][j] = jieba.lcut(trainingSet[i][j])
    if [] in trainingSet[i]:
        trainingSet[i].remove([])


    #if trainingSet[i][0][0] == '体育' :
    for j in range(1,len(trainingSet[i])):
        #if trainingSet[i][j][0] != '体育':
        trainingSet[i][j].insert(0,trainingSet[i][0][0])
    file.close()    
#        print(trainingSet[i][j])
    #if trainingSet[i][0][0] == '历史' :
      #  for j in range(len(trainingSet[i])):
       #     if trainingSet[i][j][0] != '历史':
        #        trainingSet[i][j].insert(0,'历史')

#print(trainingSet)

Temp = [item for sublist in trainingSet for item in sublist]
trainingSet = Temp
Temp = []

#print(trainingSet)

file = open('dictionary.txt','w')
for i in range(len(trainingSet)):
    for j in range(len(trainingSet[i])):
        file.write(trainingSet[i][j]+'\t')
    file.write("\n")
file.close()
def reCW():
    for i in range(len(trainingSet)):
        for j in range(1,len(trainingSet[i])):
            if trainingSet[i][j] not in classifierWords:
                classifierWords.append(trainingSet[i][j])

#print(classifierWords)
#print(len(classifierWords))
'''
        if trainingSet[i][0] == '历史':
            if trainingSet[i][j] not in historyClassifierWords:
                historyClassifierWords.append(trainingSet[i][j])
        if trainingSet[i][0] == '体育':
            if trainingSet[i][j] not in sportClassifierWords:
                sportClassifierWords.append(trainingSet[i][j])
'''
'''
for i in range(len(trainingSet)):
    for j in range(1,len(trainingSet[i])):
        if trainingSet[i][0] == type_:
            if trainingSet[i][j] not in typeClassifierText:
                typeClassifierText.append(trainingSet[i][j])
                '''
#print(historyClassifierWords)
#print(sportClassifierWords)

#print(trainingSet)
def MI(type_):
    '''
    classifierWords[i] = [word,N00,N01,N10,N11]
    '''

    #print(1)
    typeClassifierText = []
    print(type_)
    for i in range(len(trainingSet)):
        for j in range(1,len(trainingSet[i])):
            if trainingSet[i][0] == type_:
                if trainingSet[i][j] not in typeClassifierText:
                    typeClassifierText.append(trainingSet[i][j])

    
#    print(len(typeClassifierText))
#    print(len(classifierWords))

    trainingSet2 = copy.deepcopy(trainingSet)
    for i in range(len(trainingSet2)):
        del trainingSet2[i][0]

    for k in range(len(classifierWords)):
        num1 = 0
        num2 = 0
        num3 = 0
        num4 = 0
        if k % 100 == 1:
            progress_bar(int(len(classifierWords)/288),k)
        #print(classifierWords[k])
        for i in range(len(trainingSet)):
            if trainingSet[i][0] != type_:
                if classifierWords[k] not in trainingSet2[i]:
                    num1 += 1
                if classifierWords[k] in trainingSet2[i]:
                    num3 += 1
            else:
                if classifierWords[k] not in trainingSet2[i]:
                    num2 += 1
                if classifierWords[k] in trainingSet2[i]:
                    num4 += 1
        #print(num1,num2,num3,num4)
        classifierWords[k] = [classifierWords[k],num1+1,num2+1,num3+1,num4+1]#平滑

    return


'''
num1 = 0
num2 = 0
num3 = 0
num4 = 0
for i in range(len(trainingSet)):
            if trainingSet[i][0] != '历史':
                if classifierWords[8] not in trainingSet[i]:
                    num1 += 1
                if classifierWords[8] in trainingSet[i]:
                    num2 += 1
            else:
                if classifierWords[8] not in trainingSet[i]:
                    num3 += 1
                if classifierWords[8] in trainingSet[i]:
                    num4 += 1
print(classifierWords[8])
print(num1,num2,num3,num4)
'''
#print(classifierWords)

def IUC():
    '''
    I(U;C) = N11/Nlog2(NN11/N1.N.1) + N01/Nlog2(NN01/N0.N.1) + N10/Nlog2(NN10/N1.N.0) + N00/Nlog2(NN00/N0.N/0)
    '''
    for i in range(len(classifierWords)):
        sum = classifierWords[i][1]+classifierWords[i][2]+classifierWords[i][3]+classifierWords[i][4]
        classifierWords[i] = [classifierWords[i][0],classifierWords[i][1]/sum * math.log(sum*classifierWords[i][1]/
                                                                                            (classifierWords[i][1]+classifierWords[i][2])/(classifierWords[i][1]+classifierWords[i][3]))
        +classifierWords[i][2]/sum * math.log(sum*classifierWords[i][2]/
                                              (classifierWords[i][1]+classifierWords[i][2])/(classifierWords[i][2]+classifierWords[i][4]))
        +classifierWords[i][3]/sum * math.log(sum*classifierWords[i][3]/
                                              (classifierWords[i][1]+classifierWords[i][3])/(classifierWords[i][3]+classifierWords[i][4]))
        +classifierWords[i][4]/sum * math.log(sum*classifierWords[i][4]/
                                              (classifierWords[i][4]+classifierWords[i][2])/(classifierWords[i][3]+classifierWords[i][4]))]


#classifierWords = []
#reCW()
#MI("体育")
#IUC()
#classifierWords = sorted(classifierWords,key = itemgetter(1),reverse=True)

#print(len(classifierWords))
classifierWords = []
reCW()
MI("体育")
print(classifierWords)
IUC()
classifierWords = sorted(classifierWords,key = itemgetter(1),reverse=True)
print(classifierWords)
'''

classifierWords = []
reCW()
MI("体育")
IUC()
classifierWords = sorted(classifierWords,key = itemgetter(1),reverse=True)
i = 0
while True:
    if classifierWords[i][0] not in classifierDictionary1:
        classifierDictionary1.append(classifierWords[i][0])
        i += 1
    if i >= 500:
        break
classifierWords = []
reCW()
MI("历史")
IUC()
classifierWords = sorted(classifierWords,key = itemgetter(1),reverse=True)
i = 0
while True:
    print(1)
    if classifierWords[i][0] not in classifierDictionary2:
        classifierDictionary2.append(classifierWords[i][0])
        i += 1
        print(2)
    if i >= 500:
        break
classifierWords = []
reCW()
MI("音乐")
IUC()
classifierWords = sorted(classifierWords,key = itemgetter(1),reverse=True)
i = 0
while True:
    if classifierWords[i][0] not in classifierDictionary3:
        classifierDictionary3.append(classifierWords[i][0])
        i += 1
    if i >= 500:
        break
classifierWords = []
reCW()
MI("时尚")
IUC()
classifierWords = sorted(classifierWords,key = itemgetter(1),reverse=True)
i = 0
while True:
    if classifierWords[i][0] not in classifierDictionary4:
        classifierDictionary4.append(classifierWords[i][0])
        i += 1
    if i >= 500:
        break
classifierWords = []
reCW()
MI("游戏")
IUC()
classifierWords = sorted(classifierWords,key = itemgetter(1),reverse=True)
i = 0
while True:
    if classifierWords[i][0] not in classifierDictionary5:
        classifierDictionary5.append(classifierWords[i][0])
        i += 1
    if i >= 500:
        break

classifierDictionary = classifierDictionary1+classifierDictionary2+classifierDictionary3+classifierDictionary4+classifierDictionary5

'''
'''
file = open('feature_selection_music.txt','w')
for i in range(len(classifierWords)):
    file.write(classifierWords[i][0]+'\t')
    file.write(str(classifierWords[i][1])+'\n')
file.close()
'''

#file = open('feature_selection_dictionary.txt','w+')
'''
file = open('features.txt','w')
for i in range(len(classifierDictionary)):
    file.write(classifierDictionary[i]+'\n')
file.close()

'''





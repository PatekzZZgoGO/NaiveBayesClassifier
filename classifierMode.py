'''

分类器创建


author:Kris_goGOzZZ

'''
import copy
import math
import jieba
import re
from operator import itemgetter

trainingSet = []
classifier = []
i = 0
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0

file = open('dictionary.txt','r')
while True:
    trainingSet.append(file.readline())
    if trainingSet[-1] == "":
        del trainingSet[-1]
        break
    trainingSet[i] = trainingSet[i].strip()
    trainingSet[i] = trainingSet[i].split('\t')
    i += 1
#print(trainingSet)
file.close()

file = open('features.txt','r')
i = 0
while True:
    classifier.append(file.readline())
    if classifier[-1] == "":
        del classifier[-1]
        break
    classifier[i] = classifier[i].strip()
    i += 1
file.close()
#print(classifier)

for i in range(len(classifier)):
    classifier[i] = [classifier[i],0,0,0,0,0]
#print(classifier)

#print(trainingSet)
def ClasssifierCount():
    '''

    [词，体育，历史，游戏，时尚，音乐]

    '''
    for i in range(len(classifier)):
        for j in range(len(trainingSet)):
            for k in range(1,len(trainingSet[j])):
                if trainingSet[j][k] == classifier[i][0]:
                    if trainingSet[j][0] == '体育':
                        classifier[i][1] += 1
                    if trainingSet[j][0] == '历史':
                        classifier[i][2] += 1
                    if trainingSet[j][0] == '游戏':
                        classifier[i][3] += 1
                    if trainingSet[j][0] == '时尚':
                        classifier[i][4] += 1
                    if trainingSet[j][0] == '音乐':
                        classifier[i][5] += 1
        classifier[i][1] += 1
        classifier[i][2] += 1
        classifier[i][3] += 1
        classifier[i][4] += 1
        classifier[i][5] += 1



ClasssifierCount()

for i in range(len(classifier)):
    sum1 += classifier[i][1]
    sum2 += classifier[i][2]
    sum3 += classifier[i][3]
    sum4 += classifier[i][4]
    sum5 += classifier[i][5]


for i in range(len(classifier)):
    classifier[i][1] = math.log(classifier[i][1]/sum1)
    classifier[i][2] = math.log(classifier[i][2]/sum2)
    classifier[i][3] = math.log(classifier[i][3]/sum3)
    classifier[i][4] = math.log(classifier[i][4]/sum4)
    classifier[i][5] = math.log(classifier[i][5]/sum5)

#print(classifier)
'''
file = open('classifier.txt','w')
for i in range(len(classifier)):
    for j in range(len(classifier[i])):
        file.write(str(classifier[i][j])+'\t')
    file.write('\n')
file.close()

'''

text = input("请输入test语句:\n")
text = text.strip()
text = jieba.lcut(text)
print(text)


conditionalP1 = 0
conditionalP2 = 0
conditionalP3 = 0
conditionalP4 = 0
conditionalP5 = 0
prioriP1 = 0
prioriP2 = 0
prioriP3 = 0
prioriP4 = 0
prioriP5 = 0
P1 = 0
P2 = 0
P3 = 0
P4 = 0
P5 = 0
print(classifier)
tempList = []
temp = 0
for i in range(len(classifier)):
    tempList.append(classifier[i][0])
print(tempList)
for i in range(len(text)):
    print(text[i])
    if text[i] in tempList:
        temp = tempList.index(text[i])
        print(temp)
        conditionalP1 += classifier[temp][1]
        conditionalP2 += classifier[temp][2]
        conditionalP3 += classifier[temp][3]
        conditionalP4 += classifier[temp][4]
        conditionalP5 += classifier[temp][5]

'''
prioriP1 = sum1/(sum1+sum2+sum3+sum4+sum5)
prioriP2 = sum2/(sum1+sum2+sum3+sum4+sum5)
prioriP3 = sum3/(sum1+sum2+sum3+sum4+sum5)
prioriP4 = sum4/(sum1+sum2+sum3+sum4+sum5)
prioriP5 = sum5/(sum1+sum2+sum3+sum4+sum5)


P1 = prioriP1*conditionalP1
P2 = prioriP2*conditionalP2
P3 = prioriP3*conditionalP3
P4 = prioriP4*conditionalP4
P5 = prioriP5*conditionalP5
'''
print(str(conditionalP1)+'\n'+str(conditionalP2)+'\n'+str(conditionalP3)+'\n'+str(conditionalP4)+'\n'+str(conditionalP5)+'\n')

resultList = [conditionalP1,conditionalP2,conditionalP3,conditionalP4,conditionalP5]
resultList.sort()

if resultList[-1] == conditionalP1:
    print('体育')
if resultList[-1] == conditionalP2:
    print('历史')
if resultList[-1] == conditionalP3:
    print('游戏')
if resultList[-1] == conditionalP4:
    print('时尚')
if resultList[-1] == conditionalP5:
    print('音乐')
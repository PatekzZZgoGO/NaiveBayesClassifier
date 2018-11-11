'''

分类器


author:Kris_goGOzZZ

'''


import math
import jieba

trainingSet = []
classifier = []
i = 0
file = open('classifier.txt','r')
while True:
    classifier.append(file.readline())
    if classifier[-1] == "":
        del classifier[-1]
        break
    classifier[i] = classifier[i].strip()
    classifier[i] = classifier[i].split('\t')
    for j in range(1,6):
        classifier[i][j] = float(classifier[i][j])
    i += 1
file.close()

#print(classifier)

file = open('dictionary.txt','r')
i = 0
while True:
    trainingSet.append(file.readline())
    if trainingSet[-1] == "":
        del trainingSet[-1]
        break
    trainingSet[i] = trainingSet[i].strip()
    trainingSet[i] = trainingSet[i].split('\t')
    i += 1
file.close()

#print(trainingSet)
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0

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
for i in range(len(trainingSet)):
    if trainingSet[j][0] == '体育':
        sum1 += 1
    if trainingSet[j][0] == '历史':
        sum2 += 1
    if trainingSet[j][0] == '游戏':
        sum3 += 1
    if trainingSet[j][0] == '时尚':
        sum4 += 1
    if trainingSet[j][0] == '音乐':
        sum5 += 1


text = input("请输入test语句:\n")
text = text.strip()
text = jieba.lcut(text)
print(text)

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
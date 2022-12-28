from Functions import myReduce, myMap
import csv

"""
При помощи myMap разделить столбец "Идентификатор акции" на 
три отдельных столбца "Целевая/Контрольная", "Процент" и 
"Новый/Отток"

При помощи myReduce посчитать сумму бонусов (сумма 
чисел в 8 столбце)
"""

# Получить таблицу в виде двумерного списка
def getDataSet(csvFile):
    with open(csvFile, 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        return [list(i) for i in spamreader]
        

# Вставить в таблицу двуменый список
def createDataSet(dataSet, csvFile):
    with open(csvFile, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for row in dataSet:
            writer.writerow(row)
        
        
# Задача 1
def splitStockId():
    dataSet = getDataSet('DataSet.csv')
    def fun(string):
        newString = []
        newString.append(string[0])
        newString.extend(string[1].split(' ')[0:2])
        newString.append('на ' + string[1].split(' ')[3])
        newString.extend(string[2:])
        return newString

    newDataSet = myMap(fun, dataSet[1:])

    newDataSet.insert(0, [])    
    newDataSet[0].append(dataSet[0][0])
    newDataSet[0].extend(["Целевая/Контрольная", "Процент", "Новый/Отток"])
    newDataSet[0].extend(dataSet[0][2:])
    
    createDataSet(newDataSet, "new_DataSet.csv")
    
    
# Задание 2
def bonusSum():
    dataSet = getDataSet('DataSet.csv')
    bonuses = [float(i[7].replace(',', '.').replace(' ', '')) for i in dataSet[1:]]    
    return myReduce(lambda x, y: x + y, bonuses)    
    
if __name__ == "__main__":
    splitStockId()
    print(bonusSum())
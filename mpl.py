import random

train_set = [[0,0,0],
           [0,1,0],
           [1,0,0],
           [1,1,1]]


learning_rate = 0.6

n_epoch = 10

weight = [random.uniform(0,1),random.uniform(0,1)]

def predict(row, weight):
    result = 0
    for i in range(len(row) -1):
        result = result + (row[i] * weight[i])
    if result > 1.0:
        result = 1.0

    return  result

def train(train_set, weight):
    for row in train_set:
        erro = row[-1] - predict(row,weight)
        weight[0] = weight[0] + learning_rate * erro * row[0]
        weight[1] = weight[1] + learning_rate * erro * row[1]

    return weight

for row in train_set:
    print('Esperado: ' + str(row[-1]) + ' Resultado: ' + str(predict(row,weight)))


for epoch in range(n_epoch):
    weight = train(train_set, weight)
    print('Epoch = ' + str(epoch) + ' Weight = ' + str(weight))

print(predict([1,0],weight))


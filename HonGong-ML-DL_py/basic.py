import numpy as np
from sklearn.model_selection import train_test_split

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

fish_data = np.column_stack((fish_length, fish_weight)) #column_stack()는 1차원 배열을 열 방향으로 합쳐서 2차원 배열로 만들어주는 함수입니다.
fish_target = np.concatenate((np.ones(35), np.zeros(14))) #concatenate()는 여러 배열을 하나로 합치는 함수입니다. 여기서는 35개의 1과 14개의 0을 합쳐서 총 49개의 요소를 가진 배열을 만듭니다. 이 배열은 각 데이터 포인트가 어떤 클래스에 속하는지를 나타냅니다. 1은 첫 번째 클래스(예: 특정 종류의 물고기)를 나타내고, 0은 두 번째 클래스(예: 다른 종류의 물고기)를 나타냅니다.

train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, random_state=42) #train_test_split() 함수는 데이터를 무작위로 섞어서 훈련 세트와 테스트 세트로 나누는 함수입니다. 여기서는 fish_data와 fish_target을 입력으로 받아서 train_input, train_target, test_input, test_target으로 나눕니다. random_state=42는 데이터 분할을 재현 가능하게 하기 위해 사용되는 시드 값입니다. 이 값을 설정하면 같은 데이터를 사용할 때마다 같은 방식으로 데이터를 나눌 수 있습니다.
#print(train_input.shape, test_input.shape) #train_input은 훈련 세트의 입력 데이터이고, test_input은 테스트 세트의 입력 데이터입니다. 각각의 형태는 (훈련 샘플 수, 특성 수)와 (테스트 샘플 수, 특성 수)로 나타납니다.
#print(train_target)
#print(test_target) #1은 도미, 0은 빙어, 이 둘의 비율은 3.3:1 -> 이 비율을 target에 반영하기 위해 stratify 매개변수를 사용하여 데이터를 나눌 때 클래스 비율을 유지하도록 할 수 있습니다. 예를 들어, train_test_split 함수에서 stratify=fish_target을 추가하면 훈련 세트와 테스트 세트 모두에서 도미와 빙어의 비율이 원래 데이터셋과 유사하게 유지됩니다.
train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, stratify=fish_target, random_state=42) 
#print(train_target)
#print(test_target)

#K-Nearest Neighbors(KNN)은 분류와 회귀 문제에 모두 사용할 수 있는 간단한 머신 러닝 알고리즘입니다. KNN은 새로운 데이터 포인트가 주어졌을 때, 훈련 데이터에서 가장 가까운 K개의 이웃을 찾아서 그 이웃들의 클래스 레이블을 기반으로 새로운 데이터 포인트의 클래스를 예측합니다. KNN은 거리 기반 알고리즘이므로, 일반적으로 유클리드 거리나 맨하탄 거리와 같은 거리 측정 방법을 사용하여 이웃을 찾습니다. KNN은 학습 단계가 없고, 예측 단계에서 모든 훈련 데이터를 사용하기 때문에 메모리 사용량이 많고 예측 속도가 느릴 수 있지만, 간단하고 직관적인 모델로 널리 사용됩니다.
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier() #n_neighbors는 가장 가까운 이웃의 수를 지정, return_distance는 이웃과의 거리를 반환할지 여부를 지정. 여기서는 기본값인 n_neighbors=5와 return_distance=True를 사용하여 KNN 모델을 생성
kn.fit(train_input, train_target) #fit() 메서드는 KNN 모델을 훈련 데이터에 맞추는 데 사용됩니다. 여기서는 train_input과 train_target을 입력으로 주어서 모델이 훈련 데이터의 패턴을 학습하도록 합니다. 이 과정에서 KNN은 훈련 데이터의 각 포인트와 그에 해당하는 클래스 레이블을 기억하게 됩니다. 이후에 새로운 데이터 포인트가 주어졌을 때, 모델은 이 훈련 데이터를 기반으로 가장 가까운 이웃을 찾아서 예측을 수행할 수 있습니다.
print(kn.score(test_input, test_target)) #score() 메서드는 모델의 성능을 평가하는 데 사용됩니다. 여기서는 test_input과 test_target을 입력으로 주어서 모델이 테스트 데이터에서 얼마나 정확하게 예측하는지를 계산합니다. 반환되는 값은 0과 1 사이의 숫자로, 1에 가까울수록 모델의 예측이 정확하다는 것을 의미합니다. 예를 들어, 0.9라는 점수가 반환되면 모델이 테스트 데이터에서 90%의 정확도로 예측했다는 것을 나타냅니다.
print(kn.predict([[25, 150]])) #25cm, 150g인 물고기가 도미인지 빙어인지 예측하는 코드입니다. predict() 메서드는 입력된 데이터 포인트가 어떤 클래스에 속하는지를 예측합니다. 여기서는 [[25, 150]]이라는 2차원 배열을 입력으로 주었는데, 이는 길이가 25cm이고 무게가 150g인 물고기를 나타냅니다. 예측 결과는 1이면 도미, 0이면 빙어로 해석할 수 있습니다.

'''
import matplotlib.pyplot as plt
plt.scatter(train_input[:, 0], train_input[:, 1]) #train_input의 첫 번째 열은 길이, 두 번째 열은 무게를 나타냅니다. scatter() 함수는 이 데이터를 시각화하는 데 사용됩니다. 여기서는 train_input의 첫 번째 열을 x축으로, 두 번째 열을 y축으로 하여 산점도를 그립니다. 이렇게 하면 훈련 데이터에서 물고기의 길이와 무게가 어떻게 분포되어 있는지를 시각적으로 확인할 수 있습니다.
plt.scatter(25, 150, marker='^') #25cm, 150g
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
'''

import matplotlib.pyplot as plt
distance, index = kn.kneighbors([[25, 150]]) #kneighbors() 메서드는 입력된 데이터 포인트와 가장 가까운 K개의 이웃을 찾는 데 사용됩니다. 여기서는 [[25, 150]]이라는 2차원 배열을 입력으로 주어서 길이가 25cm이고 무게가 150g인 물고기와 가장 가까운 이웃들을 찾습니다. 반환되는 distance는 입력된 데이터 포인트와 각 이웃 사이의 거리를 나타내는 배열이고, index는 각 이웃의 인덱스를 나타내는 배열입니다. 예를 들어, distance[0]은 첫 번째 이웃과의 거리를 나타내고, index[0]은 첫 번째 이웃의 인덱스를 나타냅니다.
#print(distance) #입력된 데이터 포인트와 가장 가까운 이웃들 사이의 거리를 출력합니다. 이 값은 KNN 알고리즘에서 이웃을 찾는 데 사용되는 거리 측정 방법에 따라 달라질 수 있습니다. 예를 들어, 유클리드 거리를 사용하는 경우, distance 배열에는 입력된 데이터 포인트와 각 이웃 사이의 유클리드 거리가 포함됩니다.
#print(index) #입력된 데이터 포인트와 가장 가까운 이웃들의 인덱스를 출력합니다. 이 인덱스는 훈련 데이터에서 해당 이웃이 위치한 위치를 나타냅니다. 예를 들어, index[0]이 10이라면, 첫 번째 이웃은 훈련 데이터의 10번째 샘플에 해당한다는 것을 의미합니다. 이 인덱스를 사용하여 훈련 데이터에서 해당 이웃의 특성이나 클래스 레이블을 확인할 수 있습니다.
'''
plt.scatter(train_input[:, 0], train_input[:, 1]) #train_input의 첫 번째 열은 길이, 두 번째 열은 무게를 나타냅니다. scatter() 함수는 이 데이터를 시각화하는 데 사용됩니다. 여기서는 train_input의 첫 번째 열을 x축으로, 두 번째 열을 y축으로 하여 산점도를 그립니다. 이렇게 하면 훈련 데이터에서 물고기의 길이와 무게가 어떻게 분포되어 있는지를 시각적으로 확인할 수 있습니다.
plt.scatter(25, 150, marker='^') #25cm, 150g
plt.scatter(train_input[index, 0], train_input[index, 1], marker='D') #index 배열에 있는 이웃들의 위치를 산점도로 표시합니다. 여기서는 index 배열을 사용하여 train_input에서 해당 이웃들의 길이와 무게를 가져와서 x축과 y축으로 사용합니다. marker='D'는 이웃들을 다이아몬드 모양으로 표시하도록 지정하는 옵션입니다. 이렇게 하면 입력된 데이터 포인트와 가장 가까운 이웃들이 시각적으로 구분되어 나타납니다.
plt.xlabel('length')
plt.ylabel('weight')
'''
#plt.show()
#print(train_input[index]) #index 배열에 있는 이웃들의 특성 값을 출력합니다. 여기서는 train_input에서 index 배열에 해당하는 행들을 선택하여 이웃들의 길이와 무게를 출력합니다. 예를 들어, train_input[index]는 index 배열에 있는 이웃들의 길이와 무게를 포함하는 2차원 배열을 반환합니다. 이를 통해 입력된 데이터 포인트와 가장 가까운 이웃들의 특성 값을 확인할 수 있습니다.
mean = np.mean(train_input, axis=0) #train_input의 각 열에 대한 평균을 계산합니다. axis=0은 열 방향으로 평균을 계산하도록 지정하는 옵션입니다. 이렇게 하면 train_input의 첫 번째 열(길이)의 평균과 두 번째 열(무게)의 평균이 각각 계산되어 mean_length 배열에 저장됩니다. 예를 들어, mean_length[0]은 길이의 평균을 나타내고, mean_length[1]은 무게의 평균을 나타냅니다.
std = np.std(train_input, axis=0) #train_input의 각 열에 대한 표준 편차를 계산합니다. axis=0은 열 방향으로 표준 편차를 계산하도록 지정하는 옵션입니다. 이렇게 하면 train_input의 첫 번째 열(길이)의 표준 편차와 두 번째 열(무게)의 표준 편차가 각각 계산되어 std_length 배열에 저장됩니다. 예를 들어, std_length[0]은 길이의 표준 편차를 나타내고, std_length[1]은 무게의 표준 편차를 나타냅니다.
#print(mean, std) #train_input의 각 열에 대한 평균을 출력합니다.
train_scaled = (train_input - mean) / std #train_input의 각 열에서 평균을 빼고 표준 편차로 나누어서 train_scaled 배열을 만듭니다. 이렇게 하면 train_scaled의 각 열은 평균이 0이고 표준 편차가 1인 표준화된 데이터가 됩니다. 예를 들어, train_scaled[:, 0]은 길이의 표준화된 값을 나타내고, train_scaled[:, 1]은 무게의 표준화된 값을 나타냅니다.
test_scaled = (test_input - mean) / std #test_input의 각 열에서 test_input의 평균을 빼고 test_input의 표준 편차로 나누어서 test_scaled 배열을 만듭니다. 이렇게 하면 test_scaled의 각 열도 평균이 0이고 표준 편차가 1인 표준화된 데이터가 됩니다. 예를 들어, test_scaled[:, 0]은 길이의 표준화된 값을 나타내고, test_scaled[:, 1]은 무게의 표준화된 값을 나타냅니다.
kn.fit(train_scaled, train_target) #fit() 메서드는 KNN 모델을 훈련 데이터에 맞추는 데 사용됩니다. 여기서는 train_scaled과 train_target을 입력으로 주어서 모델이 표준화된 훈련 데이터의 패턴을 학습하도록 합니다. 이 과정에서 KNN은 표준화된 훈련 데이터의 각 포인트와 그에 해당하는 클래스 레이블을 기억하게 됩니다. 이후에 새로운 데이터 포인트가 주어졌을 때, 모델은 이 표준화된 훈련 데이터를 기반으로 가장 가까운 이웃을 찾아서 예측을 수행할 수 있습니다.
print(kn.score(test_scaled, test_target)) #score() 메서드는 모델의 성능을 평가합니다. 여기서는 test_scaled과 test_target을 입력으로 주어서 모델이 표준화된 테스트 데이터에서 얼마나 정확하게 예측하는지를 계산합니다. 반환되는 값은 0과 1 사이의 숫자로, 1에 가까울수록 모델의 예측이 정확하다는 것을 의미합니다. 예를 들어, 0.9라는 점수가 반환되면 모델이 표준화된 테스트 데이터에서 90%의 정확도로 예측했다는 것을 나타냅니다.
new = (np.array([[25, 150]]) - mean) / std #새로운 데이터 포인트 [[25, 150]]을 표준화합니다. 여기서는 입력된 데이터 포인트에서 train_input의 평균을 빼고 train_input의 표준 편차로 나누어서 new 배열을 만듭니다. 이렇게 하면 new 배열은 평균이 0이고 표준 편차가 1인 표준화된 데이터가 됩니다. 예를 들어, new[0, 0]은 길이의 표준화된 값을 나타내고, new[0, 1]은 무게의 표준화된 값을 나타냅니다.
print('예측 확률값=', kn.predict(new)) #predict() 메서드는 입력된 데이터 포인트가 어떤 클래스에 속하는지를 예측합니다. 여기서는 new 배열을 입력으로 주어서 길이가 25cm이고 무게가 150g인 물고기가 도미인지 빙어인지 예측합니다. 예측 결과는 1이면 도미, 0이면 빙어로 해석할 수 있습니다.
'''
plt.scatter(train_scaled[:, 0], train_scaled[:, 1]) #train_scaled의 첫 번째 열은 표준화된 길이, 두 번째 열은 표준화된 무게를 나타냅니다. scatter() 함수는 이 데이터를 시각화하는 데 사용됩니다. 여기서는 train_scaled의 첫 번째 열을 x축으로, 두 번째 열을 y축으로 하여 산점도를 그립니다. 이렇게 하면 표준화된 훈련 데이터에서 물고기의 길이와 무게가 어떻게 분포되어 있는지를 시각적으로 확인할 수 있습니다.
plt.scatter(new[0, 0], new[0, 1], marker='^') #new 배열의 첫 번째 요소는 표준화된 길이, 두 번째 요소는 표준화된 무게를 나타냅니다. scatter() 함수는 이 데이터를 시각화하는 데 사용됩니다. 여기서는 new[0, 0]을 x축으로, new[0, 1]을 y축으로 하여 산점도를 그립니다. marker='^'는 이 데이터 포인트를 삼각형 모양으로 표시하도록 지정하는 옵션입니다. 이렇게 하면 입력된 데이터 포인트가 표준화된 훈련 데이터에서 어디에 위치하는지를 시각적으로 확인할 수 있습니다.
plt.scatter(train_scaled[index, 0], train_scaled[index, 1], marker='D') #index2 배열에 있는 이웃들의 위치를 산점도로 표시합니다. 여기서는 index2 배열을 사용하여 train_scaled에서 해당 이웃들의 표준화된 길이와 무게를 가져와서 x축과 y축으로 사용합니다. marker='D'는 이웃들을 다이아몬드 모양으로 표시하도록 지정하는 옵션입니다. 이렇게 하면 입력된 데이터 포인트와 가장 가까운 이웃들이 시각적으로 구분되어 나타납니다.
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
'''
#3장: k-최근접 이웃 회귀

import calendar
calendar.setfirstweekday(calendar.SUNDAY) 
print(calendar.calendar(2026))

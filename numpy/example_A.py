import numpy as np

array1 = np.arange(4) #0~3까지 배열
print(array1)

array2 = np.zeros((4,4), dtype = float) #4,4의 2차원배열 만들고 float형 0.으로 초기화
print(array2)

array3 = np.ones((3,3), dtype = str) # 3,3의 2차원 배열후 문자열 '1' 로 초기화
print(array3)

array4 = np.random.randint(0, 10, (3, 3)) #0~9까지 3*3배열에 랜덤 int 채워넣기
print(array4)

array5 = np.random.normal(0, 1, (3, 3)) #평균이 0이교 표준편차가 1인 표준정규를 띄는 배열
print(array5)


array6 = np.array([1,2,3])
array7 = np.array([4,5,6])
array8 = np.concatenate([array6, array7])
array8 = array8.reshape(2,3) # 변수 합성후 형 변환
print(array8)


array9 = np.arange(4).reshape(4,1)
array10 = np.arange(8).reshape(4,2)
array11 = np.concatenate([array9, array10], axis = 1) #합친다 0 행을기준으로 1열을 기준으로 
print(array11)

array = np.arange(16).reshape(8,2)
left, right = np.split(array, [4], axis = 0) # 분할한다 행(가로)을기준으로 2칸씩
print(left ,"\n" , right) 
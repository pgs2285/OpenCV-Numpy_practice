import numpy as np

# array = np.arange(0,10)
# np.save('saved.npy',array) #압축된 형태로 저장

# result = np.load('saved.npy')
# print(result)

# array1 = np.arange(0,10)
# array2 = np.arange(10,20)
# np.savez('saved.npz', save1 = array1, save2 = array2) # savez는 복수개의 넘파이를 저장하는데 사용함 뒤에 (...)= array1 부분은 이름지정하는것

# data = np.load('saved.npz')
# result1 = data['save1'] # 위에서 저장했던 이름 넣음 된다
# result2 = data['save2'] # 위에서 저장했던 이름 넣음 된다
# print(result1, result2)

# array3 = np.array([5,2,1,2,3,4])
# array3.sort()#정렬
# array3 = array3[::-1]#역정렬
# print(array3)

# #행기준 정렬

# array4 = np.array([[1,4,3,6,3,2],[1,3,1,2,9,8]])
# array4.sort(axis = 0)#행기준 정렬 이 경우엔 위아래 비교후 큰게 아래로 간다
# print(array4)

# array5 = np.linspace(0,9,5) # 0~9까지 균일한 간격 데이테 5개 생성
# print(array5)

# np.random.seed(7) #난수 시드 설정, 시드가 같으면 동일한 난수가 나옴
# print(np.random.randint(0, 10, (2, 3)))

# array6 = np.arange(10)
# array7 = array6.copy()#copy를 안쓰고 =만 사용할 경우에는 주소가 그대로 복사되 array6에도 영향을 미치므로 copy 사용 
# array7[0] = 99
# print(array6,array7)


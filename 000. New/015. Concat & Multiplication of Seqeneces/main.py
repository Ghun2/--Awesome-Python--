# 동일한 Sequence 객체끼리의 합 연산, Sequence와 int 간의 곱 연산이 가능하다

# -- Sequence + Sequence
print([1, 2, 3, 4] + [4, 5]) # [1, 2, 3, 4, 4, 5]
print((1, 2, 3, 4) + (4,)) # (1, 2, 3, 4, 4)
# print((1,) + [1])
# Sequence더라도, 서로 다른 객체 간에는 합 연산이 불가능하다

# -- Sequence * int
print([1, 2, 3, 4] * 2) # [1, 2, 3, 4, 1, 2, 3, 4]
print((1, 2, 3, 4) * 2) # (1, 2, 3, 4, 1, 2, 3, 4)
# Sequence와 int 간의 곱은 n만큼의 길이를 가지고, 모두 m으로 채워진 list를 만드는 데에 유용하게 쓰인다
print([0] * 10) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

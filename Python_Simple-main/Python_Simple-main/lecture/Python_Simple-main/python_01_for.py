# 문제4) list b 에서 최소값 찾기
b = [22, 1, 4, 7, 98]

num_min = b[0] #22
for x in b:
    if x <num_min:
        num_min = x
print(f"최소값: {num_min}")

# 문제5) list c의 최소값, 최대값 찾기
c = [2, 5, 7, 1, 8]

num_min = c[0]
num_max = c[0]

num_min = c[0]
for x in c:
    if x <num_min:
        num_min = x
    if x > num_max:
        num_max = x
        
print(f"최소값: {num_min}")
print(f"최대값: {num_max}")

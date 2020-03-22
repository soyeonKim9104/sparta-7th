# 여기는 주석입니다.
# 변수 선언하기
a = 2
b = 3

# 파이선은 변수명을 스네이크 케이스를 권장한다.
sparta_coding = 10

# 사칙연산
c = a + b
c = a - b
c = a * b
c = a / b
c = a % b

# 변수 타입
a = 'sparta coding'
a = 10.3
a = True
b = False
# 나열형
a = [10, 'Sparta', True, 11]
# 딕셔너리 형
b = {
    "Sparta" : 10,
    "cording" : True
}

c = a[0]
d = b["Sparta"]

a = []
a.append(10)
# js에서는 a.push(10)
b = {}
b["sparta"] = 20
# 결과물 : b = { "sparta" : 20 }


# 반복문
# js는
# for(let i =0; i <10; i++){}

# 파이썬은 js처럼 중괄호로 닫고 열기지만, 파이썬은 닫는 개념이 아니라 탭으로 구분한다.
for i in range(10):
    print(i)

# 조건문
# js 는
# if(...){}

if a > 10:
    print(a)
elif b > 10:
    print(b)
else:
    print(c)

# 함수 작성시
# js는
# function test{}

def test(a = 10):
    print(a)
# 함수실행시
test(20)
a = 'spartacodingclub@gmail.com'

#채워야하는 함수
def check_mail(s):
    #return s.find('@') > -1
    b = s.split('@')
    if len(b) > 1:
        return True
    else:
        return False

#결과값
print(check_mail(a))

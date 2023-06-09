'''
2023-05-17
최재혁
for문을 이용한 파일 읽기
'''

with open("C:/data/linetext.txt","r") as f: #파일 열기
    for line in f: #파일 객체를 지정해서 반복문 작성
        print(line,end='')

#readline():(한줄씩 읽어 오기) 메소드로 파일 읽어 오기
print()

with open("C:/data/linetext.txt","r") as f: #파일 열기
    while True:
        line=f.readline() #파일 한 줄씩 읽어 오기
        print(line,end='') #줄 바꿈 없이 출력

        if line=='': #읽어 올 내용이 없다면
            break #반복 종료

#readlines(): 한 줄씩 읽어서 리스트형으로 반환
print()

with open("C:/data/linetext.txt","r") as f:
    textlists=f.readlines() #한 줄씩 리스트 형식으로 읽어 오기
    print(type(textlists)) #변수 타입 확인
    print(textlists)


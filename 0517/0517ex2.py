'''
2023-05-17
최재혁
#문제정의
    기존파일을 새로운 파일에 복사하는 프로그램 만들기
#문제분석
    변수: 원본파일입력(source), 복사할 파일(target),
          원본파일의 내용(texts)
#알고리즘3
    1.source에 원본파일 이름 입력
    2. target에 복사할 파일 이름 입력
    3.파일처리
        source파일 객체생성
            파일 한꺼번에 읽어 오기
            내용을 texts 변수에 저장
        target파일 객체생성
            texts파일 쓰기
        파일생성 메세지 출력
'''

source=input("source 파일 입력:")
target=input("target 파일 입력:")

with open("C:/data/linetext.txt","r") as f: #읽기 파일 객체
    texts=f.read() #파일  한꺼번에 문자열로 읽기

with open("C:/data/copylinetext.txt","w") as fp: #쓰기 파일 객체
    fp.write(texts) #원본파일에서 읽어 온 내용 파일에 출력

    print(target+"파일이 생성되었습니다.") #메세지 출력
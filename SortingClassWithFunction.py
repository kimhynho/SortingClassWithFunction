#프로그램명 SortingClassWithFunction.py
#작성자 소웨 김현호
#작성일 3/18 ~3/23
#프로그램 설명.
#학생 5명의 성적을 입력받고, 평균에 따라 학점을 부여하며,
#평균 점수를 기준으로 등수를 계산해 출력하는 성적 관리 프로그램.
 #hamsu(x): x번째 학생의 정보를 입력받아 계산된 정보를 반환 리스트들을 이용해 학생별 정보 저장후 반복문을 통해 5명의 성적 입력 및 처리
#평균 기준으로 등수 계산 전체 학생 정보를 정리해서 출력

def hamsu(x):

 hak = int(input("학번"))
 name = str(input("이름"))
 eng = int(input("영어"))
 c = int(input("c언어"))
 py = int(input("파이썬"))
 sum = eng+c +py
 evg = (eng + c + py) // 3
 score = evg
 score1 =evg
 score2 =evg
 score3 =evg
 score4 =evg
 score5 =evg

 if evg >= 90:
    score = "A"
 elif evg >= 80:
    score = "B"
 elif evg >= 70:
     score ="C"
 else: #else 구문은 옵션이지만 다중족너을 설정할 때는 절대 조건을 명기하면 안된다.
    score = "F"
 if (x == 1):
     return hak, name, eng, c, py, sum, evg, score, score1
 elif (x ==2 ):
     return hak, name, eng, c, py, sum, evg, score, score2
 elif (x ==3 ):
     return hak, name, eng, c, py, sum, evg, score, score3
 elif (x == 4):
     return hak, name, eng, c, py, sum, evg, score, score4
 elif (x ==5 ):

     return hak, name, eng, c, py, sum, evg, score, score5

hack = [1,2,3,4,5]
name = [1,2,3,4,5]
eng = [1,2,3,4,5]
c = [1,2,3,4,5]
py = [1,2,3,4,5]
sum = [1,2,3,4,5]
evg = [1,2,3,4,5]
score = [1,2,3,4,5]
score_rank =[1,2,3,4,5]

for i in range (1 , 6):
       hack[i-1],name[i-1],eng[i-1],c[i-1],py[i-1],sum[i-1],evg[i-1],score[i-1],score_rank[i-1] = hamsu(i)

sorted_arr1 = sorted(score_rank, reverse = True ) #점수가 높은순으로 내림차순 정렬
ranks = [sorted_arr1.index(s) +1 for s in score_rank]  #등수는 1부터 시작되므로 +1 넣어줌


print("                                              성적관리 프로그램                                                 \n")
for i in range (0, 5):
 print("============================================================================================================\n")
 print("\t",hack[i],"\t",name[i],"\t",eng[i],"\t",c[i],"\t\n",py[i],"\t",sum[i],"\t",evg[i],"\t",score[i],"\t",ranks[i])

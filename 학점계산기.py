print("작업을 선택하세요.\n1. 입력\n2. 계산")
task = input('')

creditsum2 = 0                                    #제출용 (F 미포함)
creditsum = 0                                     #열람용 (F 포함)
gradesum = 0
credit = 1

if task == "1" :
    while credit !=0 : 
        print("학점을 입력하세요: ")
        credit = int(input(''))
        creditsum += credit
        creditsum2 += credit

        if credit != 0 :
            print("평점을 입력하세요: ")
            grade = input('')
            print("입력되었습니다.\n")
                
            if grade == "A+" :
                gradesum = gradesum + 4.5 * credit
                
            elif grade == "A" :
                gradesum = gradesum + 4.0 * credit

            elif grade == "B+" :
                gradesum = gradesum + 3.5 * credit

            elif grade == "B" :
                gradesum = gradesum + 3.0 * credit

            elif grade == "C+" :
                gradesum = gradesum + 2.5 * credit

            elif grade == "C" :
                gradesum = gradesum + 2.0 * credit

            elif grade == "D+" :
                gradesum = gradesum + 1.5 * credit

            elif grade == "D" :
                gradesum = gradesum + 1.0 * credit

            elif grade == "F" :
                creditsum2 = creditsum - credit

print("작업을 선택하세요.\n1. 입력\n2. 계산")
task = input('')

if task == "2" :
    print(f"제출용: {creditsum2} 학점 (GPA: {round(gradesum/creditsum2, 2)})")
    print(f"열람용: {creditsum} 학점 (GPA: {round(gradesum/creditsum, 2)})")
    print("\n프로그램을 종료합니다.")
# 模式匹配，可以看作是switch的加强版，python中没有swtich语句
score = input("请输入你的成绩等级：")
match score: 
    case 'A':
        print("优秀")
    case 'B':
        print("良好")
    case 'C':
        print("及格")
    case 'D':
        print("不及格")
    case 'E':
        print("差")
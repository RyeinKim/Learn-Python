'''
조건 분기 사용하기
'''
def washingmachine(mode):
    print('급수한다')
    if(mode == 'soft'):
        print('부드럽게 씻는다')
    elif(mode == 'hard'):
        print('세게 씻는다')
    else:
        print('씻는다')
    print('헹군다')
    print('탈수한다')
    print('건조한다')

washingmachine('soft')

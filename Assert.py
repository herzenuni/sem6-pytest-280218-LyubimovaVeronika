from Dictionary import Dictionary

test1 = ['а','б','в','г','д']
test2 = ['а','б','в','г','д']
result = {'а': 'а', 'б': 'б', 'в': 'в', 'г': 'г','д': 'д'}

assert Dictionary(test1,test2) == result, 'Ошибка'

test1 = ['а','б','в']
test2 = [1,2]
result = {'а': 1, 'б': 2, 'в': None}


assert Dictionary(test1,test2) == result, 'Ошибка'

test1 = ['а','б','в']
test2 = [1,2,3,4,5]
result = {'а': 1, 'б': 2, 'в': 3}


assert Dictionary(test1,test2) == result, 'Ошибка'

test1 = []
test2 = []
result = {}

assert Dictionary(test1,test2) == result, 'Ошибка'
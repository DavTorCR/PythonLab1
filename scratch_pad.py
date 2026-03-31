import numpy
un = [[9,8,7], [6,5,4], [3,2,1]]
de = [[1,2,3], [4,5,6], [7,8,9]]
trois = [[10,11,12], [13,14,15], [16,17,18]]
print('I had to spend a good thirty minutes getting NumPy to work.')
print('-'*30)
print('Seeing that the error message repeated the advice that the documentation recommednded, retry to download.')
print('-'*30)
print('Making a quick try to see if it was a version issue, I downgraded from the newest version, 2.4.3.')
print('-'*30)
print(f'"The version that did work is: {numpy.__version__}"')
print('-'*30)
print(f'"The number that corresponds to matrix un 1,3 is: {un[0][2]}"')
print('-'*30)
print(numpy.dot(un,de))
print('-'*30)
print(numpy.dot(de,trois))

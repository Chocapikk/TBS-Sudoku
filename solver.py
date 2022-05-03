from bs4 import BeautifulSoup as bs
import requests
import urllib.parse
import numpy as np

M = 9

def matrixes(list,number):
  mat = []
  while list != []:
    mat.append(list[:number])
    list = list[number:]
  return mat

def reset_matrixes(list):
	result = []
	for i in range(len(list)):
		for j in list[i]:
			result.append(j)
	return result

def inverse(list):
	tmp = []
	result = []
	order = [0,3,6,1,4,7,2,5,8]
	for i in range(0,3):
		for j in range(i,len(list),3):
			tmp.append(list[j])
	tmp = matrixes(reset_matrixes(tmp),9)
	for i in order:
		result.append(tmp[i])
	return result


def puzzle(a):
	solution = []
	for i in range(M):
		for j in range(M):
			solution.append(str(a[i][j]))
			print(a[i][j],end=' ')
		print()
	return solution

def solve(grid, row, col, num):
	for x in range(9):
		if grid[row][x] == num:
			return False
		    
	for x in range(9):
		if grid[x][col] == num:
			return False


	startRow = row - row % 3
	startCol = col - col % 3
	for i in range(3):
		for j in range(3):
			if grid[i + startRow][j + startCol] == num:
				return False
	return True

def Sudoku(grid, row, col):

	if (row == M - 1 and col == M):
		return True
	if col == M:
		row += 1
		col = 0
	if grid[row][col] > 0:
		return Sudoku(grid, row, col + 1)
	for num in range(1, M + 1, 1): 
	
		if solve(grid, row, col, num):
		
			grid[row][col] = num
			if Sudoku(grid, row, col + 1):
				return True
		grid[row][col] = 0
	return False

'''0 means the cells where no value is assigned'''
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
		[4, 0, 7, 0, 0, 0, 2, 0, 8],
		[0, 0, 5, 2, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 9, 8, 1, 0, 0],
		[0, 4, 0, 0, 0, 3, 0, 0, 0],
		[0, 0, 0, 3, 6, 0, 0, 7, 2],
		[0, 7, 0, 0, 0, 0, 0, 0, 3],
		[9, 0, 3, 0, 0, 0, 6, 0, 4]]

grid2 = [[2, 5, 0], [0, 3, 0], [9, 0, 1],
         [0, 1, 0], [0, 0, 4], [0, 0, 0],
		 [4, 0, 7], [0, 0, 0], [2, 0, 8],
		 [0, 0, 5], [2, 0, 0], [0, 0, 0],
		 [0, 0, 0], [0, 9, 8], [1, 0, 0],
		 [0, 4, 0], [0, 0, 3], [0, 0, 0],
		 [0, 0, 0], [3, 6, 0], [0, 7, 2],
		 [0, 7, 0], [0, 0, 0], [0, 0, 3],
		 [9, 0, 3], [0, 0, 0], [6, 0, 4]]


url = "http://sudoku.tbsctf.fr/"
request = requests.get(url)
request = str(request.text)
request = request.replace('&amp;nbsp', '').replace('&nbsp','').replace('+::::::::::::::::+:::::::::::::::+::::::::::::::::+','').strip('\n')
soup = bs(request, "lxml")
request = str(soup.findAll('p')).replace('<p>','').replace('</p>','').replace(',','').replace('\n\n','').replace('\n','').replace('Send me the result under the form : board:SUDOKU_COMPLETED urlencoded using a POST request. The board must be a two dimensional array representing each row of the sudoku.','').replace(' ','').replace('|','').replace('[','').replace(']','')

#print(request)

list1=[]
list1[:0]=request
list1 = [int(x) for x in list1]
matrix = matrixes(list1,M)




if (Sudoku(matrix, 0, 0)):
	solution = matrixes(puzzle(matrix),M)
	print("Solved")
else:
	print("Solution does not exist:(")

solution = reset_matrixes(solution)
solution = matrixes(solution,3)
print(solution)
print('\n\n')
solution = inverse(solution)
solution = reset_matrixes(solution)
solution = matrixes(solution,9)
#print(solution)
params = {'board': solution}
#print(params)
#flag = requests.post(url = url, data = params)
#print(flag.text)

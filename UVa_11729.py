from operator import itemgetter, attrgetter, methodcaller

Question = 'UVa_11729'
def open_unit_test_file():
	UT_file = open('unit_test.txt').read()
	IO = UT_file[UT_file.find(Question + '_start'):UT_file.find(Question + '_end')]

	Input = IO[IO.find('input'):IO.find('output')]
	Input_arr = Input.split('\n')
	Input_arr = Input_arr[1:-1]

	Output = IO[IO.find('output'):]
	Output_arr = Output.split('\n')
	Output_arr = Output_arr[1:-1]
	
	return Input_arr, Output_arr

def UVa_11729(Input_arr, Output_arr):
	Answer = []
	for i in range(0, len(Output_arr), 1):
		data = (Input_arr[i].split('\t'))
		data = [eval(ii) for ii in data]
############################################################
		data = sorted(data, key=itemgetter(1,0), reverse=True)
		
		max_time = 0
		temp = 0
		for ii in data:
			temp = temp + ii[0]
			max_time = max(max_time, temp+ii[1])
		Answer = Answer + [str(max_time)]
	return Answer
############################################################

if __name__ == '__main__':
	[Input_arr, Output_arr] = open_unit_test_file()
	Answer = UVa_11729(Input_arr, Output_arr)
	print Answer
	print Output_arr

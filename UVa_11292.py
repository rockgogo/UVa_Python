Question = 'UVa_11292'
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

def UVa_11292(Input_arr, Output_arr):
	Answer = []
	Input_item = len(Input_arr)/len(Output_arr)
	for i in range(0, len(Output_arr), 1):
		if( Input_arr[i*Input_item+0] == '0\t0'):
			return Answer
		n = (Input_arr[i*Input_item+1].split('\t'))
		for ii in range(len(n)):
			n[ii] = int(n[ii])
		m = (Input_arr[i*Input_item+2].split('\t'))
		for ii in range(len(m)):
			m[ii] = int(m[ii])
############################################################
		n.sort()
		m.sort()
		cur = 0; cost = 0
		for m_num in m:
			if m_num >= n[cur]:
				cur = cur + 1
				cost = cost + m_num
				if cur == len(n):
					Answer = Answer + [str(cost)]
					break
		else:
			Answer = Answer + ['Loowater is doomed!']
	return Answer
############################################################

if __name__ == '__main__':
	[Input_arr, Output_arr] = open_unit_test_file()
	Answer = UVa_11292(Input_arr, Output_arr)
	print Answer
	print Output_arr

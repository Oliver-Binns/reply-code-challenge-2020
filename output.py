import os

def replyer_position(replyer):
	if replyer.position == None:
		return "X"
	else:
		return str(replyer.position)

def output_solution(file_name, replyers):
	path = "Outputs"
	if not os.path.exists(path):
	  os.mkdirs(path)
	file = open(f'{path}/{file_name}.txt', "w+")
	
	for replyer_line in map(replyer_position, replyers):
		file.write(f'{replyer_line}\n')

	file.close()
	

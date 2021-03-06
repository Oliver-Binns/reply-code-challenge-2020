class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __str__(self):
		return f'{self.x} {self.y}'

class Replyer:
	def __init__(self, company, bonus_potential):
		self.company = company
		self.bonus_potential = bonus_potential
		self.position = None
		
	def set_position(position):
		self.position = position

class Developer(Replyer):
	def __init__(self, input_string):
		info = input_string.split(" ")
		super(Developer, self).__init__(info[0], int(info[1]))
		
		self.skills = info[3:]
		
class ProjectManager(Replyer):
	def __init__(self, input_string):
		info = input_string.split(" ")
		super(ProjectManager, self).__init__(info[0], int(info[1]))

def parse_input(file_name):
	file = open(f'Inputs/{file_name}.txt', "r")
	width, height = map(int, file.readline().split(" "))
	
	office_rows = [file.readline().strip() for _ in range(height)]
	
	developer_count = int(file.readline())
	developers = list(map(Developer, 
	                  [file.readline().strip() for _ in range(developer_count)]))
	
	pm_count = int(file.readline())
	project_managers = list(map(ProjectManager,
	                        [file.readline().strip() for _ in range(pm_count)]))
	
	file.close()
	return (office_rows, developers, project_managers)

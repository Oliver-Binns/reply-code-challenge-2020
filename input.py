class Replyer:
	def __init__(self, company, bonus_potential):
		self.company = company
		self.bonus_potential = bonus_potential

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
	file = open("%s.txt" % file_name, "r")
	width, height = map(int, file.readline().split(" "))
	
	office_rows = [file.readline().strip() for _ in range(height)]
	
	developer_count = int(file.readline())
	developers = list(map(Developer, 
	                  [file.readline().strip() for _ in range(developer_count)]))
	
	pm_count = int(file.readline())
	project_managers = list(map(ProjectManager,
	                        [file.readline().strip() for _ in range(pm_count)]))
	
	return (office_rows, developers, project_managers)

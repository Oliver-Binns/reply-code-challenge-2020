from input import parse_input
from output import output_solution

def run_challenge(file_name):
	office_layout, developers, project_managers = parse_input(file_name)
	output_solution(f'{file_name}_solution', developers + project_managers)

if __name__ == "__main__":
	files = ["a_solar", "b_dream", "c_soup", "d_maelstrom", "e_igloos", "f_glitch"]
	
	run_challenge("a_solar")
  #map(run_challenge, map(lambda file_name: "Inputs/%s" % file_name, files))



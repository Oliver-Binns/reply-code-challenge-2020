from input import parse_input

def run_challenge(file_name):
	office_layout, developers, project_managers = parse_input(file_name)
	print(office_layout)

if __name__ == "__main__":
	files = ["a_solar", "b_dream", "c_soup", "d_maelstrom", "e_igloos", "f_glitch"]
	run_challenge("Inputs/a_solar")
  #map(run_challenge, map(lambda file_name: "Inputs/%s" % file_name, files))



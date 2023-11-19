#class Token:
    #token = [SECTION, DOT, MESSAGE, 
             #INPUT, VARIABLE, SINGLEQUOTES, 
             #DATA]

def extract_text(line):
    text_start = line.find("'") + 1
    text_end = line.rfind("'")
    return line[text_start:text_end]


with open('main.wnbl', 'r') as file:
    lines = file.readlines()

current_section = None
sections = {}
variables = {}

for line in lines:
    line = line.strip() 

    if line.startswith('.section'):
        current_section = line.split()[1]
        sections[current_section] = []

    if line.startswith('.data'):
        current_section = '.data'
        sections[current_section] = []

    if line.startswith('variable'):
        variable_data = extract_text(line)
        variable_name, value = variable_data.split("' '")
        variables[variable_name] = value

    if current_section:
        sections[current_section].append(line)

for section_name, section_code in sections.items():
    input_needed = False
    input_text = ""

    for line in section_code:
        if 'message' in line:
            extracted_text = extract_text(line)
            if extracted_text:
                print(f"{extracted_text}")

        if 'input' in line:
            input_needed = True
            extracted_input = extract_text(line)
            if extracted_input:
                input_text = input("")

        if 'jmp' in line:
            jmp_section = line.split()[1]

    if input_needed and input_text:
        pass

for var_name, value in variables.items():
    if "'" not in value:
        pass

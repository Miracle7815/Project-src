import os
import ast
import program_graph
import re

def build_graph(file_path , method_name):
    if os.path.isfile(file_path):
        with open(file_path , 'r' , encoding="utf-8") as file:
            content = file.readlines()
            file.close()
        pattern_package = r'^(\s*package\s+[a-zA-Z0-9_.]+\s*;)\s*(?://.*|/\*.*?\*/)?\s*$'
        pattern_import = r'^(\s*import\s+(?:static\s+)?[a-zA-Z0-9_.*]+\s*;)\s*(?://.*|/\*.*?\*/)?\s*$'
        packages = []
        imports = []
        static_vars = []
        for line in content:
            if re.match(pattern_package, line):
                new_line = re.sub(pattern_package, r'\1', line.strip()).rstrip(';')
                packages.append(new_line)
    
            elif re.match(pattern_import, line):
                new_line = re.sub(pattern_import, r'\1', line.strip()).rstrip(';')
                imports.append(new_line)
        
        print(packages)
        print(imports)
    else:
        print("The file no exists")

file_path = os.path.join(os.getcwd() , "My_project" , "example_program.java")
print(file_path)
build_graph(file_path , "d")

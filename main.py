import os


print("Hello World!")

current_directory = os.path.dirname(__file__)
f_path = current_directory+"/../../project_course_data/pilot3.txt"

if os.path.exists(f_path):
    with open(f_path, "r") as f:
        f_content = f.read()
        print(f_content)


 
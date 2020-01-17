import os
import sys

def start_sort(path_to_template_file, path_to_folder):
    print("Template file is:" ,path_to_template_file)
    
    with open(path_to_template_file) as template_file:
        lines_template_file = [line_template_file.strip() for line_template_file in template_file]
    
    for root, dirs, files in os.walk(path_to_folder):
            for filename in sorted(files):
                with open(path_to_folder + filename) as file:
                  lines_file = [line_file.strip() for line_file in file]  

                resault=set(lines_template_file) - set (lines_file)

                resault_file = open('resault_file', 'w')
                resault_file.write (filename + "\n")
                for item in resault:
                    resault_file.write("%s\n" % item)


def main():

    path_to_folder = input("Enter path to dir:\n")

    if os.path.isdir(path_to_folder)==True:
        for root, dirs, files in os.walk(path_to_folder):
            for filename in sorted(files):
                print(filename)
    else:
        print("Directory does not exist")
        sys.exit()

    template_filename = input ("Enter the name of template file:\n")

    if path_to_folder[-1]!= "/":
        path_to_folder = path_to_folder + "/" 
    
    path_to_template_file = path_to_folder + template_filename

    if os.path.isfile(path_to_template_file)==True:
        start_sort (path_to_template_file, path_to_folder)
    else:
        print("File does not exist")
        sys.exit()
    




if __name__ == "__main__":
    main()
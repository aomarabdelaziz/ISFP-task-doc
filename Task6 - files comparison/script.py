import os

def load_lines_into_dict(directory_path):
    files_in_directory = os.listdir(directory_path)
    lines_found = {}
    for file_name in files_in_directory:
        file_path_abs = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path_abs):
            with open(file_path_abs, 'r') as file:
                for line in file:
                    file_name_only = os.path.basename(file_path_abs)
                    if line.strip() not in lines_found:
                        lines_found[line.strip()] = [file_name_only]
                    else:
                        lines_found[line.strip()].append(file_name_only)
    return lines_found

def compare_lines_src_dest(lines_dict, output_file):
    with open("source.txt", 'r') as source_file:
        with open(output_file, 'w') as result_file:
            for line in source_file:
                line = line.strip()
                if line in lines_dict:
                    result_file.write(f"{line}'{', '.join(lines_dict[line])}\n")

lines_dict = load_lines_into_dict("./Destination")
compare_lines_src_dest(lines_dict, "output.txt")

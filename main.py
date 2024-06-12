def read(input_file_path):
    integers = []
    
    with open(input_file_path, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if not stripped_line:
                continue
            
            parts = stripped_line.split()
            if len(parts) != 1:
                continue
            
            try:
                num = int(parts[0])
                if -1023 <= num <= 1023:
                    integers.append(num)
            except ValueError:
                continue
    
    return integers

def duplicates(integers):
    count_dict = {}
    
    for num in integers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    duplicates = [num for num, count in count_dict.items() if count > 1]
    duplicates.sort()
    
    return duplicates

def write(output_file_path, duplicates):
    with open(output_file_path, 'w') as file:
        for num in duplicates:
            file.write(f"{num}\n")

def main(input_file_path, output_file_path):
    integers = read(input_file_path)
    duplicate_integers = duplicates(integers)
    write(output_file_path, duplicate_integers)


input_file_path = '/home/kellia/Term-Quiz/input.txt'
output_file_path = '/home/kellia/Term-Quiz/output.txt'
main(input_file_path, output_file_path)


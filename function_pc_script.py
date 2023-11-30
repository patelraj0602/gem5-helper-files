import re

def extract_function_calls(input_file,output_file_pc_address):
    
    with open(input_file, 'r') as infile, open(output_file_pc_address,'w') as outfile1:

        count = 0
        for line in infile:
            match = re.search(r"(\b[0-9a-fA-F]+\s<\w+>:)$", line)
            if match:
                pc_address = match.group(1)
                pc_trimmed = pc_address[:16]
                # outfile1.write(pc_trimmed+" " + pc_address + "\n")
                outfile1.write(pc_trimmed+"\n")
                count+=1
        print(count)

    
if __name__ == "__main__":
    input_file = 'riscv-exec.txt'
    output_file_pc_address = 'pc-address.txt'
    extract_function_calls(input_file, output_file_pc_address)

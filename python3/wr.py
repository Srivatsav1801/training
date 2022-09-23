import csv
import sys
import tracemalloc
import time

def in_value():
    i = 1 
    while True:
        yield i
        i=i+1        
    
def write_10mil(new_file):
    with open( new_file, 'w') as f1:
        for k in in_value():
            if k == 10000001:
                break
            f1.write(f"{k}\n")

def file_read(file_name):
    with open(file_name,'r') as f:
        for l in f:
            line = f.readline()
            yield line

def store_lines_list(file_name):
    list = []
    for l in file_read(file_name):
        list.append(l)
    print(list)

def main():
    start = time.time()
    tracemalloc.clear_traces() 
    tracemalloc.start()
    choice = int(input("1.Create a text file with 10 million lines\n2.To store the lines in text file to a list and print\n3.exit\n"))
    if choice == 1:
        print("you choose to create a text file with 10 million lines")
        new_file = input("Enter the text file name with extention:  ")
        print("Creating...")
        write_10mil(new_file)
    elif choice == 2:
        print("You choose store the lines in text file to a list and print")
        file_name = input("Enter the file name with extention: ")
        print("creating a list and printing...")
        store_lines_list(file_name)
    else:
        sys.exit
    end = time.time()
    t = end - start
    print("{:.4f}Sec".format(t)) 
    print(f"Memory Used (Current, Peak): {tracemalloc.get_traced_memory()} in bytes")
    tracemalloc.stop()
        
if __name__ =='__main__':
    main()

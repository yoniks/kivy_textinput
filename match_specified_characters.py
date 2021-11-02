files = 'sds’UHJHj/$7e\name_file.csvLjsi\file1.csvisKL#@di\file2.csv'
counter = -1
my_files = []
for f in files:
    counter += 1
    if ord(f) == 92: # if this char is '\' or something you can add
        temp = files[counter+1:len(files)]
        temp_file = ""
        for f1 in temp:
            temp_file += f1
            # [0-len(temp_file)] => if [char after . to num index of type file]== csv
            if f1 == '.' and temp[len(temp_file):len(temp_file)+3] == "csv":
                my_files.append(temp_file + "csv")
                break
print(my_files)

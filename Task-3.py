import random
import sys
import string

def fileReader(f_name):
    with open(f_name, "r") as init_file:
        student_list = init_file.readlines() # reading the given file line by line
        return [std.strip() for std in student_list] # removing character '\n' from end of line and returning list

def randomNumberGenerator():
    return str(random.randrange(1000, 10000))  # returing random 4 digit number after converting to string  

def emailGeneratorWithStdId(stdList, domain):
    splitByComma = stdList.split(',') # split for first name , id and last name
    first_names = splitByComma[1] #index 1 of splitByComma is first Name, so added in first name list
    idLastName = splitByComma[0].split(' ') # split by space for student id and last name
    std_id = idLastName.pop(0) #poping student id and storing in std_id list
    last_names = "".join([iln.translate(str.maketrans('', '', string.punctuation)) for iln in idLastName]) #once id is poped, remaining will be last name and joined if any space inside last name
    
    first_names_list = first_names.strip().split(' ') # removing white space and seperating first name if present more than one
    # steps ['Augustus', 'James'] => "index 0 of Augustus a" => a.j
    first_letters = ".".join([fl[0].lower() for fl in first_names_list])
    return std_id + " " + first_letters + "." + last_names.lower() + randomNumberGenerator() + domain + '\n'

def fileWriter(output):
    output_file = open("idandEmail.txt", "a") #open, write and append the content in file
    output_file.write(output)
    
try:
    file_name = sys.argv[1]    
    student_list = fileReader(file_name) 
    # print(student_list)
    for std_list in student_list:
        output_str = emailGeneratorWithStdId(std_list, '@poppleton.ac.uk')
        fileWriter(output_str)
        
except IndexError:
    print("Error: Missing command-line argument.")
except FileNotFoundError:    
    print("Error: Cannot open " + file_name + ". Sorry about that." )
    

     
    
      



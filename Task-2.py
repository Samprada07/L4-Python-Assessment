import re #IMPORTING REGULAR EXPRESSION
print("\nPark Run Timer")
print("~~~~~~~~~~~~~~~\nLet's Go!\n")

#DECLARING VARIABLES
data_stream = ""
list_of_runners = []
list_of_time = []
combined_list = []

#RUNNING A LOOP UNTIL USER ENTERS "END"
while data_stream.upper()!="END":
    regExp = re.compile(r'^[0-9]+::[0-9]+$') #DEFINING RegEx PATTERN
    data_stream = input("> ")
    if regExp.search(data_stream): #SEARCHING FOR regEX PATTERN IN USER-INPUT STRING
        split_data = data_stream.split("::") #SPLITTING STRING ON THE BASIS OF ::
        #APPENDING ELEMENTS TO THE NECESSARY LISTS
        list_of_runners.append(split_data[0])
        list_of_time.append(int(split_data[1]))
        combined_list.append([split_data[0], int(split_data[1])]) 
        continue
    elif data_stream.upper()=="END":
        continue
    else:
        print("Error in data stream. Ignoring. Carry on.")
        
#HANDLING EXCEPTION WHEN NO RUNNER IS FOUND
try: 
    #PROMINENT CALCULATIONS 
    avg_time = sum(list_of_time)//len(list_of_time)
    fast_time = sorted(list_of_time)[0]
    slow_time = sorted(list_of_time)[-1]
    time_min = [avg_time//60, fast_time//60, slow_time//60]
    time_sec = [avg_time%60, fast_time%60, slow_time%60] # remainder is second when divided by 60
    
    #REQUIRED OUTPUTS
    print("\nTotal Runners: ", len(list_of_runners))
    print("Average Time: " + str(time_min[0]) + " minutes " + str(time_sec[0]) + " seconds ")
    print("Fastest Time: " + str(time_min[1]) + " minutes " + str(time_sec[1]) + " seconds ")
    print("Slowest Time: " + str(time_min[2]) + " minutes " + str(time_sec[2]) + " seconds ")
    #print(combined_list)
    # sort in ascending order on the basis of time. [lambda function takes argument 'time' from combined list and sort them using sorted function]
    print("Best Time Here: Runner #" + sorted(combined_list, key = lambda s:s[1])[0][0]) 
except:
     print("No data found. Nothing to do. What a pity.")






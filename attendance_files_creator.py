import os
from tkinter import messagebox

file_path = os.getcwd() + '\\Attendance'

if os.path.exists(file_path) == False:
    os.mkdir(file_path) #Creates the general Attendance folder

destinations = ('Festac','Iyana-Ipaja','Surulere','Ogba')
bus_prefixes = ('M','E')
bus_suffixes = ('1','2','3','4','5','6','7','8')

buses = []

for destination in destinations:
    for bus_prefix in bus_prefixes:
        for bus_suffix in bus_suffixes:
            bus = destination + bus_prefix + bus_suffix + '.txt'
            buses.append(bus)

fail_count = 1

for destination in destinations: 
    for bus in buses:
        if destination in bus: #This is to ensure each text file should be under the appropriate folder 
            new_path = file_path + '\\' + destination
            if os.path.exists(new_path) == False:
                os.mkdir(new_path) 
                
            new_file = new_path + '\\' + bus #Creates the directory for the text file

            if os.path.exists(new_file) == True and fail_count == 1:
                confirm_new_creation = messagebox.askyesno(title = 'Warning', message = 'Confirm Replace',
                                                       detail = 'Click YES to delete present attendance text files and create new ones.\nClick NO to cancel')
                if not confirm_new_creation:
                    exit()
        
                fail_count +=1 #This is to ensure the messagebox runs just once in the loop thereby using the first existing text file as reference.
        
            
            with open(new_file,'w'):
                pass

exit()
    

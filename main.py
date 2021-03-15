whitelisted_name = ["name1", "name2","name3"]           #enter the whitelisted items(names,items,codes etc...)
name = input("Enter your name ")                        #takes user input as assigns it as variable "name"
if name in whitelisted_name:                            #checks if the input you entered is whitelisted
    print("Your name is whitelisted: " + name) 
else:
    print("Your name is not whitelisted:  " + name)

#Create a dictionary array for placing multiple entries
user_information_hub ={}

#Place a first loop for another entry by the users if stated yes
while True:

    # Make a loop for asking users their name and valid age
    while True:
       #Place a try and except function to remind users if there are any errors in their inputted information
       try:
           while True:
               # Print an error statement wherein the maximum characters for the name must not exceed 50 and less than 2, and the age must not exceed the maximum value of 200.

               user_name=input("What is your given name? ")

               if len(user_name):
                   if len(user_name) > 50:
                       print("Must not exceed 50 characters")
                   elif len(user_name) < 2:
                       print("Must be more than one character")
                   else:
                       break

           while True:
               current_age=int(input("what is your current age as of the moment? "))

               if current_age:
                   if current_age > 200:
                       print("Cannot accept age of more than 200")
                   elif current_age < 0:
                       print("Please try again")
                   else:
                       break

           #Placing the entry dictionary
           user_information_hub[user_name] = {
               "current_age": current_age
           }
           break  # If there are no errors, break the loop

       except:
           print("Wrong Format")

    # Generate a command that ask users if they would like to input another entry
    more_data=input("Would you like to store more info? ")

    if more_data == "Yes":
        print ("Add new entries")
    elif more_data == "No":
        break #If they would like to end, break the first loop

old= 0

for info in user_information_hub: #iterate the dictionary array
    # Create a command that prints the oldest users information, e.g. name and age
    if user_information_hub [info]["current_age"]>old:
        old= user_information_hub [info]["current_age"]
print (info, ":", old)






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
               name=user_name.title()
               if len(name):
                   if len(name) > 50:
                       print("Must not exceed 50 characters")
                   elif len(name) < 2:
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
           user_information_hub[name] = {
               "current_age": current_age
           }
           break  # If there are no errors, break the loop

       except:
           print("Wrong Format")

    # Generate a command that ask users if they would like to input another entry

    while True: #Adding loop for adding new entries
        more_data = input("Would you like to store more info? ")
        if more_data == "Yes":
           print ("Add new entries")
           break
        elif more_data == "No":
           break #If they would like to end, break the first loop
        elif more_data != "Yes" and more_data !="No":
           print ("Wrong command, please try again")
    if more_data== "No":
       break

old= 0

for similar_name, age in user_information_hub.items(): #iterate the dictionary array
    # Create a command that prints the oldest users information, e.g. name and age
    if age["current_age"]>old:
        old= age["current_age"]
        age_group = {similar_name}
    elif age["current_age"] == old:
        age_group.add(similar_name)

print (f"The oldest is/are {age_group}, with a current age of {old}")
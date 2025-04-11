# Hospital management system (manage patients' info and status,hospital room
# and status,physicians' info and status as well as transaction records )

def main ():
  patient_detail = []
  hospital_ward = []  
#Main Menu of the hospital management    
  while True: 
   print("Menu") 
   print("1.Manage patient's info and status")
   print("2.Manage hospital rooms and status")
   print("3.Manage physicians' info and status")
   print("4.Manage hospital transaction records")
   print("5.Quit")
#User can choose from the main menu   
   choice = input("Please enter your choice: ")
#Choice number 1 
   if choice == '1':
      while True:
        print("")
        print("Patient Management Menu")
        print("-------------------------------------------------------------------------------------")
        print("1.Add patient details")
        print("2.Update patient's details")
        print("3.Delete patient")
        print("4.Display all the patient's details")
        print("5.Back to the main menu")
        function = input("Plase enter the function you want:")
        print("")
 
        if function == '1':
          add_patient_detail(patient_detail)
 
        elif function == '2':
          update_patient_detail(patient_detail)
 
        elif function == '3':
          delete_patient_detail(patient_detail)
 
        elif function == '4':
          display_patient_name(patient_detail)
 
        elif function == '5':
          print("Right now will go back to the main menu")
          print("")
          break
 
        else:
          print("Please try again")
 
   elif choice == '2':
      while True:
        print("")
        print("Hospital Rooms Management Menu")
        print("-------------------------------------------------------------------------------------")
        print("1.Add ward's detail")
        print("2.Update ward's details")
        print("3.Delete ward")
        print("4.Add patient to the hospital ward")
        print("5.Delete the patient form the hospital ward")
        print("6.Display all the ward's details")
        print("7.Back to the main menu")
        selection = input("Plase enter the function you want:")
        print("")
        if selection == '1':
          add_hospital_room(hospital_ward)
        elif selection == '2':
          update_hospital_room(hospital_ward)
        elif selection == '3':
          delete_hospital_room(hospital_ward)
        elif selection == '4':
          add_patient_to_ward(hospital_ward, patient_detail)
        elif selection == '5':
          delete_patient_from_ward(hospital_ward)
        elif selection == '6':
          display_ward_detail(hospital_ward)
        elif selection == '7':
          print("Right now will go back to the main menu")
          print("")
          break
        else:
          print("Please try again")
#User input choice 3  from main menu
   elif choice == '3' : 
#Menu choice 3 on managaing physicians info and status
    while True:
     print ()
     print ("Manage physician's info and status")
     print ("Menu")
     print("1.Add physician's details")
     print("2.Update physician's details")
     print("3.Delete physician's details")
     print("4.Display all the physician's details")
     print("5.Back to the main menu")
        
     Option= input ("Please choose your option (1-5): ")
#User choose option 1 to add details       
     if Option =='1' :
       add_physician_detail()
       #print (physicians_detail)
       print ("Physician info was added")
#User choose option 2 to update details        
     elif Option == '2':
      update_physician_detail() 
      #print (physicians_detail) #to debugged the programme if needed
      print ("Physician info was updated")
#User choose option 3 to delete details     
     elif Option == '3':
      delete_physician_detail()
      #print ("Physician info is removed") #To debugged if needed
      
# User choose option 4 to be able to see all details
     elif Option == '4':
      print ('These are the physicians info: ')
      display_physician_detail()
#User choose option 5 to quit                    
     elif Option== "5":
       print ("\nBack to the menu. See you again\n")
       break
#User choose the wrong option
     else:
        print ("You had choose the wrong option. Please choose again")
#Choice 4 from main menu
   elif choice == '4':
     while True:
             print()
             print("Manage Hospital Transaction Records")
             print("Menu")
             print("1.Scheduling appointments")
             print("2.Add billing transaction")
             print("3.Add patient admission")
             print("4.View all transaction")
             print("5.Back on the main menu")
             option = input("Please choose the option (1-5): \n")
#User choose option 1 for appointment
             if option == "1":
               appointments_schedule()
#              print(hospitaltransaction_rec) -for debugging purposes
               print ("Your appointment was scheduled")
#User choose option 2 for billing transaction                    
             elif option == "2":
               transaction_bill ()
#              print (hospitaltransaction_rec)
               print ("Billing transaction successfull")
#User choose option 3 to ward admission                    
             elif option =="3":
               admission_patient()
#               print (hospitaltransaction_rec)
               print ("Patient admission successful")
#User choose option 4 to view transaction                      
             elif option=="4":
               print ()
               print ("Transaction records: ")
               view_transaction()
#User choose option 5 to quit                    
             elif option== "5":
               print ("\nBack to the menu. See you again\n")
               break
#User choose the wrong option
             else:
               print ("You had choose the wrong option. Please choose again")
#Choice 5 from main menu
   elif choice == '5':
     print("Thank you and see you soon")
     break
#User enter wrong choice 
   else:
     print("Invalid choice, please try again.")
     print("")   
     
#Function for Manage patients' info and status(1)
#Let user add the patient's detail
def add_patient_detail(patient_detail):
    patient_id = int(input("Enter patient ID: "))
    #https://book.pythontips.com/en/latest/for_-_else.html
    #for-else: run a loop and search for an item, if found the item it will break. Otherwise it will go to the another scenario.
    for patient in patient_detail:
      #Check the id is that exist or not, if yes can not put the same id again
      if patient["ID"] == patient_id:
        print("This patient's ID already exist.")
        break
    else:
      #Ask user to input the patient detail
      patient_name = str(input("Enter patient name: ").upper())
      patient_age = input("Enter the patient birthday (DD/MM/YYYY): ")
      patient_gender = str(input("Enter patient gender: ").upper())
      patient_status = str(input("Enter patient status: ").upper())
      #combine all the things become dict put inside the patient_detail list
      patient_detail.append({"Name": patient_name, "ID": patient_id, "Age": patient_age, "Gender": patient_gender, "Status": patient_status})
      print("Successfully add a patient detail.")
 
#Let user change the patient name and status
def update_patient_detail(patient_detail):
  for patient in patient_detail:
    print(patient)
  #ask user to key in the patient's id to do update
  id = int(input("Please insert the patient's id that you want to update:"))
  for patient in patient_detail:
    if patient["ID"] == id:
      new_name = str(input("Please key in the new patient's name: ").upper())
      new_status = str(input("Please key in the new status of patient: ").upper())
      patient["Name"] = new_name
      patient["Status"] = new_status
      print("You have successfully update the patient details.")
      #If successfully find the patient and update the detail, will exit the loop
      break
  else:
    print("Sorry, can't find that patient.")
 
#Let user delete the patient's detail
def delete_patient_detail(patient_detail):
  print("Current Patient List:")
  #https://www.geeksforgeeks.org/enumerate-in-python/
  #enumerate can let the index start with any number
  for index, patient in enumerate(patient_detail, 1):
    #show all the patient details in the list
    print("{}. Name: {}, ID: {}, Age: {}, Gender: {}, Status: {}".format(index, patient["Name"], patient["ID"], patient["Age"], patient["Gender"], patient["Status"]))
  #User insert the index to delete patient details
  index_to_delete = int(input("Enter the index of the patient to delete: "))
  index_to_delete = index_to_delete - 1
  #Make sure the index is valid
  if 0 <= index_to_delete < len(patient_detail):
    del patient_detail[index_to_delete]
    print("You have successfully deleted.")
  else:
    print("Sorry, can't find that patient.")
 
#display all the patient detail in the list
def display_patient_name(patient_detail):
  #If the patient_detail don't have any element, it will print this
  if not patient_detail:
    print("Please add a patient first.")
  else:
    print("This is all the patient's detail:")
    for patient in patient_detail:
      print(patient)
      
#Function for Manage hospital room and status(2) 
#Let user add the details of hospital rooms
def add_hospital_room(hospital_ward):
  ward_number = int(input("Enter ward's number: "))
  for room in hospital_ward:
    #Check the id is that exist or not, if yes can not put the same id again
    if room["Number"] == ward_number:
      print("This ward's number already exist.")
      break
  else:
    #Ask user to input the ward detail
    ward_type = str(input("Enter the type of the ward: ")).upper()
    ward_status = str(input("Enter ward status(Activated/Inactivated): ").upper())
    #combine all the things become dict put inside the hospita_ward list
    hospital_ward.append({"Number": ward_number, "Type": ward_type, "Status": ward_status, 'Patient': [] })
    print("Successfully add the ward detail.")
 
#Let user change the ward's status and type
def update_hospital_room(hospital_ward):
  for ward in hospital_ward:
    print("Number: {}, Type: {}, Status:{}".format(ward["Number"], ward["Type"], ward["Status"]))
  #ask user to key in the ward's number to do update
  number = int(input("Please insert the ward's number that you want to update:"))
  for ward in hospital_ward:
    if ward["Number"] == number:
      new_ward_type = str(input("Please key in the new type of ward: ").upper())
      new_ward_status = str(input("Please key in the new status of ward: ").upper())
      #Change the previous status become the new status
      ward["Type"] = new_ward_type
      ward["Status"] = new_ward_status
      #If the previous status is activated and inside that ward have patient, it will remove all the patient
      if new_ward_status == "INACTIVATED":
        #Remove all the patient in the hospital_ward["Patient"], let it become empthy
        ward["Patient"] = []
        print("You have remove all the patients from this ward.")
      #If successfully find the ward and update the detail, will exit the loop
      print("You have successfully update the ward details")
      break
  else:
    print("Sorry, can't find that ward.")
 
#Let user delete the ward's detail
def delete_hospital_room(hospital_ward):
  print("Current ward List:")
  #https://www.geeksforgeeks.org/enumerate-in-python/
  #enumerate can let the index start with specific number
  for index, room in enumerate(hospital_ward, 1):
    #show all the patient details in the list
    print("{}. Number: {}, Type: {}, Status: {}".format(index, room["Number"], room["Type"], room["Status"]))
  #User insert the index to delete patient details
  index_to_remove = int(input("Enter the index of the wrad to delete: "))
  index_to_remove = index_to_remove - 1
  #Make sure the index is valid
  if 0 <= index_to_remove < len(hospital_ward):
    del hospital_ward[index_to_remove]
    print("You have successfully deleted.")
  else:
    print("Sorry, can't find that ward.")
 
#Let user put the specific patient to specific ward
def add_patient_to_ward(hospital_ward, patient_detail):
  #Show the current ward list to let user choose
  print("Current all the ward list:")
  for index, ward in enumerate(hospital_ward, 1):
    #Show all the ward details in the list to let user select the ward
    print("{}. Number: {}, Type: {}, Status: {}".format(index, ward["Number"], ward["Type"], ward["Status"]))
  ward_index = int(input("Please key in the index of the ward that you want to add the patient: "))
  ward_index = ward_index - 1
  #Ensure that the index of ward type by user is valid
  if 0 <= ward_index < len(hospital_ward):
    selected_ward = hospital_ward[ward_index]
    #If the ward status is "INACTIVATED" means can not use, user need to choose another ward
    if selected_ward["Status"] == "INACTIVATED":
        print("Sorry, this ward can't be used temporarily")
    else:
      print("Current all the patient list:")
      for idx, patient in enumerate(patient_detail, 1):
        #Show all the patient details in the list to let user select the patient
        print("{}. Name: {}, ID: {}, Age: {}, Gender: {}, Status: {}".format(idx, patient["Name"], patient["ID"], patient["Age"], patient["Gender"], patient["Status"]))
      #User insert the index to delete patient details
      patient_index = int(input("Enter the index of the patient that you want to put in the ward: "))
      patient_index = patient_index - 1
      #Make sure that index of patient is correct
      if 0 <= patient_index < len(patient_detail):
        selected_patient = patient_detail[patient_index]
        #Check is that have same patient in the other ward, if yes it will stop it
        for another_ward in hospital_ward:
          if selected_patient in another_ward["Patient"]:
            print("This patient already in another ward, please try another patient to put in this ward")
            break
        #Check is that have the repeat patient in the same ward, otherwise it can successfully add the patient to the ward
        else:
          if selected_patient in selected_ward['Patient']:
            print("This patient already in this ward, please try another ward to put patient.")
          else:
            print("You have successfully put {} to the {} ward.".format(selected_patient["Name"], selected_ward["Number"]))
            selected_ward['Patient'].append(selected_patient)
      else:
        print("Sorry, can't find that patient.")    
  else:
    print("Sorry, can't find that room.")
 
#Let user delete the patient in the ward
def delete_patient_from_ward(hospital_ward):
  #Let user know all the ward's detail
  print("This is all the ward's detail:")
  #Let all the ward detail get their own index, it is easily to let user choose
  for idx, ward_detail in enumerate(hospital_ward, 1):
    print("{}. Ward Number: {}, Ward Type: {}, Ward Status: {} ".format(idx, ward_detail["Number"], ward_detail["Type"], ward_detail["Status"]))
  #Ask user to choose the index of ward they want to delete the patient inside
  ask_ward_index = int(input("Please select the index of ward that you want to remove the patient inside:"))
  ask_ward_index = ask_ward_index - 1
  #Make sure the index insert by user is valid
  if 0 <= ask_ward_index < len(hospital_ward):
    #If there has patient in the ward, it will also display the patient info
    if ward_detail['Patient']:
      print("Patients in the ward:")
      #Let all the patient detail get their own index, it is easily to let user choose
      for index, patient in enumerate(ward_detail['Patient'], 1):
        print("{}. Name: {}, ID: {}, Age: {}, Gender: {}, Status: {}".format(index, patient["Name"], patient["ID"], patient["Age"], patient["Gender"], patient["Status"]))
      #Ask user to delete patient by using index
      ask_patient_index = int(input("Please select the index of patient that you want to remove: "))
      ask_patient_index = ask_patient_index - 1
      #Make sure the index key in by user is valid
      if 0 <= ask_patient_index < len(ward_detail["Patient"]):
        #https://www.programiz.com/python-programming/methods/list/pop
        #pop = remove something by using that element index
        deleted_patient = ward_detail['Patient'].pop(ask_patient_index)
        print("You have successfully removed {} from the ward.".format(deleted_patient["Name"]))
      else:
        print("Please select valid index.")
    #If there no any patient in the ward, will display this  
    else:
      print("This ward don't have any patient.")
  else:
    print("Please select valid index.")
   
#Let user know each ward's detail
def display_ward_detail(hospital_ward):
  #Checking that is that hospital_ward has any element or not, if in the list don't have any element will print this
  if not hospital_ward:
    print("There is no ward in the hospital, please add a ward first.")
  else:
    print("This is all the ward's detail:")
    #Using for-loop to display the ward details
    for ward_detail in hospital_ward:
      print("Ward Number: {}, Ward Type: {}, Ward Status: {} ".format(ward_detail["Number"], ward_detail["Type"], ward_detail["Status"]))
      #If there has patient in the ward, it will also display the patient info
      if ward_detail['Patient']:
        print("Patients in the ward:")
        for index, patient in enumerate(ward_detail['Patient'], 1):
          print("{}. Name: {}, ID: {}, Age: {}, Gender: {}, Status: {}".format(index, patient["Name"], patient["ID"], patient["Age"], patient["Gender"], patient["Status"]))
      #If there no any patient in the ward, will display this
      else:
        print("This ward don't have any patient.")
   
#Function for Manage physicians' info and status(3) 
physicians_detail= [] 
#Add physician details        
def add_physician_detail():  
  physician_ID= int(input("Enter physician's ID: "))
  physician_name= str(input("Enter physician's name: "))
  physician_age = int(input("Enter physician's age: " ))
  physician_gender = str(input("Enter physician's gender (M/F): " ))
  physician_status = str(input("Enter physician's status: "))
  physician_info = {"Name": physician_name, "ID": physician_ID, "Age": physician_age, "Gender": physician_gender, "Status": physician_status}
  physicians_detail.append (physician_info) 
  #To append the dict (physician_info) into a list (physicians_detail)
#Upadate physicians' info   
def update_physician_detail ():
  update_name= input ("Enter physician name to update info: ")  
#To identify which name need to be updated   
  for physician_info in physicians_detail:
    if physician_info ["Name"]== update_name:
      physician_new_name= input ("Enter a name: ")
      physician_new_id=int (input ("Enter ID: "))
      physician_new_age = int(input("Enter age: " ))
      physician_new_gender = str(input("Enter gender (M/F): " ))
      physician_new_status = str(input("Enter status: "))
#Using for loop to go through the list and if loop to identify the name given
#by user 
#To change all the new value for each key in the dict of the selected name       
      physician_info ["Name"]= physician_new_name
      physician_info["ID"]=physician_new_id
      physician_info["Age"]=physician_new_age
      physician_info["Gender"]=physician_new_gender
      physician_info["Status"]=physician_new_status
      return (physician_info)
#return the values into the list (physicians_detail)  
  print ("\nPhysician's name is not found\n")
#print statement for the for loop if name cannot be identified
#Delete physician detail
def delete_physician_detail(): #function to delete the name input by user
  remove_name=input ("Enter a name to delete: ")  
  for physician_info in physicians_detail:
    if physician_info["Name"]== remove_name:
       physicians_detail.remove (physician_info) #remove method used
       print ("Physician info is removed")
       return (physician_info) #return the value and exit the function
  print ('\nPhysician is not found\n')
#function to display the details using for loop
#Display physician detail
def display_physician_detail():
  for physician_info in physicians_detail: 
    print (physician_info)
    return (physician_info)

#Function for Manage Hospital Transaction Record (4)
hospitaltransaction_rec = []
#Scedule appointment function
def appointments_schedule():
    print ()
    patient_name = input("Enter patient name: ")
    Dr_name = input("Enter the doctor name (Dr.): ")
    Dr_department = input("Enter the doctor department: ")
    date_appointment= input ("Enter the date of appointment (DD.MM.YY): ")
    time_appointment = input("Enter time of appointment (12:MM):")
    transaction_record = {"type": 'Hospital appointment', "patient": patient_name, "doctor": Dr_name,
                          "department": Dr_department, "date_appoint":date_appointment, "time": time_appointment}
    hospitaltransaction_rec.append(transaction_record)
    return (transaction_record)
    #use append methodto add dictionary to a list
    return (transaction_record)
#Billing transaction function
def transaction_bill ():
    print ()
    patient_name = input("Enter patient name: ")
    date_billing = input ("Enter the billing date (DD.MM.YY): ")
    amount_bill = float (input("Enter bill amount (RM): "))
    transaction_record = {"type": 'Hospital billing', "patient": patient_name, "date_bill":date_billing, "amount":amount_bill}
    hospitaltransaction_rec.append(transaction_record)
    #use append method to add dictionary to a list
    return (transaction_record)
#Patient admission 
def admission_patient ():
    print()
    patient_name = input("Enter patient name: ")
    admission_date = input("Enter admission date (DD.MM.YY): ")
    room_number = input("Enter patient room number: ")
    dr_incharge= input ("Enter doctor incharge (Dr.): ")
    transaction_record = {"type": 'Hospital admission', "patient": patient_name, "date_admit":admission_date, "room":room_number, "Dr":dr_incharge}
    hospitaltransaction_rec.append(transaction_record)
    #use append methodto add dictionary to a list
    return (transaction_record)
def view_transaction ():
#Use for loop to see the list of transaction
    for transaction_record in hospitaltransaction_rec:
        print (transaction_record)  
        return (transaction_record)
main ()  
    

          
         
 
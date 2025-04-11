# Add patient to different department
#https://www.w3resource.com/python-exercises/python-basic-exercise-3.php
#Import the 'datetime' module and define 'datetime' and 'timedelta' in order to estimate time
from datetime import datetime, timedelta
#Get the current date and time
now = datetime.now()
#Create a datetime object representing the current date and time
#Display a message indicating what is being printed
print("Today date: ")
#Print the current date and time with Year/Month/Date Hour/Minute
print(now.strftime("%Y/%m/%d %H:%M"))
print("")

#Define the 'queue' function
class Queue:
    def __init__(self):
        self.items = []

    #Keep add the new element to the queue
    def enqueue(self, item,estimated_time):
      self.items.append((item,estimated_time))

    #Follow the principle of queue, which is first in first out (FIFO)
    def dequeue(self):
      if self.is_empty():
        return None
      else:
        return self.items.pop(0)

    #Check the size of queue
    def size(self):
      return len(self.items)

    #Check the queue is empty or not
    def is_empty(self):
      return len(self.items) == 0

    #Using for-loop to print the results
    def print_queue(self):
      if self.is_empty():
        print("This queue is empty")
      else:
        for item,time in self.items:
          print("{} Estimated time need to arrive: {}".format(item,time))

class System:
    #Create 3 queue to store different department data
    def __init__(self):
        self.general_consultation = Queue()
        self.obstetrics_and_gynaecology = Queue()
        self.minor_surgery = Queue()

    #This function is to allow user to add patient to the department they want
    def add_patient(self, patient_name, selection):
      estimated_time = self.get_estimated_time(patient_name,selection)
      #In the queue, there will have one patient add to the queue
      #But in that patient got 2 elements which are ['Name','Estimated Time']
      if selection == '1':
        self.general_consultation.enqueue(patient_name,estimated_time)
      elif selection == '2':
        self.obstetrics_and_gynaecology.enqueue(patient_name,estimated_time)
      elif selection == '3':
        self.minor_surgery.enqueue(patient_name,estimated_time)
      else:
        print("This is an invalid index. Please try again.")

    #This is the function to call the patient from the department
    def call_patient(self, choice):
      #Using the if-else to ensure that department has the patient inside
      #Otherwise, the computer will tell the users that that department queue is empty
      if choice == '1':
        called_patient = self.general_consultation.dequeue()
        #The called patient will got 2 element in the list which is ['Name','Time']
        #Therefore using the [0] to call patient name, [1] to call the time
        if called_patient:
            print("This is the patient that you call: {}".format(called_patient[0]))
        else:
            print("The general consultation queue is empty.")
      elif choice == '2':
        called_patient = self.obstetrics_and_gynaecology.dequeue()
        if called_patient:
            print("This is the patient that you call: {}".format(called_patient[0]))
        else:
             print("The obstetrics and gynaecology queue is empty.")
      elif choice == '3':
        called_patient = self.minor_surgery.dequeue()
        if called_patient:
          print("This is the patient that you call: {}".format(called_patient[0]))
        else:
          print("The minor surgery queue is empty.")
      else:
        print("This is an invalid index. Please try again.")

    #This function is to print all the patient in the different department queue
    def print_queues(self):
      print("")
      print("General Consultation Queue:")
      self.general_consultation.print_queue()
      print("")
      print("Obstetrics and Gynaecology Queue:")
      self.obstetrics_and_gynaecology.print_queue()
      print("")
      print("Minor Surgery Queue:")
      self.minor_surgery.print_queue()
      print("")

    #This function is to tell the users that estimated time need to arrive
    def get_estimated_time(self, patient_name, selection):
      current_time = datetime.now()
      if selection == '1':
        reference_queue = self.general_consultation
      elif selection == '2':
        reference_queue = self.obstetrics_and_gynaecology
      elif selection == '3':
        reference_queue = self.minor_surgery
      else:
        print("Invalid input. Please try again")

      #If the queue is None, the patient will get the current time to be estimated time
      if reference_queue.is_empty():
        return current_time.strftime("%H:%M")
      else:
        #Get the last patient in the reference queue which is [-1]
        #After that, get the time from this patient
        last_patient_time_str = reference_queue.items[-1][1]
        #strptime is to change the time present method
        #https://www.analyticsvidhya.com/blog/2024/01/python-datetime-strptime-function/
        #The function of strptime is to convert the string to the Date/Time
        last_patient_time = datetime.strptime(last_patient_time_str, "%H:%M")
        #https://www.geeksforgeeks.org/how-to-add-time-onto-a-datetime-object-in-python/
        #Calling the timedelta function from datetime library
        #timedelta is the function that define the duration
        time_change = timedelta(minutes=30)
        new_time = last_patient_time + time_change
        return new_time.strftime("%H:%M")

#Create an empty list to store the data
system = System()

#Menu
while True:
    Ask = input("Would you like to call patient? (yes/no) or exit: ").lower()

    #This can allow users to call the patient from the department they want
    if Ask == 'yes':
      print("Which queue would you call from?")
      print(" [1] General Consultation")
      print(" [2] Obstetrics and Gynaecology")
      print(" [3] Minor Surgery")
      choice = input("Please enter the index of the nature that you want to call: ")
      system.call_patient(choice)
      system.print_queues()

    #This can let users to add the patient to the department they want
    elif Ask == 'no':
      patient_name = input("Please enter patient name: ")
      print("")
      print("This is the patient that you want to add: {}".format(patient_name))
      print("Please provide nature of visit:")
      print(" [1] General Consultation")
      print(" [2] Obstetrics and Gynaecology")
      print(" [3] Minor Surgery")
      selection = input("Please enter the index of the nature that you want to visit: ")
      system.add_patient(patient_name, selection)
      system.print_queues()

    #Allow users to stop
    elif Ask == 'exit':
      print("Thanks for using. Bye bye!")
      break

    #Notice users that the input is invalid
    else:
      print("Invalid input. Please try again. Thank you!")
      print("")
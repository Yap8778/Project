#Store the patient details
class Patient:
    def __init__(self, name, age, gender,health_condition):
        self.name = name
        self.age = age
        self.gender = gender
        self.health_condition = health_condition
        self.appointment_date = None

class DoctorAppointmentSystem:
    def __init__(self):
        #Create a few place to store the insert data
        self.waiting_list = [] #Queue
        self.confirm_queue = [] #Normal Python list
        self.cancel_stack = [] #Stack

    #Add patient to the waiting list
    def add_patient(self, name, age, gender,health_condition):
        #Create a patient list to input patient's details
        patient = Patient(name, age, gender,health_condition)
        #After users input the patient's details, it will directly store in the waiting_list to request appointment date
        self.waiting_list.append(patient)
        #To let users know which patient they already input to the waiting_list
        print("Patient {} added to waiting list.".format(name))
    
    #Present the waiting list
    def print_waiting_list(self):
      #If the waiting_list is empty, it will show the statement to let users
      if not self.waiting_list:
        print("No patient in the waiting list. Please add patients' details.")
      else:
        #Print the all the patients' details and give each of them a index, this can let users easily know got how many patients
        print("Waiting List:")
        #enumerate function is to give the index to each elements in the waiting_list
        for idx, patient in enumerate(self.waiting_list):
            print("{}. Name: {}, Age: {}, Gender: {}, Health Condition: {}".format(idx + 1,patient.name,patient.age,patient.gender,patient.health_condition))

    #Present those patient who have making the appointment
    def print_confirm_queue(self):
        print("Confirmed Appointments:")
        for idx, patient in enumerate(self.confirm_queue):
            print("{}. Name: {}, Age: {}, Gender: {}, Health Condition: {}, Appointment Date: {}".format(idx + 1,patient.name,patient.age,patient.gender,patient.health_condition,patient.appointment_date))

    #Show which patients are caneled their appointment
    def print_cancel_list(self):
        print("Current Cancel List:")
        for idx, patient in enumerate(self.cancel_stack):
            print("{}. Name: {}, Age: {}, Gender: {}, Health Condition: {}, Appointment Date: {}".format(idx + 1,patient.name,patient.age,patient.gender,patient.health_condition,patient.appointment_date))

    #Allow user to add patient a appointment date from the waiting list
    def book_appointment(self, appointment_date):
        #As waiting_list is a queue, therefore using the pop(0) to dequeue the first-element, 
        #this is follow the principle of queue which is first in first out
        patient = self.waiting_list.pop(0)
        patient.appointment_date = appointment_date
        #When the waiting_list delete the particular patient information, 
        #the confirm appointment list will get that particular patients information by using the append
        self.confirm_queue.append(patient)
        #This can let users know which patients they have make the appointment
        print("Appointment booked for {} on {}.".format(patient.name,appointment_date))

    #Allow users to cancel particular patient appointment 
    def cancel_appointment(self, idx):
        #Make sure the index inserted by users is valid
        if idx < 1 or idx > len(self.confirm_queue):
            print("Invalid index.")
            return
        else:
            #Removing the patient from the confirm_queue
            patient = self.confirm_queue.pop(idx - 1)
            #At the same time, the patient that delete from the confirm_queue will append to the cancel_stack
            self.cancel_stack.append(patient)
            print("{}'s appointment canceled.".format(patient.name))

    #Allow users to help patient to make the reschedule when the patient is in the cancel stack
    def reschedule(self, idx, appointment_date):
        #If the users select the reshcedule with using index, computer will pop the patient information form the cancel_stack
        patient = self.cancel_stack.pop()
        patient.appointment_date = appointment_date
        #Meanwhile, after the users have rescheduled a new appointment date, it will put the appointment date and that patient information to the confirm_queue
        self.confirm_queue.append(patient)
        print("{}'s appointment rescheduled for {}.".format(patient.name,appointment_date))

#Main menu to let users select the function they want
appointment_system = DoctorAppointmentSystem()
while True:
    print("Doctor Appointment System")
    print("1. Add Patient to Waiting List")
    print("2. Print Waiting List")
    print("3. Book Appointment")
    print("4. Cancel Appointment")
    print("5. Reschedule Appointment")
    print("6. Print Appointment List")
    print("7. Exit")

    print("")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter patient's name: ")
        age = int(input("Enter patient's age: "))
        gender = input("Enter patient's gender: ")
        health_condition = input("Enter patient's health condition: ")
        appointment_system.add_patient(name, age, gender,health_condition)
        print("")

    elif choice == '2':
        appointment_system.print_waiting_list()
        print("")

    elif choice == '3':
        if appointment_system.waiting_list:
            #This will print the name of the first index of patiet to let users know right now what patient they are making appointment
            next_patient = appointment_system.waiting_list[0]
            print("The patient that you are making appointment: {}".format(next_patient.name))
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
            appointment_system.book_appointment(appointment_date)
            print("")
        else:
            print("No patients in the waiting list.")
            print("")

    elif choice == '4':
      if not appointment_system.confirm_queue:
        print("No patients in the confirm queue list.")
        print("")
      else:
        appointment_system.print_confirm_queue()
        #Allow users to use index to delete specific patient
        idx = int(input("Enter index of patient's appointment to cancel: "))
        appointment_system.cancel_appointment(idx)
        print("")

    elif choice == '5':
      if not appointment_system.cancel_stack:
        print("No patients in this list.")
        print("")
      else:
        cancel_patient = appointment_system.cancel_stack[-1]
        #Allow users to select the patient to make the reschedule
        print("The patient that you are making reschedule: {}".format(cancel_patient.name))
        appointment_date = input("Enter new appointment date (YYYY-MM-DD): ")
        appointment_system.reschedule(idx, appointment_date)
        print("")

    elif choice == '6':
        if not appointment_system.confirm_queue:
          print("No patients in the confirm queue list.")
          print("")
        else:
          #This function is to present all the appointment date and each patiet information with sorting the appointment
          #sort(iterable, key=key) sort(iterable) is to put the name of list,stack or queue that need to be sorted
          #key = lambda is to retrieve the appointment_date and check the value form the patient
          #https://www.tutorialspoint.com/How-to-sort-a-Python-date-string-list
          sorted_queue = sorted(appointment_system.confirm_queue, key=lambda date: date.appointment_date)
          for idx, patient in enumerate(sorted_queue):
            print("{}. Name: {}, Age: {}, Gender: {}, Health Condition: {}, Appointment Date: {}".format(idx + 1,patient.name,patient.age,patient.gender,patient.health_condition,patient.appointment_date))
            print("")

    elif choice == '7':
        print("Thanks for your using. Bye Bye.")
        break

    else:
        print("Invalid choice. Please try again.")
        print("")

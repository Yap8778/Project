# Arrange Patient consultation
from datetime import datetime

class Node:
  def __init__(self, name=None, date=None,time=None):
    self.name = name
    self.date = date
    self.time = time
    self.next = None

#Define the 'Linkedlist' function
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  #Allow users to input the patient name, appointment date and time
  def append(self, name, date,time):
    #The newest data insert by user will become new_node
    new_node = Node(name,date,time)
    #The function of strptime is to change the string to the Date/Time
    #This can let the computer to sort with Date/Time
    new_node_datetime = datetime.strptime(f"{date} {time}", "%d/%m/%Y %H:%M")
    #When the linked list is empty, the newest will become the first element in the list
    #So it will become the head and tail at the same time
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      #Assume the current node is the only node, there don't have any node in fron of the current node
      current = self.head
      previous = None
      while current is not None:
        #Using the datetime of the current node to compare with the new added node
        current_datetime = datetime.strptime(f"{current.date} {current.time}", "%d/%m/%Y %H:%M")
        #If the current node datetime is smaller than the new node datetime,
        #The new node will add to the front of current node
        if new_node_datetime < current_datetime:
          break
        #After compare, computer will find the best position to put the new node
        previous = current
        current = current.next

      #These situation is to define where should need to put the new node
      #As the previous is empty, so the new_node will become the head and the previous head will become a normal node
      if previous is None:
        new_node.next = self.head
        self.head = new_node
      #This situation is allow the new node add to the middle of linked list
      else:
        previous.next = new_node
        new_node.next = current

      #Define the new node become the tail
      if new_node.next is None:
        self.tail = new_node

  #Check the list is empty or not
  def is_empty(self):
    return self.head is None

  #Print the linked list
  def printLinkedlist(self):
    #If the linked list is empty, it will tell users
    if self.is_empty():
      print("You haven't add the patient.")
    else:
      current = self.head
      while current:
        print("Patient Name: {} Appointment Date and Time: {} {}".format(current.name, current.date, current.time))
        current = current.next

#Create an empty linked list to store the data
linked_list = LinkedList()

#Menu
while True:
  print("Menu")
  print("----------------------")
  print("1. Add patient name and date")
  print("2. Print the current linked list")
  print("3. Exit")
  selection = input("Which function you wanna use: ")

  #Allow users to input patient name, date and time
  if selection == '1':
    name = input("Please insert the patient name: ").upper()
    date = input("Please insert the date (DD/MM/YYYY): ")
    time = input("Please insert the time with follow 24 hours format like 15:30 (HH/MM)")
    linked_list.append(name, date, time)
    print("You have successful add {} and make the appointment in {} {}".format(name,date,time))
    print("")

  elif selection == '2':
    linked_list.printLinkedlist()
    print("")

  elif selection == '3':
    print("Thanks for your using.Bye bye.")
    break

  else:
    print("This is an invalid insert. Please try again. Thank you!")
    print("")

# Patient Details
patient_detail = []

while True:
    position = 0
    print("\nMenu")
    print("1.Add a patient's name:")
    print("2.Remove a patient’s name, given its position:")
    print("3.Remove a patient’s name, given its value:")
    print("4.Display all patients:")
    print("5.Search for a patient, report its position if found:")
    print("6.Display all patients, sorted in ascending order:")
    print("7.Display the number of patients")
    print("8.Display average number of name, longest name and shortest name")
    print("9.Quit")

    choice = input("Please enter your choice(1-9):")

    if choice == '1':
      patient_name = input("Please add a patient's name:")
      patient_detail.append(patient_name)
      print("Successfully added the patient's name.")

    elif choice == '2':
      if not patient_detail:
        print("Please add the patient's name first.")
      else:
        print(patient_detail)
        position_del= eval(input("Enter the position that you want to remove:"))
        if 1<= position_del <= len(patient_detail):
          del patient_detail[position_del-1]
          print("According to your requirement, right now this is the patient's name:{}".format(patient_detail))
        else:
          print("That position is not found.")

    elif choice == '3':
        if not patient_detail:
          print("Please add the patient's name first.")
        else:
          print(patient_detail)
          patient_name_delete = input("Enter the patient's name you want to delete:")
          confirm = input("Is this patient's name ({}) you want to delete? (y/n) :".format(patient_name_delete ))
          if confirm == 'y':
            if patient_name_delete in patient_detail:
              patient_detail.remove(patient_name_delete)
              print("You have successfully deleted the patient's name, this is the patient's name you have deleted: {}".format(patient_name_delete))
            else:
              print("That patient's name is not found.")
          else:
            print("This operation has been rejected.")

    elif choice == '4':
      if not patient_detail:
          print("Please add the patient's name first.")
      else:
          for name in patient_detail:
            print("These are the patient's name you had key in:{}".format(name))

    elif choice == '5':
      if not patient_detail:
        print("Please add the patient's name first.")
      else:
        print(patient_detail)
        ask = input("What patient's position you want to find:")
        if ask in patient_detail:
          #https://www.simplilearn.com/tutorials/python-tutorial/index-in-python
          position = patient_detail.index(ask)
          user_see_position = position + 1
          print("That patient's position is {}".format(user_see_position))
        else:
          print("Can not find that patient, please try again.")

    elif choice == '6':
      if not patient_detail:
        print("Please add the patient's name first.")
      else:
        print(patient_detail)
        sorted_patient_detail = sorted(patient_detail)
        print("This is all patient's name readings, sorted in ascending order:\n{}.".format(sorted_patient_detail))

    elif choice == '7':
      if not patient_detail:
        print("Please add the patient's name first.")
      else:
        patient_number = len(patient_detail)
        print("This is all the number of patients: {}".format(len(patient_detail)))

    elif choice == '8':
      total=0
      #refer from https://www.geeksforgeeks.org/python-sort-list-according-length-elements/
      sorted_List = sorted(patient_detail, key=lambda x: len(x))
      for names in patient_detail:
        total= total + len(names)
      average_length = total / len(patient_detail)
      print("The average name is {}".format(average_length))
      print("The longest name is {}".format(sorted_List[-1]))
      print("The shortest name is {}".format(sorted_List[0]))

    elif choice == '9':
      print("Thanks for your using, goodbye!")
      break

    else:
         print("Invalid choice. Please enter a valid option.")
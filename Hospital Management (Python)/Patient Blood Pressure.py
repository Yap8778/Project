# Patient Blood pressure

patients_blood_pressure = []

while True:
    position = 0
    print("\nMenu")
    print("1.Add a patient’s blood pressure:")
    print("2.Remove a patient’s blood pressure, given its position:")
    print("3.Remove a patient’s blood pressure, given its value:")
    print("4.Display all blood pressure readings:")
    print("5.Display the sum and average of all blood pressure readings:")
    print("6.Display all blood pressure readings, sorted in ascending order:")
    print("7.Display the blood pressure which has a value more than 120:")
    print("8.Quit")

    choice = input("Please enter your choice(1-8):")

    if choice == '1':
        blood_pressure = eval(input("Please enter the patient blood pressure:"))
        patients_blood_pressure.append(blood_pressure)
        print("Successfully added the patient blood pressure.")

    elif choice == '2':
        if not patients_blood_pressure:
          print("Please key in the blood pressure first.")
        else:
          print(patients_blood_pressure)
          ask = eval(input("Enter the position that you want to remove:"))
          if 1 <= ask <= len(patients_blood_pressure):
            del patients_blood_pressure[ask-1]
            print("According to your requirement, right now this is the blood pressure:{}".format(patients_blood_pressure))
          else:
            print("That position is not found.")

    elif choice == '3':
        if not patients_blood_pressure:
          print("Please key in the blood pressure first.")
        else:
          print(patients_blood_pressure)
          bp_delete = eval(input("Enter the blood pressure you want to delete:"))
          confirm = input("This data of blood pressure {} is the blood pressure you want to delete? (y/n) :".format(bp_delete))
          if confirm == 'y':
            if bp_delete in patients_blood_pressure:
              patients_blood_pressure.remove(bp_delete)
              print("You have successfully deleted the blood pressure, this is the blood pressure you have deleted: {}".format(bp_delete))
            else:
              print("That blood pressure is not found.")
          else:
            print("This operation has been rejected.")

    elif choice == '4':
        if not patients_blood_pressure:
          print("Please key in the blood pressure first.")
        else:
          for bp in patients_blood_pressure:
            print("These are the blood pressure you had key in:{}".format(bp))

    elif choice == '5':
        total_blood_pressure = 0
        if not patients_blood_pressure:
          print("Please key in the blood pressure first.")
        else:
        #Using for-loop to plus all the value and calculate the average
          for bp in patients_blood_pressure:
             total_blood_pressure = total_blood_pressure + bp
             average_bp = total_blood_pressure/len(patients_blood_pressure)
          print("This is the total blood pressure {}.\nThis is the average blood pressure {}.".format(total_blood_pressure, average_bp))

    elif choice == '6':
        if not patients_blood_pressure:
          print("Please key in the blood pressure first.")
        else:
          print("This is the patients blood pressure:\n{}.".format(patients_blood_pressure))
          #sorted help users to arrange the original list into a new list with ascending
          sorted_patients_blood_pressure = sorted(patients_blood_pressure)
          print("This is all blood pressure readings, sorted in ascending order:\n{}.".format(sorted_patients_blood_pressure))

    elif choice == '7':
        high_bp_list = []
        if not patients_blood_pressure:
          print("Please key in the blood pressure first.")
        else:
          for high_bp in patients_blood_pressure:
#help users to detect which elements are more than or equal 120, hence that element will be printed out.
            if high_bp >= 120:
              high_bp_list.append(high_bp)
              
            else:
#if the first value is not the value user want to delete, computer will change to next position to calculate, until detect the same number which is user type.
              pass
              position = position + 1
#This cannot inside the if-else because it will using the previous list then add the new element, so it will print the previous list and the new list
#It will only shows a list that all elements are more than or equal 120 in a list when put it outside the if-else
          print("The blood pressure which has a value more than 120, there are:{}".format(high_bp_list))

    elif choice == '8':
      print("Thanks for your using, goodbye!")
      break

    else:
         print("Invalid choice. Please enter a valid option.")

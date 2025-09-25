student_name = "Ethan"  # Replace with your actual name
current_gpa = 4.0 # Float between 1.0-4.0
study_hours = 31 # Integer (Ex. 25)
social_points = 45# Integer (Ex. 50)
stress_level = 75  # Integer 0-100
#Initializes the foundation of the simulator
print(f"Welcome {student_name}, here are your current stats:\nGPA: {current_gpa}\nStudy Hours: {study_hours}\nSocial Points: {social_points}\nStress Level: {stress_level}")
print("Choose your course load:")
print("(A) Light (12 credits)")  
print("(B) Standard (15 credits)")
print("(C) Heavy (18 credits)")
#User makes a choice of workload
choice = input("Your choice: ")
#Code below checks if the simulation thinks your ready for a heavier load or need a lighter load
if choice == "A":
    if current_gpa <= 2.5 or study_hours <=10:
        print(f"I think you'll be a perfect fit!")
    if current_gpa >= 2.5 or study_hours <=10:
        print(f"I think you can handle a bit more don't doubt yourself.")
    # Use comparison operators to check GPA and adjust variables
elif choice == "B":
     if current_gpa >= 3.75 and study_hours >= 30:
        print("I think you can handle a bit more, don't doubt yourself think about option C!")
     elif current_gpa >= 3.0 or study_hours >= 15:
        if stress_level >= 50:
            print("I think you'll be a perfect fit!")
        else:
            print("You might wanna think about option A if you wanna keep the same stress level.")
     else:
        print(f" I don't think this options for you try option A.")

    # Different logic path
elif choice == "C":
    if current_gpa >= 3.75 or study_hours >= 30:
        if stress_level >= 50:
            print(f"I think you'll be a perfect fit!")
        else:
            print(f"You might wanna think about option B if you wanna keep the same stress level.")
       
    # Heavy load - check if GPA >= 3.5 for different outcomes
else:
    print(f"Invalid input")# Handle invalid input
#Code below handles calculations changes variable values and ask user input
course_options = ["Programming", "Math", "English", "History"]
pick_course = input('Pick your course you would like to study!: Programming, Math, English, History\n')
if pick_course in course_options:
    if pick_course == "Math":
        study_hours += 6
        social_points -= 15
        print(f"Math:\n Credit hours: 4\nEstimated Social Point Loss: -15\nEstimated Study Hours: +6\nCurrent Social Points: {social_points}\nCurrent Study Hours: {study_hours} ")
    if pick_course == "Programming":
        study_hours += 8
        social_points -= 15
        print(f"Programming:\n Credit hours: 3\nEstimated Social Point Loss: -15\nEstimated Study Hours: +8\nCurrent Social Points: {social_points}\nCurrent Study Hours: {study_hours}")
    if pick_course == "History":
        study_hours += 4
        social_points -= 10
        print(f"History:\n Credit hours: 3\nEstimated Social Point Loss: -10\nEstimated Study Hours: +4\nCurrent Social Points: {social_points}\nCurrent Study Hours: {study_hours}")
    if pick_course == "English":
        study_hours += 4
        social_points -= 5
        print(f"English:\n Credit hours: 3\nEstimated Social Point Loss: -5\nEstimated Study Hours: +4\nCurrent Social Points: {social_points}\nCurrent Study Hours: {study_hours}")
elif pick_course not in course_options:
    print(f"Pick a course in the options to study.")

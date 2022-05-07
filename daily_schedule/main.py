from firebase_class import Firebase_Class

my_database = Firebase_Class("/Users/Emilio_1/Documents/CSE/CSE310/cloud-database/hello-world-2ad04-firebase-adminsdk-vebcn-945b8b0773.json")

done = False
while not done:
    # Prompt.
    print("\nMENU:\n1. Display Schedule\n2. Add Class\n3. Update Class\n4. Delete Class\n5. Quit")
    action = input("> ")

    if action == "1":
        my_database.display("semester")

    elif action == "2":

        # Get the data.
        new_class = {
            "name" : input("Name: "),
            "course_code" : input("Course Code: "),
            "semester" : input("Semester: "),
            "year" : input("Year: ")
        }

        # Write to DB.
        my_database.write("semester", new_class["course_code"], new_class)

    elif action == "3":

        # Display current courses.
        my_database.display("semester")

        # Get the course.
        course = input("COURSE CODE TO UPDATE: ")
        entry = input("FIELD TO UPDATE: ")
        data = input("NEW VALUE: ")

        # Update the course.
        my_database.update("semester", course, entry, data)

        # Display updated courses.
        my_database.display("semester")

    elif action == "4":
        # Display current courses.
        my_database.display("semester")

        # Prompt for course.
        del_course = input("COURSE CODE TO DELETE (TYPE ALL TO DELETE ALL COURSES): ")

        # Handle cases.
        if del_course.lower() != "all":
            remove = input("FIELD OR DOCUMENT: ")

            # Field.
            if remove.lower() == "field":
                entry = input("ENTRY TO DELETE: ")
                my_database.delete_field("semester", del_course, entry)
            
            # Document.
            elif remove.lower() == "document":
                my_database.delete_document("semester", del_course)

        # All classes.
        elif del_course.lower() == "all":
            my_database.delete_collection("semester", 10)
        
    elif action == "5":
        done = True



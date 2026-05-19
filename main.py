from branch import BranchManager, create_branch_objects, run_demo, show_menu, validate_branch_data , Branch

raw_branches = [
    {
        "name": "Barn's Tahlia",
        "city": "Jeddah",
        "cups_sold": 420,
        "rating": 4.7,
        "complaints": 2,
        "staff_count": 8
    },
    {
        "name": "Barn's Corniche",
        "city": "Jeddah",
        "cups_sold": 380,
        "rating": 4.5,
        "complaints": 4,
        "staff_count": 7
    },
    {
        "name": "Barn's Olaya",
        "city": "Riyadh",
        "cups_sold": 510,
        "rating": 4.8,
        "complaints": 1,
        "staff_count": 9
    },
    {
        "name": "Barn's Khobar",
        "city": "Khobar",
        "cups_sold": 290,
        "rating": 4.1,
        "complaints": 7,
        "staff_count": 6
    },
    {
        "name": "Barn's Makkah Road",
        "city": "Makkah",
        "cups_sold": 350,
        "rating": 4.3,
        "complaints": 5,
        "staff_count": 7
    }
]


branches = create_branch_objects(raw_branches)
manager = BranchManager(branches)

choice = input("Hello ! \n do you want run demo (1) or try it yourself(2)?")

if choice == "1":
    run_demo(manager)
else:
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            print(manager.generate_report())

        elif choice == "2":
            high_risk = manager.get_high_risk_branches()
            for branch in high_risk:
                print(branch.name)

        elif choice == "3":
            city = input("Enter city name: ")
            matches = manager.find_by_city(city)
            for branch in matches:
                print(branch.name)

        elif choice == "4":
            print("Lets add new branch !\n")
            new_branch={
            "name":input("Enter branch name: "),
                "city": input("Enter city: "),
                "cups_sold": int(input("Enter cups sold: ")),
                "rating": float(input("Enter rating: ")),
                "complaints": int(input("Enter complaints: ")),
                "staff_count": int(input("Enter staff count: "))
            }

            manager.add_branch(new_branch)

        elif choice == "5":
            file_name = input("Enter file name: ")
            print(manager.save_report(file_name))
        
        elif choice == "6":
            print("See you later !")
            break

        else:
            print("INVALID choice, try again")



# Total Numpy concept in the python and change my life every day
import matplotlib.pyplot as plt

# -----------------------------
# Data
# -----------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 150, 180, 250, 300, 280]

students = ["Niraj", "Rahul", "Aman", "Priya", "Riya"]
marks = [90, 75, 95, 88, 82]

hours = [1, 2, 3, 4, 5, 6, 7]
score = [40, 50, 60, 70, 80, 90, 98]

distribution = [45,50,55,60,65,70,75,80,85,90,95,55,60,75,80,90,65,70]

subjects = ["Python", "Java", "C++", "JavaScript"]
votes = [40, 25, 20, 15]

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
temperature = [34,36,35,37,39,38,36]

productA = [120,150,180,200,240]
productB = [100,130,170,220,260]
months2 = ["Jan","Feb","Mar","Apr","May"]

employees = ["A","B","C","D","E"]
salary = [25000,40000,30000,50000,45000]

# -----------------------------
# MENU
# -----------------------------

while True:

    print("\n========== MATPLOTLIB PROJECT ==========")
    print("1. Line Chart")
    print("2. Bar Chart")
    print("3. Scatter Plot")
    print("4. Histogram")
    print("5. Pie Chart")
    print("6. Temperature Graph")
    print("7. Product Comparison")
    print("8. Employee Salary")
    print("9. Save Graph")
    print("0. Exit")

    choice = input("Enter Choice : ")

    # -----------------------------
    if choice == "1":

        plt.figure(figsize=(8,5))

        plt.plot(months,
                 sales,
                 marker="o",
                 linewidth=3,
                 label="Monthly Sales")

        plt.title("Monthly Sales Report")
        plt.xlabel("Months")
        plt.ylabel("Sales")
        plt.grid(True)
        plt.legend()

        plt.show()

    # -----------------------------
    elif choice == "2":

        plt.figure(figsize=(7,5))

        plt.bar(students, marks)

        plt.title("Student Marks")
        plt.xlabel("Students")
        plt.ylabel("Marks")

        plt.show()

    # -----------------------------
    elif choice == "3":

        plt.figure(figsize=(7,5))

        plt.scatter(hours, score)

        plt.title("Study Hours vs Marks")
        plt.xlabel("Study Hours")
        plt.ylabel("Marks")

        plt.grid(True)

        plt.show()

    # -----------------------------
    elif choice == "4":

        plt.figure(figsize=(7,5))

        plt.hist(distribution, bins=8)

        plt.title("Marks Distribution")
        plt.xlabel("Marks")
        plt.ylabel("Frequency")

        plt.show()

    # -----------------------------
    elif choice == "5":

        plt.figure(figsize=(7,7))

        plt.pie(
            votes,
            labels=subjects,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Programming Language Popularity")

        plt.show()

    # -----------------------------
    elif choice == "6":

        plt.figure(figsize=(8,5))

        plt.plot(days,
                 temperature,
                 marker="o",
                 linewidth=3)

        plt.title("Weekly Temperature")
        plt.xlabel("Days")
        plt.ylabel("Temperature")

        plt.grid(True)

        plt.show()

    # -----------------------------
    elif choice == "7":

        plt.figure(figsize=(8,5))

        plt.plot(months2,
                 productA,
                 marker="o",
                 label="Product A")

        plt.plot(months2,
                 productB,
                 marker="o",
                 label="Product B")

        plt.title("Product Sales Comparison")
        plt.xlabel("Months")
        plt.ylabel("Sales")

        plt.legend()

        plt.grid(True)

        plt.show()

    # -----------------------------
    elif choice == "8":

        plt.figure(figsize=(7,5))

        plt.bar(employees, salary)

        plt.title("Employee Salary")
        plt.xlabel("Employee")
        plt.ylabel("Salary")

        plt.show()

    # -----------------------------
    elif choice == "9":

        plt.figure(figsize=(8,5))

        plt.plot(months,
                 sales,
                 marker="o",
                 linewidth=3)

        plt.title("Monthly Sales")

        plt.xlabel("Months")
        plt.ylabel("Sales")

        plt.grid(True)

        plt.savefig("report.png")

        print("\nGraph Saved Successfully as report.png")

        plt.show()

    # -----------------------------
    elif choice == "0":

        print("\nThank You")
        break

    else:

        print("Invalid Choice")
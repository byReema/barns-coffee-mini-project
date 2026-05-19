class Branch:
    def __init__(self, name, city, cups_sold, rating, complaints, staff_count):
        # Store the values as object attributes
        self.name = name
        self.city = city
        self.cups_sold = cups_sold
        self.rating = rating
        self.complaints = complaints
        self.staff_count = staff_count

    def get_sales_category(self):
        
        if self.cups_sold >= 500:
           return "Excellent Sales"
        elif self.cups_sold >= 400 and self.cups_sold < 500:
           return "Strong Sales"
        elif self.cups_sold >= 300 and self.cups_sold < 400:
           return "Average Sales"
        elif self.cups_sold < 300:
           return "Needs Sales Support"

    def get_risk_level(self):
        if self.rating < 4.2 or self.complaints >= 7 :
           return "High"
        elif self.rating < 4.5 or self.complaints >= 4 :
           return "Medium"
        else:
           return "Low"

    def cups_per_staff(self):
        return self.cups_sold / self.staff_count

    def get_advice(self):
        # Hint:
        # Use self.get_risk_level()
        # Use self.get_sales_category()
        if self.get_risk_level() == "High":
           return "Visit this branch and review customer complaints."
        elif self.get_sales_category() == "Excellent Sales" or self.get_risk_level() == "Low":
           return "Top branch. Study what this branch is doing well."
        elif  self.get_sales_category() == "Needs Sales Support":
           return "Create a sales improvement plan for this branch."
        else:
           return "Monitor performance and keep improving service quality."
           
    

def create_branch_objects(raw_data):
    branches = []

    for branch in raw_data:
       
      if not validate_branch_data(branch):
    
        print("skipped: unvalid branch data")
        continue;

      branches.append(    
        Branch(
          branch["name"],
          branch["city"],
          branch["cups_sold"],
          branch["rating"],
          branch["complaints"],
          branch["staff_count"]
    ))
    

    return branches


def validate_branch_data(branch):

    if branch["name"] == "":
      return False
    if branch["city"] == "":
      return False
    if branch["cups_sold"] < 0 or branch["cups_sold"] > 1000:
      return False
    if branch["rating"] < 0 or branch["rating"] > 5:
      return False
    if branch["complaints"] < 0:
      return False
    if branch["staff_count"] < 0:
      return False
    return True


class BranchManager:
    def __init__(self, branches):
      self.branches = branches
    
    def average_cups(self):
        # Loop over self.branches and calculate average cups
        total_cups = 0
        for branch in self.branches:
           total_cups += branch.cups_sold

        average_cups = total_cups / len(self.branches)
        return average_cups

    def average_rating(self):
        # Loop over self.branches and calculate average rating
        total_rating = 0
        for branch in self.branches:
           total_rating += branch.rating

        average_rating = total_rating / len(self.branches)
        return average_rating

    def total_complaints(self):
        # Loop over self.branches and calculate total complaints
        total_complaints = 0
        for branch in self.branches:
           total_complaints += branch.complaints

        return total_complaints

    def find_by_city(self, city):
        # Return branches in the selected city
        high_risk_branches=[]
        for branch in self.branches:
           if branch.city == city :
              high_risk_branches.append(branch)
        return high_risk_branches

    def get_high_risk_branches(self):
        # Return branches with High risk level
        matched_branches=[]
        for branch in self.branches:
           if branch.get_risk_level() == "High" :
              matched_branches.append(branch)
        return matched_branches
    
    def top_selling_branch(self):
        # Return branch with highest cups_sold
        # first branch in the list
        top = self.branches[0]
        for branch in self.branches:
           if top.cups_sold < branch.cups_sold:
              top = branch
        
        return top

    def lowest_selling_branch(self):
        # Return branch with lowest cups_sold
        # first branch in the list
        lowest = self.branches[0]
        for branch in self.branches:
           if lowest.cups_sold > branch.cups_sold:
              lowest = branch
        
        return lowest

    def best_rated_branch(self):
        # Return branch with highest rating
        best = self.branches[0]
        for branch in self.branches:
           if best.rating < branch.rating:
              best = branch
        
        return best
    
    def risk_summary(self):
        summary = {
            "High": 0,
            "Medium": 0,
            "Low": 0
        }

        # Count risk levels here
        for branch in self.branches:
           if branch.get_risk_level() == "High":
              summary["High"] += 1
           elif branch.get_risk_level() == "Medium":
              summary["Medium"] += 1
           else :
              summary["Low"] += 1

        return summary

    def business_insight(self):
        # Use self.average_cups() and self.average_rating()
        if self.average_cups() >= 400 and self.average_rating() >= 4.5:
           return "The branches are performing strongly overall."
        elif self.average_cups() >= 350 and self.average_rating() >= 4.3:
           return "Performance is stable, but some branches need improvement."
        else:
           return "Performance needs attention. Review sales and customer experience."
        
    def generate_branch_details(self):
        report = "Branch Details\n"
        report += "==============\n\n"

        for branch in self.branches:
            report += f"Branch: {branch.name}\n"
            report += f"City: {branch.city}\n"
            report += f"Cups Sold: {branch.cups_sold}\n"
            report += f"Rating: {branch.rating}\n"
            report += f"Complaints: {branch.complaints}\n"
            report += f"Staff Count: {branch.staff_count}\n"
            report += f"Sales Category: {branch.get_sales_category()}\n"
            report += f"Risk Level: {branch.get_risk_level()}\n"
            report += f"Cups per Staff: {branch.cups_per_staff()}\n"
            report += f"Advice: {branch.get_advice()}\n"
            report += "*" * 40 + "\n"
        return report

    def generate_report(self):
        report = "Barn's Branch Performance Report\n"
        report += "================================\n\n"

        # Add company summary here
        report += self.generate_branch_details()
        report += "\n**Company Summary**\n"
        report += "===============\n"

        top = self.top_selling_branch()
        lowest = self.lowest_selling_branch()
        best = self.best_rated_branch()
        risks = self.risk_summary()

        report += f"Total Branches: {len(self.branches)}\n"
        report += f"Average Cups Sold: {self.average_cups():.2f}\n"
        report += f"Average Rating: {self.average_rating():.2f}\n"
        report += f"Total Complaints: {self.total_complaints()}\n"
        report += f"Top Selling Branch: {top.name} -> {top.cups_sold} cups\n"
        report += f"Lowest Selling Branch: {lowest.name} -> {lowest.cups_sold} cups\n"
        report += f"Best Rated Branch: {best.name} -> {best.rating}\n"
        report += f"Risk Summary: {risks}\n"
        report += f"Business Insight: {self.business_insight()}\n"

        return report
    
    def save_report(self, file_name):
      filename = f"{file_name.lower().replace(' ', '_')}_report.txt"

      with open(filename, "w", encoding="utf-8") as file:
        file.write(self.generate_report())

      return f"Report file saved! -- file name: {filename}"
    
def show_menu():
  print("""Barn's Branch Performance Manager
1. Show full report
2. Show high risk branches
3. Search branches by city
4. Add new branch
5. Save report
6. Exit""")

def run_demo(manager):
    # Step 1 :Print menu
    show_menu()
    print()

    # Step 2 :Print full report
    print(manager.generate_report())
    print()

    # Step 3 :Print high-risk branches
    print("High Risk Branches:")
    for branch in manager.get_high_risk_branches():
        print(branch.name)
    print()

    # Step 4 :Add Medina branch
    new_branch = {
        "name": "Barn's Medina",
        "city": "Medina",
        "cups_sold": 380,
        "rating": 4.6,
        "complaints": 2,
        "staff_count": 7
    }

    if validate_branch_data(new_branch):
        branch_obj = Branch(
            new_branch["name"],
            new_branch["city"],
            new_branch["cups_sold"],
            new_branch["rating"],
            new_branch["complaints"],
            new_branch["staff_count"]
        )
        manager.branches.append(branch_obj)
        print("Medina branch added.")
    print()

    # Step 5 :Print updated total branches
    print("Updated total number of branches:", len(manager.branches))
    print()

    # Step 6 :Save report
    print(manager.save_report("barns_demo"))

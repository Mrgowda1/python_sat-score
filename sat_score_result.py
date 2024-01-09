import json

class SATResultsSystem:
    def __init__(self):
        self.data = {}

    def insert_data(self, name, address, city, country, pincode, sat_score):
        passed = "Pass" if sat_score > 30 else "Fail"
        self.data[name] = {
            "Address": address,
            "City": city,
            "Country": country,
            "Pincode": pincode,
            "SAT Score": sat_score,
            "Passed": passed
        }

    def view_all_data(self):
        return json.dumps(self.data, indent=2)

    def get_rank(self, name):
        sorted_data = sorted(self.data.items(), key=lambda x: x[1]["SAT Score"], reverse=True)
        ranks = [item[0] for item in sorted_data]
        return ranks.index(name) + 1 if name in ranks else "Candidate not found"

    def update_score(self, name, new_score):
        if name in self.data:
            self.data[name]["SAT Score"] = new_score
            self.data[name]["Passed"] = "Pass" if new_score > 30 else "Fail"
            return "Score updated successfully"
        else:
            return "Candidate not found"

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
            return "Record deleted successfully"
        else:
            return "Candidate not found"

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file, indent=2)
        print(f"Data saved to {filename}")

def main():
    sat_system = SATResultsSystem()

    while True:
        print("\nSAT Results System Menu:")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Save to file")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            name = input("Enter candidate name: ")
            address = input("Enter address: ")
            city = input("Enter city: ")
            country = input("Enter country: ")
            pincode = input("Enter pincode: ")
            sat_score = int(input("Enter SAT score: "))
            sat_system.insert_data(name, address, city, country, pincode, sat_score)
            print("Data inserted successfully.")

        elif choice == "2":
            print(sat_system.view_all_data())

        elif choice == "3":
            name = input("Enter candidate name: ")
            print(f"Rank: {sat_system.get_rank(name)}")

        elif choice == "4":
            name = input("Enter candidate name: ")
            new_score = int(input("Enter new SAT score: "))
            print(sat_system.update_score(name, new_score))

        elif choice == "5":
            name = input("Enter candidate name to delete: ")
            print(sat_system.delete_record(name))

        elif choice == "6":
            filename = input("Enter the filename to save data (e.g., data.json): ")
            sat_system.save_to_file(filename)

        elif choice == "7":
            print("Exiting the SAT Results System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()

# data input to csv python file

import csv

def user_data_input():
    #Collect data input from user
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")

    return {'name': name, 'age': age, 'email': email}

def populate_to_csv(data, filename='user_data.csv'):
    #Create specified header
    header = ['name', 'age', 'email']

    #Write to csv file target
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)

        #Populate the header if file is empty 
        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(data)

        print("Input data has been written to user_data.csv with header")

def main():
    user_data = user_data_input()
    populate_to_csv(user_data)

if __name__ == "__main__":
    main()
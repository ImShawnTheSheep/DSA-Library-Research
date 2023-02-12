import os
from pymongo import MongoClient

#* database connection
# studData = MongoClient("mongodb+srv://shawnjumawan:vHQmZ4bOyYgQOCyP@shawncluster.ywjvagz.mongodb.net/test")
client = MongoClient("mongodb://localhost:27017/")
db = client['AMSDatabase']
dataset = db['Dataset']

#* function to search the database
def find(key, value):
    cursor = dataset.find({key: value})
    return cursor

#* saves data input from database for searching
class Patient:
    def __init__(self, name, tag,location, login, logout, time_in, time_out):
        self.name = name
        self.tag = tag
        self.location = location
        self.login = login
        self.logout = logout
        self.time_in = time_in
        self.time_out = time_out

#* function to get the patient information
def get_patient_info(patient):
    os.system('cls')
    x = find('name', patient)
    
    # saves patients information to the Patient class
    for cursors in x:
        p = Patient(
            cursors['name'],
            cursors['tag'],
            cursors['location'],
            cursors['login'],
            cursors['logout'],
            cursors['time-in'],
            cursors['time-out']
        )

    # prints out the patient information
    print(
        "-------------- Patient Information -------------\n",
        "Name:     ", p.name, "(", p.tag, ")" + '\n',
        "Location: ", p.location + '\n',
        "Time:     ", p.login, p.logout + '\n'
    )

    # calls the function for finding and displaying close contacts
    close_contact(p.name, p.location, p.time_in, p.time_out)

#* function for finding and displaying close contacts information
def close_contact(name, location, time_in, time_out):
    x = find('location', location)
    count = 0

    for cursors in x:
        if cursors['name'] == name:
            continue
        if (time_in <= cursors['time-out']) and (time_out >= cursors['time-in']):
            count +=1
            print(
                "# ", count, " --------------------------------------\n",
                "Name:     ", cursors['name'], "(", cursors['tag'], ")" + '\n', 
                "Location: ", cursors['location'] + '\n',
                "Time:     ", cursors['login'], cursors['logout'] + '\n'
            )

    print("Number of close contacts: ", count)

if __name__ == '__main__':
    os.system('cls')
    bool = True

    while bool:
        patient = input("Enter patient's name: ")
        check = dataset.find_one({'name': patient})

        if check is None:
            print("Error: Data does not exist in database\n")
            os.system('pause')
        else:
            get_patient_info(patient)

        check = input("Would like to search for another patient?[Y/n]\n")
        
        if (check == 'y') or (check == 'Y') or (check == 'Yes') or (check == 'yes'):
            os.system('cls')
            continue
        else:
            bool = False
            
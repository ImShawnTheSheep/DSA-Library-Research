import database as db


# This is the main function
if __name__ == "__main__":

    cursor = db.find('tag', 'visitor')

    for cursors in cursor:
        print(cursors['name'])

    print("Hello World")
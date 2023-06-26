import json

def get_credentials():
    user = input('Type user name: ')
    password = input('Type password: ')
    return user, password

def write_pwdb(pwdb):
    fn = 'database.json'
    with open(fn, 'w') as f:
        json.dump(pwdb, f)

def read_pwdb():
    try:
        with open('database.json', 'r') as f:
            pwdb = json.load(f)
    except FileNotFoundError:
        pwdb = {}
    return pwdb

def add_user(user, password, pwdb):
    if user not in pwdb:
        pwdb[user] = password
    return pwdb

def authenticate_user(user, password, pwdb):
    if user in pwdb:
        print("user is in database")
        stored_password = pwdb[user]
        # we compare the stored password with the one provided by the user
        if password == stored_password:
            print("Password is correct!")
        else:
            print("Incorrect password!")
    else:
        print("user not in database, adding it")
        add_user(user, password, pwdb)

if __name__ == '__main__':
    # We get the database or create a new one if it doesn't exist
    pwdb = read_pwdb()

    # Get the credentials of the user
    user, password = get_credentials()

    # Check if the user exists in the DB, and adds it if not
    authenticate_user(user, password, pwdb)
    
    # Updates/writes database to file
    write_pwdb(pwdb)
    

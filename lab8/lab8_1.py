import sqlite3 as sq

def createTableCourier(cur):
    cur.execute("""
                CREATE TABLE courier (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    last_name VARCHAR(256),
                    first_name VARCHAR(256),
                    patronymic_name VARCHAR(256),
                    passport_number VARCHAR(32),
                    date_of_birth DATE,
                    hiring_date DATE,
                    start_of_working_day TIME,
                    end_of_working_day TIME,
                    city VARCHAR(64),
                    street VARCHAR(64),
                    house VARCHAR(8),
                    apartment VARCHAR(8),
                    phone_number VARCHAR(16));
                """)
    
def createTableSender(cur):
    cur.execute("""
                CREATE TABLE sender (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    last_name VARCHAR(256),
                    first_name VARCHAR(256),
                    patronymic_name VARCHAR(256),
                    date_of_birth DATE,
                    `index` VARCHAR(10),
                    city VARCHAR(64),
                    street VARCHAR(64),
                    house VARCHAR(8),
                    apartment VARCHAR(8),
                    phone_number VARCHAR(16));
                """)
    
def insertSampleCourier(cur):
    courier = ("Ivanov", "Ivan", "Ivanovich", "7777 777777", "30.05.1998", "19.10.2023", "8:00:00", "17:00:00", "Moscow",
               "Pushkina", "1 litera a", "3-1", "+79777777777")
    cur.execute("""
                INSERT INTO courier (last_name, first_name, patronymic_name, passport_number, date_of_birth,
                hiring_date, start_of_working_day, end_of_working_day, city, street, house, apartment, phone_number)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
                """, courier)

def insertSampleSender(cur):
    sender = ("Viktorov", "Viktor", "Viktorovich", "10.06.1973", "350003", "Moscow",
               "Kolotushkina", "13", "68", "+79799999999")
    cur.execute("""
                INSERT INTO sender (last_name, first_name, patronymic_name, date_of_birth, `index`,
                city, street, house, apartment, phone_number)
                VALUES(?,?,?,?,?,?,?,?,?,?)
                """, sender)
    
def updateSampleSender(cur):
    sender = ("Viktorov", "Viktor", "Viktorovich", "10.06.1973")
    cur.execute("""
                UPDATE sender SET phone_number="+79899113542"
                WHERE last_name=? AND first_name=? AND patronymic_name=? AND date_of_birth=?;
                """, sender)

if __name__ == "__main__":
    connection = sq.connect('lab8/orders1.db')
    cursor = connection.cursor()
    createTableCourier(cursor)
    createTableSender(cursor)
    insertSampleCourier(cursor)
    insertSampleSender(cursor)
    updateSampleSender(cursor)
    connection.commit()
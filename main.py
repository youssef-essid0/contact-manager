import sqlite3

conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT
)
""")

def add_contact(name, phone):
    cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()

def show_contacts():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    for c in contacts:
        print(c)

while True:
    print("\n1. Ajouter contact")
    print("2. Afficher contacts")
    print("3. Quitter")

    choice = input("Choix : ")

    if choice == "1":
        name = input("Nom : ")
        phone = input("Téléphone : ")
        add_contact(name, phone)

    elif choice == "2":
        show_contacts()

    elif choice == "3":
        break

conn.close()

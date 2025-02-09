import sqlite3
import os, json

config = json.load(open('src/config.json'))
magnetDatabase = config['magnetDatabase']
database = config['database']

input1 = input('Do you want to run migration for magnet link database? Y/[n]: ')
if input1 == 'y':
    if os.path.exists(magnetDatabase):
        os.remove(magnetDatabase)
        print('[-] Database already exists. Deleting it.')

    conn = sqlite3.connect(magnetDatabase)
    print('[+] Magnetlink Database opened successfully.')

    conn.execute('''CREATE TABLE data
            (key       TEXT PRIMARY KEY,
            date      INT,
            magnetlink TEXT
            );''')

    print('[+] Table data created successfully.')

    conn.close()

input1 = input('Do you want to run migration for Torrent Hunt database? Y/[n]: ')
if input1 == 'y':
    if os.path.exists(database):
        os.remove(database)
        print('[-] Database already exists. Deleting it.')

    conn = sqlite3.connect(database)
    print('[+] Database opened successfully.')

    conn.execute('''CREATE TABLE users
            (UserId       INTEGER PRIMARY KEY
            );''')

    print('[+] Table users created successfully.')

    conn.execute('''CREATE TABLE settings
            (ownerId       INTEGER PRIMARY KEY,
            language       TEXT DEFAULT "english",
            defaultSite    TEXT DEFAULT "piratebay",
            restrictedMode INTEGER DEFAULT 1
            );''')

    print('[+] Table settings created successfully.')

    conn.close()
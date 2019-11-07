import os
import sqlite3 as sql
import sys

if __name__ == '__main__':
    with sql.connect(os.path.join(sys.path[0], "names")) as conn:
        curs = conn.cursor()
        address = curs.execute("SELECT * FROM address").fetchall()[0]
        curs.execute("DELETE FROM address")
        curs.execute("DELETE FROM name")
        conn.commit()

    os.remove(address[0])

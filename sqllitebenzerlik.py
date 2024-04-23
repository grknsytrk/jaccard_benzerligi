import sqlite3

def jaccard_benzerligi(metin1, metin2):
    set1 = set(metin1.split())
    set2 = set(metin2.split())
    kesisim = set1.intersection(set2)
    birlesim = set1.union(set2)
    return len(kesisim) / len(birlesim)

metin1 = "Bu bir python ödevidir."
metin2 = "Bu bir python ödevi değildir."
conn = sqlite3.connect('metinler.db')
c = conn.cursor()
c.execute('''CREATE TABLE metinler (id INTEGER PRIMARY KEY, metin TEXT)''')
c.execute("DELETE FROM metinler")
c.execute("INSERT INTO metinler (metin) VALUES (?)", (metin1,))
c.execute("INSERT INTO metinler (metin) VALUES (?)", (metin2,))
conn.commit()
conn.close()

benzerlik = jaccard_benzerligi(metin1, metin2)
print("Benzerlik Oranı:", benzerlik)

with open('benzerlik_durumu.txt', 'w') as f:
    f.write("Benzerlik Oranı: " + str(benzerlik))

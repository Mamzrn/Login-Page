import sqlite3
import csv

# انشاء قاعدة بيانات جديدة او الاتصال بالقاعدة القائمة
conn = sqlite3.connect('accounts.db')

# إنشاء جدول accounts
conn.execute('''CREATE TABLE IF NOT EXISTS accounts
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         username TEXT NOT NULL,
         email TEXT NOT NULL,
         password TEXT NOT NULL);''')

# إدخال بيانات مسؤول
conn.execute("INSERT INTO accounts (username, email, password) VALUES ('admin', 'admin@admin.com', '123')")

# حفظ التغييرات
conn.commit()

# استيراد البيانات من ملف CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        conn.execute("INSERT INTO accounts (username, email, password) VALUES (?, ?, ?)", (row[0], row[1], row[2]))

# تصدير البيانات إلى ملف CSV
cursor = conn.execute("SELECT username, email, password from accounts")
with open('export_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'Email', 'Password'])
    writer.writerows(cursor)

# إغلاق الاتصال بقاعدة البيانات
conn.close()

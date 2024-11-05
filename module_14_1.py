import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создайте таблицу Users, если она ещё не создана.
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

# Заполните её 10 записями:
# for i in range(1, 11):
#     cursor.execute('INSERT INTO USERS (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))

# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# for i in range(1, 11, 2):
#     cursor.execute('UPDATE Users set balance = ? WHERE username = ?', ('500', f'User{i}'))

# Удалите каждую 3ую запись в таблице начиная с 1ой:
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM USERS WHERE Username = ?', (f'User{i}',))

# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в
# следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

connection.commit()
connection.close()
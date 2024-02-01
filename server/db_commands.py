import sqlite3
class MyDB:
   
	def __init__(self) -> None:
		self.con = sqlite3.connect("data.db", check_same_thread=False)
		self.cur = self.con.cursor()
	
	def create_user(self, id , name ,email , password):
		text_db_command = f"""
    INSERT INTO users
    (name,email,password) VALUES
    ('{name}', '{email}' , '{password}');
"""
		self.cur.execute(text_db_command)
		self.con.commit()
		self.con.close()
  
	def get_users(self):
		self.cur.execute('''SELECT * from users''')
		result = self.cur.fetchall()
		return result

  
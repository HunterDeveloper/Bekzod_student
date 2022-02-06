import sqlite3
class royhat:
    def __init__(self, db_name):
        self.con=sqlite3.connect(db_name, check_same_thread=False)
        self.con.row_factory=sqlite3.Row
        self.cursor=self.con.cursor()

    def db_exequite(self, sql, commit=False, fetchone=False, fechall=False):
        self.conn=sqlite3.connect('royhat.db', check_same_thread=False)
        connection =self.conn
        cursor = connection.cursor()
        data=None
        cursor.execute(sql)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fechall:
            data = cursor.fetchall()

        connection.close()

        return data
    
    def get_users(self):
        sql="SELECT id FROM royhat"
        self.db_exequite(sql, fechall=True)
    

    # bu funksiya db ga foydalanuvchini qo'shadi
    def add_product(self, id ):
        sql = f""" INSERT INTO royhat VALUES ({id}, "", "", 0, "") """
        self.db_exequite(sql,commit=True)
        
    def edit_name(self, id, name):
        sql = f""" UPDATE royhat
                SET ism="{name}"
                WHERE id={id};"""
        self.db_exequite(sql,True)
        
    def edit_surname(self, id, surname):
        sql = f""" UPDATE royhat
                SET familiyasi="{surname}"
                WHERE id={id};"""
        self.db_exequite(sql,True)
        
    def edit_phone(self, id, phone):
        sql = f""" UPDATE royhat
                SET telefonraqam={phone}
                WHERE id={id};"""
        self.db_exequite(sql,True)
        
    def edit_group(self, id, group):
        sql = f""" UPDATE royhat
                SET guruh="{group}"
                WHERE id={id};"""
        self.db_exequite(sql,True)

    def check_user(self, id):
        sql = f"SELECT id FROM royhat WHERE id={id}"
        res=self.db_exequite(sql,fechall=True)
        if len(res)==0: return False
        else : return True
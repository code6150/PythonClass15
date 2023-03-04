import pymysql

con = pymysql.connect(host="127.0.0.1", user="root", password="1234", database="python")
cur = con.cursor()

cur.execute("create table if not exists `user` (`id` char(32) not null primary key, `pw` char(32) not null, `email` text not null, `name` text not null)")

def insert_user(id, pw, email, name):
    try:
        cur.execute(f"insert into `user` (`id`, `pw`, `email`, `name`) values('{id}', '{pw}', '{email}', '{name}')")
        con.commit()
        return True
    except:
        return False

def get_user(id):
    # 데이터베이스에서 id, pw 회원정보를 찾는 일.
    # get_user('test123') -> 아이디가 같으면 무조건 데이터는 리턴
    #                     -> 일치하는 아이디가 아예 없으면, 데이터는 리턴되지 않음.
    cur.execute(f"select * from `user` where `id` = '{id}'")
    cur.fetchall()

get_user('test123')
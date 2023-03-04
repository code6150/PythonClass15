from tkinter import messagebox
import tkinter as tk
import re
import database

# python 에서 다른 클래스 상속 (부모 클래스)
# Frame -> master = None -> 내가 최상위 창
#       -> master = ??? -> ??? 의 자식 창
class Login(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_login_form()

    def sign_up_button(self):
        global window
        if self.login_mode:
            self.login_button.destroy()
            self.sign_button.destroy()
            self.login_mode = False
            # 회원가입 부분.
            self.name_label = tk.Label(self.master, text="이름 : ")
            self.email_label = tk.Label(self.master, text="이메일 : ")
            self.name_label.grid(row=2, column=0)
            self.email_label.grid(row=3, column=0)

            self.email_box = tk.StringVar()
            self.name_box = tk.StringVar()

            self.name_var = tk.Entry(self.master, textvariable=self.name_box)
            self.email_var = tk.Entry(self.master, textvariable=self.email_box)

            self.name_var.grid(row=2,column=1)
            self.email_var.grid(row=3,column=1)

            self.sign_button = tk.Button(self.master, text="회원가입", command=self.sign_up_button)
            self.sign_button.grid(row=4,column=1)

            window.geometry("200x250")

        else:
            dic = {
                "아이디" : self.id_box,
                "비밀번호" : self.pw_box,
                "이름" : self.name_box,
                "이메일" : self.email_box
            }
            for key in dic:
                if not dic[key].get():
                    messagebox.showerror("오류!",f"{key}이/가 비어있다구요 싸발")
                    return

            kor_pattern = re.compile('^[가-힣]+$')
            if not kor_pattern.match(self.name_box.get()):
                messagebox.showerror('오류!','이름은 한국어로 입력하세요!')
                return

            pw1_pattern = re.compile('^[a-z0-9]+$')
            if pw1_pattern.match(self.pw_box.get()):
                messagebox.showerror("오류!","대문자 하나이상을 포함시키세요.")

            pw2_pattern = re.compile('^[a-z0-9A-Z]+$')
            if pw2_pattern.match(self.pw_box.get()):
                messagebox.showerror("오류!", "특수문자 하나 이상을 포함시키세요.")

            p = re.compile('^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-z]+$')
            if not p.match(self.email_box.get()):
                messagebox.showerror("오류","올바르지 않은 이메일 형식입니다!")
                return

            # 회원가입을 데이터 베이스에 저장/이미 있다면, 회원가입 막음.
            if not database.insert_user(self.id_box.get(), self.pw_box.get(), self.email_box.get(), self.name_box.get()):
                messagebox.showerror("오류!","이미 존재하는 아이디입니다.")
                return
            else:
                messagebox.showinfo("환영합니다!","예 뭐..")

            window.geometry("200x100")
            # 다시 로그인 모드로 활성화 ( 로그인 창 )
            self.name_label.destroy()
            self.email_label.destroy()
            self.name_var.destroy()
            self.email_var.destroy()
            self.sign_button.destroy()
            self.login_button = tk.Button(self.master, text="로그인")
            self.login_button.grid(row=2, column=0)
            self.sign_button = tk.Button(self.master, text="회원가입", command=self.sign_up_button)
            self.sign_button.grid(row=2, column=1)
            self.login_mode = True
            window.geometry("200x200")

    def login_button_click(self):
        if not self.id_box.get():
            messagebox.showerror("오류!","아이디가 비어있습니다.")
            return
        if not self.pw_box.get():
            messagebox.showerror("오류!","비밀번호가 비어있습니다.")
            return
        user_data = database.get_user(self.id_box.get())
        if user_data == self.pw_box.get():
            messagebox.showinfo('환영합니다!', f'{user_data["name"]}({user_data["email"]})님 환영합니다!')

    def init_login_form(self):
        self.master.title("login")
        tk.Label(self.master, text="ID : ").place(x=0, y=0)
        tk.Label(self.master, text="PW : ").place(x=0, y=20)

        self.id_box = tk.StringVar()
        self.pw_box = tk.StringVar()

        tk.Entry(self.master, textvariable=self.id_box).grid(row=0, column=1)
        tk.Entry(self.master, textvariable=self.pw_box).grid(row=1, column=1)

        self.login_button = tk.Button(self.master, text = "로그인", command=self.login_button_click)
        self.login_button.grid(row=2,column=0)
        self.login_mode = True

        self.sign_button =tk.Button(self.master, text = "회원가입",command=self.sign_up_button)
        self.sign_button.grid(row=2, column=1)

window = tk.Tk()
Login = Login(window)
Login.mainloop()
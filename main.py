import tkinter

# 창 생성
window = tkinter.Tk()

# 아이디, 패스워드 입력받는 Strinig Variable 클래스 생성
id = tkinter.StringVar()
pw = tkinter.StringVar()

up_name, up_id, up_pw, up_check, up_email = \
    tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(),

#로그인 버튼을 눌렀을 때 실행 할 함수

def login_button_click():
    print(id.get())
    print(pw.get())

# 회원가입 버튼을 눌렀을 때 실행 할 함수

def singup_check_button_click():
    if up_pw.get() == up_check.get():
        pass
    else:
        print("비밀번호가 다릅니다!")
    pass


# 창 설정
window.title("f")

def signup_button_click():

    new_window = tkinter.Tk()

    new_window.title("회원가입")

    #각 입력 칸에 대한 라벨
    tkinter.Label(new_window, text="이름 : ").grid(row=0,column=0)
    tkinter.Label(new_window, text = "ID : ").grid(row=1,column=0)
    tkinter.Label(new_window, text = "PW : ").grid(row=2, column=0)
    tkinter.Label(new_window, text="email : ").grid(row=3, column=0)

    # 각 입력칸 배치
    tkinter.Entry(new_window, textvariable=up_name).grid(row=0,column=1)
    tkinter.Entry(new_window, textvariable=up_id).grid(row=1, column=1)
    tkinter.Entry(new_window, textvariable=up_pw).grid(row=2, column=1)
    tkinter.Entry(new_window, textvariable=up_check).grid(row=3, column=1)
    tkinter.Entry(new_window, textvariable=up_email).grid(row=4, column=1)

    tkinter.Button(new_window, text="회원가입", command=singup_check_button_click).grid(row=5,column=1)

    new_window.mainloop()

window.resizable(False, False)

tkinter.Label(window, text="ID : ").grid(row=0,column=0)
tkinter.Label(window, text="PW : ").grid(row=1,column=0)

# 사용자가 입력하는 데이터를 저장하는 TextBox ( StringVar )
tkinter.Entry(window, textvariable=id).grid(row=0,column=1)
tkinter.Entry(window, textvariable=pw, show="a").grid(row=1,column=1)

# 버튼 추가
tkinter.Button(window, text="회원가입", command=signup_button_click).grid(row=2,column=0,padx=20)
tkinter.Button(window, text="로그인", command=login_button_click).grid(row=2,column=1,padx=20)

# 창 띄우기
window.mainloop()
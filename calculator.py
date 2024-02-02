import tkinter as tk

win = tk.Tk()
win.geometry('600x650')
win.title('졸업학점계산기(22.12.07) made by leeeejsp')
label11 = tk.Label(win,text='졸업학점계산기',height=1,font=('맑은 고딕',28,'bold'))
label11.grid(row=0,column=0,padx = 5, pady = 10)

label21 = tk.Label(win,text='해당하는 학번에 체크해주세요.(필수)',font=('맑은 고딕',13))
label21.place(x=10,y=70)

hackbun_var = tk.IntVar() #학번체크--------------------------------------------------
bt_18 = tk.Radiobutton(win, text='18학번',value = 18, variable=hackbun_var)
bt_18.place(x=10,y=100)
bt_19 = tk.Radiobutton(win, text='19학번',value = 19, variable=hackbun_var)
bt_19.place(x=100,y=100)
bt_20 = tk.Radiobutton(win, text='20학번',value = 20, variable=hackbun_var)
bt_20.place(x=200,y=100)
bt_21 = tk.Radiobutton(win, text='21학번',value = 21, variable=hackbun_var)
bt_21.place(x=300,y=100)

label31 = tk.Label(win,text='단일전공 or 복수전공에 체크해주세요.(필수)',font=('맑은 고딕',13))
label31.place(x=10,y=140)

major_var = tk.IntVar() #단일전공 or 복수전공-----------------------------------------------------
one_mj = tk.Radiobutton(win, text='단일전공',value = 1, variable=major_var)
one_mj.place(x=10,y=170)
two_mj = tk.Radiobutton(win, text='복수전공',value = 2, variable=major_var)
two_mj.place(x=100,y=170)

#------------------------------------입력시작-----------------------------------------------------
label41 = tk.Label(win,text='학점을 입력해주세요. ex) 7학점이면 --> 7 ,0학점이면 --> 0',font=('맑은 고딕',13))
label41.place(x=10,y=210)

label51 = tk.Label(win,text='▶ 기초교양',font=('맑은 고딕',13))
label51.place(x=10,y=240)
ent52 = tk.Entry(win,bg='white',font=('맑은 고딕',12))
ent52.place(x=130,y=240)

label61 = tk.Label(win,text='▶ 균형교양',font=('맑은 고딕',13))
label61.place(x=10,y=270)
ent62 = tk.Entry(win,bg='white',font=('맑은 고딕',12))
ent62.place(x=130,y=270)
label63 = tk.Label(win,text='<<특화+균교',font=('맑은 고딕',13))
label63.place(x=330,y=270)

label71 = tk.Label(win,text='▶ 학문기초',font=('맑은 고딕',13))
label71.place(x=10,y=300)
ent72 = tk.Entry(win,bg='white',font=('맑은 고딕',12))
ent72.place(x=130,y=300)

label81 = tk.Label(win,text='▶ 전공필수',font=('맑은 고딕',13))
label81.place(x=10,y=330)
ent82 = tk.Entry(win,bg='white',font=('맑은 고딕',12))
ent82.place(x=130,y=330)

label91 = tk.Label(win,text='▶ 전공선택',font=('맑은 고딕',13))
label91.place(x=10,y=360)
ent92 = tk.Entry(win,bg='white',font=('맑은 고딕',12))
ent92.place(x=130,y=360)

label101 = tk.Label(win,text='▶ 자유선택',font=('맑은 고딕',13))
label101.place(x=10,y=390)
ent102 = tk.Entry(win,bg='white',font=('맑은 고딕',12))
ent102.place(x=130,y=390)

label111 = tk.Label(win,text='결과는?',font=('맑은 고딕',13))
label111.place(x=10,y=420)
#---------------------------------------출력레이블----------------------
label112 = tk.Label(win)
label112.place(x=150,y=460)
label122 = tk.Label(win)
label122.place(x=150,y=480)
label132 = tk.Label(win)
label132.place(x=150,y=500)
label142 = tk.Label(win)
label142.place(x=150,y=520)
label152 = tk.Label(win)
label152.place(x=150,y=540)
label162 = tk.Label(win)
label162.place(x=150,y=560)
label172 = tk.Label(win)
label172.place(x=150,y=580)

#--------------------------------------함수 생성---------------------------------
def cal21():
    if hackbun_var.get() >= 19 and hackbun_var.get() <= 21 and major_var.get() == 1: # ---19,20,21학번 단일전공
        simjun = 0
        if int(ent92.get()) > 30:
            simjun = int(ent92.get()) - 30  # 심화전공 계산

        gyo_total = int(ent52.get()) + int(ent62.get()) + int(ent72.get())  # 교양 10학점 초과 자선계산
        gyo_jasun = 0
        if gyo_total > 36 and gyo_total <= 46:
            gyo_jasun = gyo_total - 36
        elif gyo_total > 46:
            gyo_jasun = 10  # 교양 초과학점이 10학점을 넘어간다면?
        jun_jasun = 0
        if simjun > 27:  # 초과 심화전공 자선으로 넘어가는 계산
            jun_jasun = simjun - 27
        jasun = int(ent102.get()) + gyo_jasun + jun_jasun
        label112.configure(
            text='기초교양 분야에서 %d 학점이 부족합니다.' % (10 - int(ent52.get())) if int(ent52.get()) < 10 else '기초교양 clear')
        label122.configure(
            text='균형교양 분야에서 %d 학점이 부족합니다.' % (14 - int(ent62.get())) if int(ent62.get()) < 14 else '균형교양 clear')
        label132.configure(text='학문기초(대학별교양) 분야에서 %d학점이 부족합니다.' % (12 - int(ent72.get())) if int(
            ent72.get()) < 12 else '학문기초(대학별교양) clear')
        label142.configure(
            text='전공필수 분야에서 %d학점이 부족합니다.' % (12 - int(ent82.get())) if int(ent82.get()) < 12 else '전공필수 clear')
        label152.configure(
            text='전공선택 분야에서 %d학점이 부족합니다.' % (30 - int(ent92.get())) if int(ent92.get()) < 30 else '전공선택 clear')
        label162.configure(text='심화전공 분야에서 %d학점이 부족합니다. (전공선택을 더 들으세요.)' % (27 - simjun) if simjun < 27 else '심화전공 clear')
        label172.configure(text='자유선택 분야에서 %d학점이 부족합니다.' % (25 - jasun) if jasun < 25 else '자유선택 clear')

    if hackbun_var.get() >= 19 and hackbun_var.get() <= 21 and major_var.get() == 2: # ---19,20,21학번 복수전공
        simjun = 0
        if int(ent92.get()) > 30:
            simjun = int(ent92.get()) - 30  # 복수전공은 심화전공을 자선으로 넘겨버린다.
        gyo_total = int(ent52.get()) + int(ent62.get()) + int(ent72.get())  # 교양 10학점 초과 자선계산
        gyo_jasun = 0
        if gyo_total > 36 and gyo_total <= 46:
            gyo_jasun = gyo_total - 36
        elif gyo_total > 46:
            gyo_jasun = 10  # 교양 초과학점이 10학점을 넘어간다면?
        jasun = int(ent102.get()) + gyo_jasun + simjun
        label112.configure(
            text='기초교양 분야에서 %d 학점이 부족합니다.' % (10 - int(ent52.get())) if int(ent52.get()) < 10 else '기초교양 clear')
        label122.configure(
            text='균형교양 분야에서 %d 학점이 부족합니다.' % (14 - int(ent62.get())) if int(ent62.get()) < 14 else '균형교양 clear')
        label132.configure(text='학문기초(대학별교양) 분야에서 %d학점이 부족합니다.' % (12 - int(ent72.get())) if int(
            ent72.get()) < 12 else '학문기초(대학별교양) clear')
        label142.configure(
            text='전공필수 분야에서 %d학점이 부족합니다.' % (12 - int(ent82.get())) if int(ent82.get()) < 12 else '전공필수 clear')
        label152.configure(
            text='전공선택 분야에서 %d학점이 부족합니다.' % (30 - int(ent92.get())) if int(ent92.get()) < 30 else '전공선택 clear')
        #label162.configure(text='심화전공 분야에서 %d학점이 부족합니다. (전공선택을 더 들으세요.)' % (27 - simjun) if simjun < 27 else '심화전공 clear')
        label172.configure(text='자유선택 분야에서 %d학점이 부족합니다.' % (52 - jasun) if jasun < 52 else '자유선택 clear')

    if hackbun_var.get() == 18 and major_var.get() == 1: #-------18학번 단일전공------------------------------------------
        simjun = 0
        if int(ent92.get()) > 30:
            simjun = int(ent92.get()) - 30 # 심화전공 계산

        gyo_total = int(ent52.get()) + int(ent62.get()) + int(ent72.get())
        gyo_jasun = 0
        if gyo_total > 33 and gyo_total <= 43:
            gyo_jasun = gyo_total - 33
        elif gyo_total > 43:
            gyo_jasun = 10

        jun_jasun = 0
        if simjun > 27:
            jun_jasun = simjun - 27
        jasun = int(ent102.get()) + gyo_jasun + jun_jasun
        label112.configure(text='기초교양 분야에서 %d 학점이 부족합니다.' % (7-int(ent52.get())) if int(ent52.get())<7 else '기초교양 clear')
        label122.configure(text='균형교양 분야에서 %d 학점이 부족합니다.' % (14-int(ent62.get())) if int(ent62.get())<14 else '균형교양 clear')
        label132.configure(text='학문기초(대학별교양) 분야에서 %d학점이 부족합니다.' % (12 - int(ent72.get())) if int(ent72.get())<12 else'학문기초(대학별교양) clear')
        label142.configure(text='전공필수 분야에서 %d학점이 부족합니다.' % (12 - int(ent82.get())) if int(ent82.get()) < 12 else '전공필수 clear')
        label152.configure(text='전공선택 분야에서 %d학점이 부족합니다.' % (30 - int(ent92.get())) if int(ent92.get()) < 30 else '전공선택 clear')
        label162.configure(text='심화전공 분야에서 %d학점이 부족합니다. (전공선택을 더 들으세요.)' % (27 - simjun) if simjun < 27 else '심화전공 clear')
        label172.configure(text='자유선택 분야에서 %d학점이 부족합니다.' % (28 - jasun) if jasun < 28 else '자유선택 clear')

    if hackbun_var.get() == 18 and major_var.get() == 2: #-------18학번 복수전공------------------------------------------
        simjun = 0
        if int(ent92.get()) > 30:
            simjun = int(ent92.get()) - 30 # 복수전공은 심화전공을 자선으로 넘겨버린다.

        gyo_jasun = 0
        gyo_total = int(ent52.get()) + int(ent62.get()) + int(ent72.get())
        if gyo_total > 33 and gyo_total <= 43:
            gyo_jasun = gyo_total - 33
        elif gyo_total > 43:
            gyo_jasun = 10

        jasun = int(ent102.get()) + gyo_jasun + simjun
        label112.configure(text='기초교양 분야에서 %d 학점이 부족합니다.' % (7-int(ent52.get())) if int(ent52.get())<7 else '기초교양 clear')
        label122.configure(text='균형교양 분야에서 %d 학점이 부족합니다.' % (14-int(ent62.get())) if int(ent62.get())<14 else '균형교양 clear')
        label132.configure(text='학문기초(대학별교양) 분야에서 %d학점이 부족합니다.' % (12 - int(ent72.get())) if int(ent72.get())<12 else'학문기초(대학별교양) clear')
        label142.configure(text='전공필수 분야에서 %d학점이 부족합니다.' % (12 - int(ent82.get())) if int(ent82.get()) < 12 else '전공필수 clear')
        label152.configure(text='전공선택 분야에서 %d학점이 부족합니다.' % (30 - int(ent92.get())) if int(ent92.get()) < 30 else '전공선택 clear')
        #label162.configure(text='심화전공 분야에서 %d학점이 부족합니다. (전공선택을 더 들으세요.)' % (27 - simjun) if simjun < 27 else '심화전공 clear')
        label172.configure(text='자유선택 분야에서 %d학점이 부족합니다.' % (55 - jasun) if jasun < 55 else '자유선택 clear')
#------------------------------------------------함수 끝---------------------------------------------
button101 = tk.Button(win,text='결과보기',font=('맑은 고딕',11,'bold'),fg='black',width=15,command=cal21)
button101.place(x=150,y=420)

win.mainloop()
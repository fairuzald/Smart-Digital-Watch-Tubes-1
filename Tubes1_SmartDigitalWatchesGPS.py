from tkinter import * 
import tkinter as tk
import time
import winsound

# variable in indonesian language is for global variable 
# that became the essential of this code

ui = Tk()
ui.resizable(0,0)
ui.title("Tugas Besar 1 : Smart Digital Watches")
ui.geometry("900x640")
ui.config(background="light grey")

# BAGIAN UTAMA DISPLAY JAM TANGAN
foto = PhotoImage(file="jam.png")
def photo(frame):
    global foto
    label = Label(frame, image=foto)
    label.place(x=0, y=0, relwidth=1, relheight=1)

# BAGIAN TOMBOL / BUTTON
# Tombol lampu
def light_button(frame):
    light_button = tk.Button(frame,
        text = "Light", 
        command = light, 
        activeforeground = "grey", 
        cursor = "hand2")
    light_button.place(x=250, y=240)

# Tombol ganti jam_tangan
def next_button(frame, words):
    button = tk.Button(frame, cursor="hand2", text=words, command=frame_mode)
    button.place(x=250, y=360)

# Tombol reset 
def reset_button(frame, task):
    reset_button = tk.Button(frame, cursor="hand2", text="reset", command=task)
    reset_button.place(x=616,y=360)

# Tombol start
def start_button(frame, task):
    start_button = tk.Button(frame, cursor="hand2", text="start", command=task)
    start_button.place(x=616, y=240)

# FUNGSI GLOBAL UNTUK SEMUA FRAME

# Fungsi untuk tidak melakukan apa-apa
def skip():
    pass

# frame_mode untuk pindah mode penggunaan jam
count_jam_tangan = 1
def frame_mode():
    global count_jam_tangan
    if count_jam_tangan == 1:
        frame_watches.forget()
        frame_stopwatch.pack(fill="both", expand=1)
        count_jam_tangan += 1
    elif count_jam_tangan == 2:
        frame_stopwatch.forget()
        frame_timer.pack(fill="both", expand=1)
        count_jam_tangan += 1
    elif count_jam_tangan == 3:
        frame_timer.forget()
        frame_alarm.pack(fill="both", expand=1)
        count_jam_tangan += 1
    else : 
        frame_alarm.forget()
        frame_watches.pack(fill="both", expand=1)
        count_jam_tangan -= 3

# lampu akan menyala ketika dipencet
count_color=1
def light():
    global count_color, labels
    #inisiasi label yang akan menyala
    labels=[digital_label, day,
    stopwatch_label, miliseconds_label, sto,
    timer_jam_label, timer_menit_label, timer_detik_label, ctd, bg_timer_label,
    bg_alarm_label, alarm_jam_label, alarm_menit_label, alarm_detik_label,
    alm, status_alm_label1, status_alm_label2, alm]
    # proses nyala 
    current_color = digital_label.cget("background")
    if current_color == "#c0dcd9" and count_color==1:
        next_color="cyan"
        for j in labels:
            j.config(background=next_color)
        ui.after(4000, light)
    elif current_color == "cyan" and count_color == 1:
        next_color = "#c0dcd9"
        for k in labels:
            k.config(background=next_color)
        count_color += 1
        ui.after(10, light)
    else:
        count_color -= 1

# BAGIAN AKSI ATAU FUNGSI PADA TAMPILAN JAM UTAMA

# update tampilan jam utama
def update():
    global hari
    jam = time.strftime("%H")
    menit = time.strftime("%M")
    detik = time.strftime("%S")
    hari = time.strftime("%A")
    label_digital = f'{jam:02}:{menit:02}:{detik:02}'
    digital_label.config(text= jam + ":" + menit + ":" + detik)
    # kasus ketika nilai jam = nilai alarm
    for j in alarm_set_time:
        if j == label_digital:
            winsound.PlaySound("alarm.wav",winsound.SND_ASYNC)
            stop_button1.place(x=250,y=240)
            stop_button2.place(x=250,y=240)
            stop_button3.place(x=250,y=240)
            stop_button4.place(x=250,y=240)
            
    digital_label.after(1000, update)

#untuk menampilkan hari ketika dipencet start atau reset  
count_day=1
def date_time():
    global count_day
    tanggal = time.strftime("%d")
    bulan = time.strftime("%m")
    if count_day == 1:
        day.config(text=f"{tanggal}/{bulan}", font=('digital-7',8), pady=5)
        count_day += 1
        day.after(3000,date_time)
    else:
        day.config(text=hari[:3], font=('digital-7', 11), pady=3)
        count_day=1

# BAGIAN AKSI ATAU FUNGSI PADA MODE STOPWATCH

# variabel bantuan untuk menu stopwatch
run_stopwatch = False
hours_stopwatch = 0
minutes_stopwatch = 0
seconds_stopwatch = 0
milisecs_stopwatch = 0
count_start_stopwatch = 1

# Aksi ketika tombol start untuk stopwatch di pencet
def start_stopwatch():
    global count_start_stopwatch, run_stopwatch
    if count_start_stopwatch == 1:
        if not run_stopwatch:
            count_start_stopwatch+=1
            update_stopwatch()
            start_button_stopwatch.config(text="pause")
            run_stopwatch = True
    else:
        if run_stopwatch:
            count_start_stopwatch=1
            stopwatch_label.after_cancel(update_stopwatch_time)
            start_button_stopwatch.config(text="start")
            run_stopwatch = False

# Aksi ketika tombol reset untuk stopwatch di pencet
def reset_stopwatch():
    global run_stopwatch, count_start_stopwatch
    global hours_stopwatch, minutes_stopwatch, seconds_stopwatch, milisecs_stopwatch
    #gagalkan update digit dan setting ke 0 
    if run_stopwatch:
        count_start_stopwatch=1
        stopwatch_label.after_cancel(update_stopwatch_time)
        run_stopwatch = False
    hours_stopwatch = 0
    minutes_stopwatch = 0
    seconds_stopwatch = 0
    milisecs_stopwatch = 0
    start_button_stopwatch.config(text="start")
    stopwatch_label.config(text='00:00:00')
    miliseconds_label.config(text='00')

# Aksi untuk perhitungan penambahan digit stopwatch
def update_stopwatch():
    global hours_stopwatch, minutes_stopwatch, seconds_stopwatch, milisecs_stopwatch
    milisecs_stopwatch += 1
    if milisecs_stopwatch == 100:
        seconds_stopwatch += 1
        milisecs_stopwatch=0
    if seconds_stopwatch == 60:
        minutes_stopwatch += 1
        seconds_stopwatch = 0
    if minutes_stopwatch == 60:
        hours_stopwatch += 1
        minutes_stopwatch = 0
    stopwatch_label.config(text=f"{hours_stopwatch:02}:{minutes_stopwatch:02}:{seconds_stopwatch:02}")
    miliseconds_label.config(text=f"{milisecs_stopwatch:02}")
    global update_stopwatch_time
    update_stopwatch_time = stopwatch_label.after(10, update_stopwatch)

# BAGIAN AKSI ATAU  MODE TIMER

#Variabel untuk merepresentasikan digit pada jam    
jam_timer = 0
menit_timer = 0
detik_timer = 0
timer_digit = 'J'
status_timer = False
list_mode_timer = ['J','M',"D","Switch"]
count_switch_timer=1

def switch_timer():
    global list_mode_timer, timer_digit, blink_colours
    global count_switch_timer
    count_switch_timer += 1
    if count_switch_timer == 2: #mode menit
        timer_digit =list_mode_timer[1]
    elif count_switch_timer == 3: #mode detik
        timer_digit=list_mode_timer[2]
    elif count_switch_timer == 4: #mode mulai countdown
        timer_digit=list_mode_timer[3]
        timer_jam_label.config(foreground='black')
        timer_menit_label.config(foreground='black')
        timer_detik_label.config(foreground='black')
    elif count_switch_timer == 5: #mode jam
        timer_digit=list_mode_timer[0]
        reset_timer()
        blink_timer(0)
        count_switch_timer=1
    return timer_digit

# fungsi add_timer untuk mengatur penambahan digit tiap komponen waktu
def add_timer():
    global timer_digit, jam_timer,menit_timer,detik_timer
    global count_start_timer, run_timer, status_timer
    if timer_digit == 'J':
        jam_timer += 1
        if jam_timer == 24:
            jam_timer=0 
    if timer_digit=='M':
        menit_timer += 1
        if menit_timer == 60:
            menit_timer=0
    if timer_digit == 'D':
        detik_timer += 1
        if detik_timer == 60:
            detik_timer=0
    if timer_digit == "Switch":
        # jika belum diset maka ketika diset akan mulai hitung mundur
        if status_timer == False:
            status_timer = True
            if not run_timer:
                count_start_timer += 1
                start_timer_button.config(text="pause")
                update_timer()
                run_timer = True
        #jika udah hitung mundur pause
        elif status_timer ==  True:
            status_timer = False
            if run_timer:
                count_start_timer=1
                start_timer_button.config(text="start")
                count_down_label.after_cancel(update_timers)
                run_timer = False
    timer_jam_label.config(text=f'{jam_timer:02}')
    timer_menit_label.config(text=f':{menit_timer:02}')
    timer_detik_label.config(text=f':{detik_timer:02}')
    count_down_label.config(text=f'{jam_timer:02}+{menit_timer:02}+{detik_timer:02}')
    return jam_timer,menit_timer, detik_timer

blink_colours = ['black', 'grey']
def blink_timer(colour_index):
    global timer_digit, blink_colours, list_mode_timer, timer_digit, status_timer
    if timer_digit == "J":
        timer_jam_label.config(foreground = blink_colours[colour_index])
        timer_menit_label.config(foreground = blink_colours[0])
        timer_detik_label.config(foreground = blink_colours[0])
        timer_jam_label.after(200, blink_timer, 1 - colour_index)
    elif timer_digit == "M":
        timer_menit_label.config(foreground = blink_colours[colour_index])
        timer_jam_label.config(foreground = blink_colours[0])
        timer_detik_label.config(foreground = blink_colours[0])
        timer_jam_label.after(200, blink_timer, 1 - colour_index)
    elif timer_digit == "D":
        timer_detik_label.config(foreground = blink_colours[colour_index])
        timer_menit_label.config(foreground = blink_colours[0])
        timer_jam_label.config(foreground = blink_colours[0])
        timer_jam_label.after(200, blink_timer, 1 - colour_index)

count_start_timer=1
run_timer = False
# fungsi untuk melakukan reset timer
def reset_timer():
    global run_timer, count_start_timer, jam_timer, menit_timer, detik_timer
    # hitung mundur dibatalkan dan setting ke nilai 0
    if run_timer:
        count_start_timer=1
        count_down_label.after_cancel(update_timers)
        run_timer = False
    jam_timer = 0
    menit_timer = 0
    detik_timer = 0
    start_timer_button.config(text="start")
    timer_jam_label.config(text=f'{jam_timer:02}')
    timer_menit_label.config(text=f':{menit_timer:02}')
    timer_detik_label.config(text=f':{detik_timer:02}')

# update_timer untuk prosessing ketike timer dimulai
def update_timer():
    global jam_timer, menit_timer, detik_timer,update_timers
    times_timer = int(jam_timer)*3600+int(menit_timer)*60+int(detik_timer)
    if times_timer > 0:
        times_timer -= 1
    jam_timer=times_timer//3600
    menit_timer=(times_timer%3600)//60
    detik_timer=(times_timer%3600)%60
    timer_jam_label.config(text=f'{jam_timer:02}')
    timer_menit_label.config(text=f':{menit_timer:02}')
    timer_detik_label.config(text=f':{detik_timer:02}')
    count_down_label.config(text=f'{jam_timer:02}+{menit_timer:02}+{detik_timer:02}')
    if times_timer == 0:    
        winsound.PlaySound("timer.wav",winsound.SND_ASYNC)
        start_timer_button.config(text="start")
        timer_jam_label.config(text=f'{jam_timer:02}')
        timer_menit_label.config(text=f':{menit_timer:02}')
        timer_detik_label.config(text=f':{detik_timer:02}')
        update_timers = count_down_label.after(1000, skip)
    # selama nilai hitung mundur belum 0 selalu cek
    if times_timer > 0:
        update_timers = count_down_label.after(1000, update_timer)
        
# BAGIAN AKSI ATAU FUNGSI UNTUK MODE ALARM

# variabel bantuan untuk mode alarm
run_alarm = False
jam_alarm = 0
menit_alarm = 0
detik_alarm = 0
mode_digit = 'J1'
count_switch = 1
list_mode=['J1','M1','D1',"Switch1", "J2", 'M2','D2','Switch2']

# fungsi untuk beralih ke komponen waktu yang lain
def switch_alarm():
    global list_mode, count_switch, mode_digit
    count_switch += 1
    if count_switch == 2: #menit alarm 1
        mode_digit=list_mode[1]
    elif count_switch == 3: #detik alarm 1
        mode_digit=list_mode[2]
    elif count_switch == 4: #set alarm 1
        mode_digit=list_mode[3]
        status_alm_label1.place(x=430,y=312)
        alarm_jam_label.place_forget()
        alarm_menit_label.place_forget()
        alarm_detik_label.place_forget()
    elif count_switch == 5: #jam alarm 2
        mode_digit=list_mode[4]
        status_alm_label1.place_forget()
        alarm_jam_label.place(x=402,y=312)
        alarm_menit_label.place(x=430,y=312)
        alarm_detik_label.place(x=462,y=312)
        blink(0)
        alm.config(text="ALM2", font=('digital-7', 10))
    elif count_switch == 6: #menit alarm 2
        mode_digit=list_mode[5]
    elif count_switch == 7: #detik alarm 2
        mode_digit=list_mode[6]
    elif count_switch == 8:  #set alarm 2
        mode_digit = list_mode[7]
        status_alm_label2.place(x=430,y=312)
        alarm_jam_label.place_forget()
        alarm_menit_label.place_forget()
        alarm_detik_label.place_forget()
    elif count_switch == 9: #jam alarm 1
        mode_digit = list_mode[0]
        blink(0)
        count_switch = 1
        status_alm_label2.place_forget()
        alarm_jam_label.place(x=402,y=312)
        alarm_menit_label.place(x=430,y=312)
        alarm_detik_label.place(x=462,y=312)
        alm.config(text="ALM1", font=('digital-7', 11))

status_alarm1 = False
status_alarm2 = False
alarm_set_time = ["" for i in range(2)]
# fungsi untuk tindakan menambah komponen waktu
def add_alarm():
    global mode_digit, alarm_label, set_new, status_alarm1, status_alarm2
    global jam_alarm,menit_alarm,detik_alarm, alarm_set_time
    set_new=f'{jam_alarm:02}:{menit_alarm:02}:{detik_alarm:02}'
    mode=mode_digit
    if mode == 'J1' or mode == 'J2':
        jam_alarm += 1
        if jam_alarm == 24:
            jam_alarm=0
    if mode == 'M1' or mode == 'M2':
        menit_alarm += 1
        if menit_alarm == 60:
            menit_alarm=0
    if mode == 'D1' or mode == 'D2':
        detik_alarm += 1
        if detik_alarm == 60:
            detik_alarm=0
    if mode == "Switch1":
        if status_alarm1 == False:
            status_alm_label1.config(text="On")
            alarm_set_time[0]=set_new
            status_alarm1 = True
        elif status_alarm1 ==  True:
            status_alm_label1.config(text="Off")
            alarm_set_time[0] = ""
            status_alarm1 = False
        print(alarm_set_time)
        update()
    if mode == "Switch2":
        if status_alarm2 == False:
            status_alm_label2.config(text="On")
            alarm_set_time[1]=set_new
            status_alarm2 = True
        elif status_alarm2 ==  True:
            status_alm_label2.config(text="Off")
            alarm_set_time[1]=""
            status_alarm2 = False
        print(alarm_set_time)
        update()
    alarm_jam_label.config(text=f'{jam_alarm:02}')
    alarm_menit_label.config(text=f':{menit_alarm:02}')
    alarm_detik_label.config(text=f':{detik_alarm:02}')
    alarm_label.config(text=f'{jam_alarm:02}:{menit_alarm:02}:{detik_alarm:02}')
    return alarm_detik_label,alarm_jam_label,alarm_menit_label

# fungsi untuk bunyi alarm yang nyala  
def stop_alarm():
    winsound.PlaySound(None, winsound.SND_PURGE)
    stop_button1.place_forget()
    stop_button2.place_forget()
    stop_button3.place_forget()
    stop_button4.place_forget()

flash_colours = ['black', 'grey']
# fungsi untuk blink berkedip saat pindah mode komponen waktu
def blink(colour_index):
    global mode_list,mode,mode_digit
    mode=mode_digit
    if mode == "J1" or mode == "J2":
        alarm_jam_label.config(foreground = flash_colours[colour_index])
        alarm_menit_label.config(foreground = flash_colours[0])
        alarm_detik_label.config(foreground = flash_colours[0])
        alarm_jam_label.after(200, blink, 1 - colour_index)
    elif mode == "M1" or mode == "M2":
        alarm_menit_label.config(foreground = flash_colours[colour_index])
        alarm_jam_label.config(foreground = flash_colours[0])
        alarm_detik_label.config(foreground = flash_colours[0])
        alarm_jam_label.after(200, blink, 1 - colour_index)
    elif mode == "D1" or mode == "D2":
        alarm_detik_label.config(foreground = flash_colours[colour_index])
        alarm_menit_label.config(foreground = flash_colours[0])
        alarm_jam_label.config(foreground = flash_colours[0])
        alarm_jam_label.after(200, blink, 1 - colour_index)   
  
# Frame untuk melakukan pindah jam_tangan 
frame_watches = tk.Frame(ui)
frame_stopwatch = tk.Frame(ui)
frame_timer = tk.Frame(ui)
frame_alarm = tk.Frame(ui)

frame=[frame_timer,frame_stopwatch,frame_watches, frame_alarm]

list_jam_tangan=[
    [frame_watches,date_time,date_time,"Mode"], 
    [frame_stopwatch,skip,reset_stopwatch,"Timer"],
    [frame_timer,skip,switch_timer,"Alarm"],
    [frame_alarm,add_alarm,switch_alarm,"Back"]
    ]

# Memanggil fungsi dan button yang bersifat global 
for i in (list_jam_tangan):
    photo(i[0])
    light_button(i[0])
    start_button(i[0],i[1])
    reset_button(i[0],i[2])
    next_button(i[0],i[3])

# Menu dan frame utama
digital_label = Label(frame_watches,width=11,pady=9, text="", bg="#c0dcd9", fg="black", justify="center", font=('digital-7', 20))
digital_label.place(x=375,y=304) 
day = Label(frame_watches, pady=3,text=time.strftime("%A")[:3], height=1, bg="#c0dcd9", fg="black", font=('digital-7', 11))
day.place(x=489, y=258)

# Menu dan tombol stopwatch
stopwatch_label = Label(frame_stopwatch, text="00:00:00",width=11,pady=9, bg="#c0dcd9", fg="black", font=("digital-7",20))
stopwatch_label.place(x=375,y=304)
miliseconds_label = Label(frame_stopwatch, text="00", bg="#c0dcd9", fg="black", font=("digital-7",14))
miliseconds_label.place(x=492,y=307)
sto = Label(frame_stopwatch,pady=3, text="STO", bg="#c0dcd9", fg="black", font=('digital-7', 11))
sto.place(x=489, y=258)
# imgg = PhotoImage(file="start.png")
# image1 = imgg.subsample(5,7)
start_button_stopwatch = tk.Button(frame_stopwatch, text="start", cursor="hand2",command=start_stopwatch)
start_button_stopwatch.place(x=616,y=240)

# Menu dan tombol timer
count_down_label = Label(frame_timer, text="00:00:00", width=10, bg="#c0dcd9", fg="black", font=("digital-7",20))
ctd = Label(frame_timer, text="CTD", pady=3,bg="#c0dcd9", fg="black", font=('digital-7', 11))
ctd.place(x=489, y=258)
bg_timer_label = Label(frame_timer,width=20, padx=2,pady=15, bg="#c0dcd9")
bg_timer_label.place(x=375,y=304)
timer_jam_label = Label(frame_timer, text = '00', bg="#c0dcd9", fg="black", font=("digital-7",20),foreground = blink_colours[0])
timer_jam_label.place(x=402,y=312)
timer_menit_label = Label(frame_timer, text = ':00',bg="#c0dcd9", fg="black", font=("digital-7",20),foreground = blink_colours[0])
timer_menit_label.place(x=430,y=312)
timer_detik_label = Label(frame_timer, text = ':00', bg="#c0dcd9", fg="black", font=("digital-7",20),foreground = blink_colours[0])
timer_detik_label.place(x=462,y=312)
blink_timer(0)
start_timer_button = tk.Button(frame_timer, text="start", cursor="hand2",command=add_timer)
start_timer_button.place(x=616,y=240)


# Menu dan tombol alarm
alarm_label = Label(frame_alarm, text="00:00:00", width=10, bg="#c0dcd9", fg="black", font=("digital-7",20))
alm = Label(frame_alarm,pady=2, text="ALM1", bg="#c0dcd9", fg="black", font=('digital-7', 11))
alm.place(x=488, y=260)
bg_alarm_label = Label(frame_alarm,width=20, padx=2,pady=15, bg="#c0dcd9")
bg_alarm_label.place(x=375,y=304)
alarm_jam_label = Label(frame_alarm, text = '00', bg="#c0dcd9", fg="black", font=("digital-7",20),foreground = flash_colours[0])
alarm_jam_label.place(x=402,y=312)
alarm_menit_label = Label(frame_alarm, text = ':00',bg="#c0dcd9", fg="black", font=("digital-7",20),foreground = flash_colours[0])
alarm_menit_label.place(x=430,y=312)
alarm_detik_label = Label(frame_alarm, text = ':00', bg="#c0dcd9", fg="black", font=("digital-7",20),foreground = flash_colours[0])
alarm_detik_label.place(x=462,y=312)
status_alm_label1 = Label(frame_alarm, text = 'Off', bg="#c0dcd9", fg="black", font=("digital-7",20),foreground = flash_colours[0])
status_alm_label2 = Label(frame_alarm, text = 'Off', bg="#c0dcd9", fg="black", font=("digital-7",20),foreground = flash_colours[0])
blink(0)
stop_button1 = tk.Button(frame_watches, text="silent", cursor="hand2",command=stop_alarm)
stop_button2 = tk.Button(frame_stopwatch, text="silent", cursor="hand2",command=stop_alarm)
stop_button3 = tk.Button(frame_timer, text="silent", cursor="hand2",command=stop_alarm)
stop_button4 = tk.Button(frame_alarm, text="silent", cursor="hand2",command=stop_alarm)


# Main program
frame_watches.pack(fill="both", expand="True")

update()

ui.mainloop()
from tkinter import *
from tkinter import ttk
from time import sleep

execution_count = 0

def action(win, more) :
    global execution_count
    global root
    print('Jawab', more)
    if more:
        win.destroy()
        sleep(waktu_tunda * 60) #mengubah detik menjadi menit (1 menit = 60 detik)
        execution_count = execution_count + 1
        TampilanNote(title, message)
    else:
        win.destroy()
        root.destroy()
        
def TampilanNote(title, message):
    global root
    print('Menjalankan perintah Tuan', execution_count)
    win = Toplevel()
    win.withdraw()
    win.update_idletasks()
    x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
    y = (win.winfo_screenheight()- win.winfo_reqheight()) / 2
    win.geometry("+%d+%d" % (x, y))
    win.deiconify()
    win.title(title)
    message1=message
    message2='Waktu tunda saat ini={0} menit'.format(waktu_tunda) #*60 mengubah detik menjadi menit
    message3='Apakah tuan ingin lebih banyak pengingat?'
    ttk.Label(win, text=message1).grid(column=0, row=0)
    ttk.Label(win, text=message2).grid(column=0, row=1)
    ttk.Label(win, text=message3).grid(column=0, row=2)
    yes_btn = ttk.Button(win, text='Yes', command=lambda: action(win, True))
    yes_btn.grid(column=0,row=3)
    ttk.Button(win, text='No', command=lambda: action(win, False)).grid(column=1, row=3)
    yes_btn.focus()
    win.lift()
    win.attributes('-topmost', True)
    
print('\n\n\n')
print('Selamat datang Tuan Fedy!')
print('-------------------------------------------------')
print('Setelah dimulai, aplikasi akan berjalan tanpa henti sampai anda memintanya berhenti, Tuan.')
print('Hamba akan menampilkan jendela pesan setiap interval waktu tunda untuk mengingatkan tuan untuk melakukan tugas secara berkala')
print('-------------')
waktu_tunda = int(input('Masukkan Waktu Tunda:'))
title = input('Masukkan Judul Pengingat: ')
message = input('Masukkan Pesan Untuk Pengingat: ')
# waktu_tunda = 3
print('\n\nTerima kasih Tuan Fedy! Tuan akan mendapatkan pengingat pertama dalam {0} detik'.format(waktu_tunda))
print('\n\n')
print('Aplikasi dimulai....')

root = Tk()
root.withdraw()
execution_count = 1
TampilanNote(title, message)   # contoh Judul='Belajar coding, Pesan='Waktunua untuk belajar coding, Tuan!'
root.mainloop()
print('Keluar, sampai jumpa Tuan!')
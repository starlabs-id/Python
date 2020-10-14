import sys
import socket
import random
from thread import start_new_thread


HOST=''
PORT=1332

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print 'Socket created'

try:
    s.bind((HOST,PORT))
except socket.error as msg:
    print 'Bind gagal. Error Code : ' +str(msg[0]) + '. Pesan : ' + msg[1]
    sys.exit()

print 'Socket bind ke port ' + str(PORT)

s.listen(100000)
print 'Socket sedang listening'

#list soal
def Tampil(soal):
    if soal == 0:
        reply = 'Katak bernafas dengan ?'
    elif soal == 1:
        reply = 'Bendera Indonesia warnanya ?'
    elif soal == 2:
        reply = 'Kenapa mobil berhenti di tengah jalan?'
    elif soal == 3:
        reply = 'Ada raja, ratu dan pangeran. Raja meninggal, pangeran jadi ?'
    elif soal == 4:
        reply = 'Anaknya nyamuk disebut ?'
    elif soal == 5:
        reply = 'Endek merupakan produk asli dari ?'
    elif soal == 6:
        reply = 'Candi Borobudur peninggalan dari jaman ?'
    elif soal == 7:
        reply = 'Tak kenal maka tak ?'
    elif soal == 8:
        reply = 'Sebutan untuk eseorang yang mengambil kemudian pergi ?'
    elif soal == 9:
        reply = 'Bandung lautan ?'
    else:
        reply = 'Soal tidak ditemukan, Range Error'

    conn.sendall('\n' + reply)

#mengecek jawaban dari client dengan list jawaban
def check(poin, jawab,soal):
    jawaban = ["semaunya","ada dua","di rem","yatim","keluarga","manusia","dahulu","taulah","mantan","kota"]
    if jawaban[soal] == jawab:
        poin += 20
        return poin
    else:
        return poin

def clientTread(conn):
    conn.send('Selamat datang di Game Tebak-tebakan :D\n')

    #perulangan untuk menu permainan
    while True :
        #menu
        reply = "===================================\n"
        reply1= "| S = START | Q = QUIT | H = HELP |\n"
        reply2= "===================================\n"
        conn.sendall(reply+reply1+reply2)
        data = conn.recv(1024).upper()
        #kondisi jika pilihan start
        if data == "S":
            #deklarasi variable
            i = 0
            poin = 0
            listSoal = []
            jawab = ['']
            #perulangan permainan untuk 5 soal
            while i != 5:
                soal = random.randint(0,9)
                if soal not in listSoal:
                    Tampil(soal)
                    jawab = conn.recv(1024).lower()
                    poin = check(poin, jawab, soal)
                    listSoal.append(soal)
                    i+=1
                if not data:
                    break
   
            reply = "Game Berakhir\nNilai anda : %d poin" % (poin)
            conn.sendall(reply+'\n')
            print 'Client dengan IP '+ addr[0] + ' berhasil mendapat point sebanyak %d'% poin
        #kondisi jika ingin keluar
        elif data == "Q":
            reply = "Sampai ketemu lagi (:"
            conn.sendall(reply+'\n')
            print 'IP ' + addr[0] + ' keluar'
            break
        #kondisi jika memilih bantuan
        elif data == "H":
            reply =  "[1] Ketik S untuk memulai permainan\n[2] Ketik Q untuk keluar dari server\n[3] Permainan akan selesai jika telah menjawab 5 soal"
            conn.sendall(reply+'\n')

        #kondisi jika pilihan tidak ada di menu
        else:
            reply = 'Bad command. Silahkan ketik sesuai menu pilihan\n'
            conn.sendall(reply+'\n')
        
        if not data:
            break
        

    conn.close()

while 1:
    try:
        conn, addr = s.accept()
        print '\nTerhubung dengan ' + addr[0] + ' dari port ' + str(addr[1])
        start_new_thread(clientTread, (conn,))
    except KeyboardInterrupt:
        print 'Server dimatikan'
        sys.exit() 
    
s.close()
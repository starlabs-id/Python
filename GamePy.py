import sys
import socket
import random
from thread import start_new_thread


HOST=''
PORT=1331

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
        reply = 'Apakah singkatan dari LAN ?'
    elif soal == 1:
        reply = 'Apa ibukota negara Filiphina ?'
    elif soal == 2:
        reply = 'Apa mata uang negara Thailand ?'
    elif soal == 3:
        reply = 'Dimana titik nol kilometer kota Denpasar ?'
    elif soal == 4:
        reply = 'Binatang yang bisa hidup di darat dan di air disebut ?'
    elif soal == 5:
        reply = 'Negara terluas keempat di dunia adalah ?'
    elif soal == 6:
        reply = 'Udara yang bergerak disebut ?'
    elif soal == 7:
        reply = 'Gunung tertinggi di Bali ?'
    elif soal == 8:
        reply = 'Pulau dengan penduduk terpadat di Indonesia ?'
    elif soal == 9:
        reply = 'Hardware untuk menyimpan data pada komputer atau laptop adalah ?'
    else:
        reply = 'Soal tidak ditemukan, Range Error'

    conn.sendall('\n' + reply)

#mengecek jawaban dari client dengan list jawaban
def check(poin, jawab,soal):
    jawaban = ["local area network","manila","bath","catur muka","amfibi","amerika serikat","angin","gunung agung","jawa","hard disk"]
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
            reply = "Main lagi di lain waktu :) byee~~"
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
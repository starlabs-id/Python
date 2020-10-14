#!/usr/bin/env python
import socket
import errno
import sys

# deklarasi variabel
HOST="127.0.0.1"
PORT=1332

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST,PORT))
    print (s.recv(1024))

    while True:
        print (s.recv(1024))
        PESAN = raw_input('Pilih Menu: ')
        s.send(PESAN)
        data = PESAN.upper()
        if data == "S":
            jum = 0
            while jum !=5:
                print (s.recv(1024))
                PESAN = raw_input('Masukan jawaban: ')
                s.send(PESAN)
                jum +=1
            print (s.recv(1024))
        elif data == "H":
            print (s.recv(1024))
        elif data == "Q":
            print (s.recv(1024))
            sys.exit()
        if not data:
            break
        
except socket.error as e:
    if e.errno == errno.ECONNREFUSED:
        print 'gagal melakukan koneksi ke server'
    elif e.errno ==  errno.ECONNRESET:
        print 'koneksi ke server terputus'
    elif e.errno == errno.ETIMEDOUT:
        print 'koneksi timeout!'
    else:
        print e
except Exception as e:
    print e
finally:
    s.close()        
import ftplib, getpass

try:
	print "\nWelcome to FTP Client Application"
	ftp = ftplib.FTP()
	IP = raw_input("IP : ")
	PORT = raw_input("PORT : ")
	ftp.connect(IP,PORT) #check ip & port
	print(ftp.getwelcome())
	while True:
		USER = raw_input("USER : ")
		PASS = getpass.getpass()
		#check user & password
		try:
			login = ftp.login(USER,PASS)
			if login[:3] == "230":
				print "Login Success\n"
				break
		except Exception as err:
				print(err)

	while True:
		print "========================================================="
		print "| L = List \t\t| U = Upload \t| R = Remove \t|"
		print "| C = Change directory \t| D = Download \t| Q = Quit \t|"
		print "========================================================="
		chose = (raw_input("Input Your Choice: ")).upper()
		#list file & dir
		if chose == "L":
			print(ftp.retrlines("LIST"))
		#change dir
		elif chose == "C":
			try:
				folder = raw_input("Name Folder: ")
				print(ftp.cwd(folder))
			except Exception as err:
				print(err)
		#upload file
		elif chose == "U":
			try:
				asal = raw_input("Upload File: ")
				file = raw_input("Save File As: ")
				print ftp.storbinary("STOR " + file, open(asal,"rb"))
			except Exception as err:
				print(err)
		#download file
		elif chose == "D":
			try:
				download = raw_input("Download File: ")
				save = raw_input("Save File As: ")
				File1 = open(save, "wb")
				print ftp.retrbinary("RETR " + download, File1.write)
			except Exception as err:
				print(err)
		#remove file
		elif chose == "R":
			try:
				remove = raw_input("Select File: ")
				print ftp.delete(remove)
			except Exception as err:
				print(err)
		#quit
		elif chose == "Q":
			print "Application Closed!"
			break

		else:
			print "Bad Commant!"
	ftp.close()
except Exception as err:
	print("Error: %s" % err)
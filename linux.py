import os

vg_name = "vg"
lv_name = "lv"
remote_ip = "192.169.43.223"

# List disk available on remote system
def remote_disk_list():
	global remote_ip
	os.system("clear")
	print()
	os.system("tput setaf 1")
	print("\t\t    ----------------------------------------")
	print("\t\t    | Check if Disk is Available or Not !! |")
	print("\t\t    ----------------------------------------")
	os.system("tput setaf 7")
	print()

	os.system("ssh {} fdisk -l".format(remote_ip))
	os.system("tput setaf 4")
	print("Press Y to continue if disk is available.")
	print("Press N to exit the program if disk is not available.")
	os.system("tput setaf 3")
	ch = input("Enter your choice(Y/N): " )
	if ch == "N":
		os.system("clear")
		print()
		os.system("tput setaf 1")
		print("\t    --------------------------------------")
		print("\t    |\t\t\tAdd the Disk First\t\t        |")
		print("\t    | Thank You for Partation Manager !! |")
		print("\t    --------------------------------------")
		os.system("tput setaf 7")
		exit()

# Create partation on remote system
def remote_create_part():
	global remote_ip
	global vg_name
	global lv_name

	os.system("clear")
	print()
	os.system("tput setaf 1")
	print("\t\t     --------------------------------------")
	print("\t\t     | Create and Mount Partation !! |")
	print("\t\t     --------------------------------------")
	os.system("tput setaf 7")
	print()

	os.system("tput setaf 3")
	disk = input("Enter the Disk Name : ")
	os.system("tput setaf 7")
	os.system("ssh {0} fdisk {1}".format(remote_ip, disk))
	os.system("tput setaf 3")
	os.system("tput setaf 3")	
	fs = input("Enter the File System : ")
	part_name = input("Enter the Partation Name : ")
	os.system("tput setaf 7")	
	os.system("ssh {0} mkfs.{1} {2}".format(remote_ip, fs, part_name))
	os.system("tput setaf 3")
	mount_point = input("Enter the Mountpoint : ")
	os.system("tput setaf 7")
	os.system("ssh {0} mount {1} {2}".format(remote_ip, part_name, mount_point))
	os.system("ssh {0} df -h".format(remote_ip))

	os.system("tput setaf 3")
	input("Press Enter to Continue")
	os.system("tput setaf 7")

# Create LVM on remote system
def remote_create_lv():
	global remote_ip
	global vg_name
	global lv_name

	os.system("clear")
	print()
	os.system("tput setaf 1")
	print("\t\t     --------------------------------------")
	print("\t\t     | Create and Mount Logical Volume !! |")
	print("\t\t     --------------------------------------")
	os.system("tput setaf 7")
	print()

	os.system("tput setaf 3")
	disk = input("Enter the disk Name : ")
	os.system("tput setaf 7")
	os.system("ssh {0} pvcreate {1}".format(remote_ip, disk))
	os.system("ssh {0} pvdisplay {1}".format(remote_ip, disk))
	os.system("tput setaf 3")
	vg_name = input("Enter the Virtual Group Name : ")
	os.system("tput setaf 7")
	os.system("ssh {0} vgcreate {1} {2}".format(remote_ip, vg_name, disk))
	os.system("ssh {0} vgdisplay {1}".format(remote_ip, vg_name))
	os.system("tput setaf 3")
	lv_name = input("Enter the Locial Volume Name : ")
	lv_size = input("Enter the size of partation : ")
	os.system("tput setaf 7")
	os.system("ssh {0} lvcreate --size {1} --name {2} {3}".format(remote_ip, lv_size, lv_name,  vg_name))
	os.system("ssh {0} lvdisplay {1}/{2}".format(remote_ip, vg_name,  lv_name))
	os.system("tput setaf 3")	
	fs = input("Enter the File System : ")
	os.system("tput setaf 7")	
	os.system("ssh {0} mkfs.{1} /dev/{2}/{3}".format(remote_ip, fs, vg_name, lv_name))
	os.system("tput setaf 3")
	mount_point = input("Enter the Mountpoint : ")
	os.system("tput setaf 7")
	os.system("ssh {0} mount /dev/{1}/{2} {3}".format(remote_ip, vg_name, lv_name, mount_point))
	os.system("ssh {} df -h".format(remote_ip))

	os.system("tput setaf 3")
	input("Press Enter to Continue")
	os.system("tput setaf 7")

# Resize the LV on remote system
def remote_resize_lv():
	global remote_ip
	os.system("clear")
	print()
	os.system("tput setaf 1")
	print("\t\t    ----------------------------------------")
	print("\t\t    | Resize the Size of Logical Volume !! |")
	print("\t\t    ----------------------------------------")
	os.system("tput setaf 7")
	print()

	os.system("tput setaf 3")
	size = input("Enter the Size : ")
	os.system("tput setaf 7")
	os.system("ssh {0} lvextend --size +{1} /dev/{2}/{3}".format(remote_ip, size, vg_name, lv_name))
	os.system("ssh {0} resize2fs /dev/{1}/{2}".format(remote_ip, vg_name, lv_name))
	os.system("ssh {0} df -h".format(remote_ip))

	os.system("tput setaf 3")
	input("Press Enter to Continue")
	os.system("tput setaf 7")


# List disk available on Local system
def disk_list():
	os.system("clear")
	print()
	os.system("tput setaf 1")
	print("\t\t    ----------------------------------------")
	print("\t\t    | Check if Disk is Available or Not !! |")
	print("\t\t    ----------------------------------------")
	os.system("tput setaf 7")
	print()

	os.system("fdisk -l")
	os.system("tput setaf 4")
	print("Press Y to continue if disk is available.")
	print("Press N to exit the program if disk is not available.")
	os.system("tput setaf 3")
	ch = input("Enter your choice(Y/N): " )
	if ch == "N":
		os.system("clear")
		print()
		os.system("tput setaf 1")
		print("\t    --------------------------------------")
		print("\t    |\t\t\tAdd the Disk First\t\t        |")
		print("\t    | Thank You for Partation Manager !! |")
		print("\t    --------------------------------------")
		os.system("tput setaf 7")
		exit()

# Create partation in local system
def create_part():
	global vg_name
	global lv_name

	os.system("clear")
	print()
	os.system("tput setaf 1")
	print("\t\t     --------------------------------------")
	print("\t\t     | Create and Mount Partation !! |")
	print("\t\t     --------------------------------------")
	os.system("tput setaf 7")
	print()

	os.system("tput setaf 3")
	disk = input("Enter the Disk Name : ")
	os.system("tput setaf 7")
	os.system("fdisk {}".format(disk))
	os.system("tput setaf 3")
	os.system("tput setaf 3")	
	fs = input("Enter the File System : ")
	part_name = input("Enter the Partation Name : ")
	os.system("tput setaf 7")	
	os.system("mkfs.{0} {1}".format(fs, part_name))
	os.system("tput setaf 3")
	mount_point = input("Enter the Mountpoint : ")
	os.system("tput setaf 7")
	os.system("mount {0} {1}".format(part_name, mount_point))
	os.system("df -h")

	os.system("tput setaf 3")
	input("Press Enter to Continue")
	os.system("tput setaf 7")

# Create LVM on remote system
def create_lv():
	global vg_name
	global lv_name

	os.system("clear")
	print()
	os.system("tput setaf 1")
	print("\t\t     --------------------------------------")
	print("\t\t     | Create and Mount Logical Volume !! |")
	print("\t\t     --------------------------------------")
	os.system("tput setaf 7")
	print()

	os.system("tput setaf 3")
	disk = input("Enter the disk Name : ")
	os.system("tput setaf 7")
	os.system("pvcreate {}".format(disk))
	os.system("pvdisplay {}".format(disk))
	os.system("tput setaf 3")
	vg_name = input("Enter the Virtual Group Name : ")
	os.system("tput setaf 7")
	os.system("vgcreate {0} {1}".format(vg_name, disk))
	os.system("vgdisplay {0}".format(vg_name))
	os.system("tput setaf 3")
	lv_name = input("Enter the Locial Volume Name : ")
	lv_size = input("Enter the size of partation : ")
	os.system("tput setaf 7")
	os.system("lvcreate --size {0} --name {1} {2}".format(lv_size, lv_name,  vg_name))
	os.system("lvdisplay {0}/{1}".format( vg_name,  lv_name))
	os.system("tput setaf 3")	
	fs = input("Enter the File System : ")
	os.system("tput setaf 7")	
	os.system("mkfs.{0} /dev/{1}/{2}".format(fs, vg_name, lv_name))
	os.system("tput setaf 3")
	mount_point = input("Enter the Mountpoint : ")
	os.system("tput setaf 7")
	os.system("mount /dev/{0}/{1} {2}".format(vg_name, lv_name, mount_point))
	os.system("df -h")

	os.system("tput setaf 3")
	input("Press Enter to Continue")
	os.system("tput setaf 7")

# Resize the size of LV
def resize_lv():
	os.system("clear")
	print()
	os.system("tput setaf 1")
	print("\t\t    ----------------------------------------")
	print("\t\t    | Resize the Size of Logical Volume !! |")
	print("\t\t    ----------------------------------------")
	os.system("tput setaf 7")
	print()

	os.system("tput setaf 3")
	size = input("Enter the Size : ")
	os.system("tput setaf 7")
	os.system("lvextend --size +{0} /dev/{1}/{2}".format(size, vg_name, lv_name))
	os.system("resize2fs /dev/{0}/{1}".format(vg_name, lv_name))
	os.system("df -h")

	os.system("tput setaf 3")
	input("Press Enter to Continue")
	os.system("tput setaf 7")



# Linux Remote Login
def remote_login():
	global remote_ip
	while True:
		os.system("clear")
		os.system("tput setaf 1")
		print("\t\t    ------------------------------")
		print("\t\t    | Welcome to Remote Login !! |")
		print("\t\t    ------------------------------")
		os.system("tput setaf 7")

		os.system("tput setaf 2")
		print("""
		  Press 1 : To Create the Key
		  Press 2 : To Continue if you have key already
		  Press 3 : To Return Previous Menu
		""")
		
		print()
		os.system("tput setaf 3")
		ch = input("\t\t  Enter your Choice : ")
		os.system("tput setaf 7")

		if int(ch) == 1:
			remote_ip = input("Enter the Remote IP : ")
			os.system("ssh-keygen")
			os.system("ssh-copy-id root@{0}".format(remote_ip))
			input("Key Successfully Copied Press ENter to Continue")
			remote()

		elif int(ch) == 2:
			remote()

		elif int(ch) == 3:
			break

		else:
			print("Please Select Right Choice")
			input()


# Linux Local Login
def locally():
	while True:
		os.system("clear")
		os.system("tput setaf 1")
		print("\t\t          ------------------------------")
		print("\t\t          | Welcome Linux Assistant !! |")
		print("\t\t          ------------------------------")
		os.system("tput setaf 7")

		os.system("tput setaf 2")
		print("""
		\tPress 1 : To Check IP Address
		\tPress 2 : To Run Command
		\tPress 3 : To configure Webserver
		\tPress 4 : To Create Partation
		\tPress 5 : To Create LVM
		\tPress 6 : To Resize LV
		\tPress 7 : To Exit
		""")
		
		print()
		os.system("tput setaf 3")
		ch = input("\t\t\tEnter your Choice : ")
		os.system("tput setaf 7")

		if int(ch) == 1:
			os.system("ifconfig enp0s3")
			input()

		elif int(ch) == 2:
			cmd = input("Enter the Command : ")
			os.system(cmd)
			input()

		
		elif int(ch) == 3:
			os.system('yum install httpd -y')
			os.system('cp index.html /var/www/html/index.html')
			os.system('systemctl start httpd')
			os.system('systemctl status httpd')
			input()	

		elif int(ch) == 4:
			disk_list()
			create_part()

		elif int(ch) == 5:
			disk_list()
			create_lv()

		elif int(ch) == 6:
			resize_lv()

		elif int(ch) == 7:
			break
		else:
			print("Please Select Righ Choice")
			input()				


# Linux Menu
def linux_menu():
	print()
	os.system("tput setaf 3")
	login = input("Do you want to perform task locally/remotely(L/R) : ")
	print(login)
	print()
	os.system("tput setaf 7")
	if login == "R" or login == "r":
		remote_login()
			
	elif login == "L" or login == "l":
		locally()

	else:
		print("Select Right Choice")
		input()



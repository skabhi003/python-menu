import os

NN_ip = "0.0.0.0"
DD_ip = "10.0.0.1"
client_ip = "10.10.10.10"

# Configure the Namenode
def namenode_config():
	global NN_ip
	print()
	os.system("tput setaf 3")
	NN_ip = input("Enter the Name Node IP : ")
	os.system("tput setaf 7")
	os.system("ssh-keygen")
	os.system("ssh-copy-id root@{0}".format(NN_ip))
	os.system("tput setaf 3")
	input("Key Successfully Copied Press Enter to Continue")
	os.system("tput setaf 7")
	
	# Remove all the files and software if exist	
	os.system("ssh root@{0} yum remove hadoop -y".format(NN_ip))
	os.system("ssh root@{0} yum remove jdk -y".format(NN_ip))
	os.system("ssh root@{0} rm -rf /etc/hadoop".format(NN_ip))
    	
	#Copy and Insatall Software
	os.system("tput setaf 3")
	print("\t  Copying Required Softwares Namenode ")
	print("\t -------------------------------------\n")
	os.system("tput setaf 7")	
	os.system("scp /root/jdk-8u171-linux-x64.rpm {0}:/root".format(NN_ip))
	os.system("scp /root/hadoop-1.2.1-1.x86_64.rpm {0}:/root".format(NN_ip))
	os.system("scp /root/epel-release-latest-8.noarch.rpm {0}:/root".format(NN_ip))
	os.system("tput setaf 3")	
	print("\t  Installing Required Softwares Namenode ")
	print("\t -------------------------------------\n")
	os.system("tput setaf 7")
	os.system("ssh root@{0} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force".format(NN_ip))
	os.system("ssh root@{0} rpm -ivh /root/jdk-8u171-linux-x64.rpm".format(NN_ip))

	#Folder Associate with Nameode
	os.system("tput setaf 3")
	nnfold = input("Enter the Folder Name to associate with Name Node : ")
	os.system("tput setaf 7")
	os.system("ssh {} mkdir /{}".format(NN_ip, nnfold))
	
    	
	#Create Namenode hdfs and core file
	os.system("touch nn-file_core.xml")
	my_file = open("nn-file_core.xml","r+")
	my_file.truncate(0)
	my_file.write("<?xml version='1.0'?>\n")
	my_file.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n")
	my_file.write("<configuration>\n")
	my_file.write("<property>\n")
	my_file.write("<name>fs.default.name</name>\n")
	my_file.write("<value>hdfs://{0}:9001</value>\n".format(NN_ip))
	my_file.write("</property>\n")
	my_file.write("</configuration>\n")
	my_file.close()

	os.system("touch nn-file_hdfs.xml")
	my_file = open("nn-file_hdfs.xml" , "r+")
	my_file.truncate(0)
	my_file.write("<?xml version='1.0'?>\n")
	my_file.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n")
	my_file.write("<configuration>\n")
	my_file.write("<property>\n")
	my_file.write("<name>dfs.name.dir</name>\n")
	my_file.write("<value>/{0}</value>\n".format(nnfold))
	my_file.write("</property>\n")
	my_file.write("</configuration>\n")
	my_file.close()
	
	#Copy files
	os.system("scp nn-file_hdfs.xml root@{0}:/etc/hadoop/hdfs-site.xml".format(NN_ip))
	os.system("scp nn-file_core.xml root@{0}:/etc/hadoop/core-site.xml".format(NN_ip))

	#Start Service
	os.system("ssh root@{0} hadoop namenode -format".format(NN_ip))
	os.system("ssh root@{0} systemctl stop firewalld".format(NN_ip))
	os.system("ssh root@{0} hadoop-daemon.sh start namenode".format(NN_ip))
	os.system("ssh root@{0} jps".format(NN_ip))
	os.system("tput setaf 3")
	input("Press Enter to Continue")
	os.system("tput setaf 3")

# Configure the Datanode
def datanode_config():
	global DD_ip
	print()
	os.system("tput setaf 3")
	DD_ip = input("Enter the Name Node IP : ")
	os.system("tput setaf 7")
	os.system("ssh-keygen")
	os.system("ssh-copy-id root@{0}".format(DD_ip))
	os.system("tput setaf 3")
	input("Key Successfully Copied Press Enter to Continue")
	os.system("tput setaf 7")
	
	# Remove all the files and software if exist	
	os.system("ssh root@{0} yum remove hadoop -y".format(DD_ip))
	os.system("ssh root@{0} yum remove jdk -y".format(DD_ip))
	os.system("ssh root@{0} rm -rf /etc/hadoop".format(DD_ip))
    	
	#Copy and Insatall Software
	os.system("tput setaf 3")
	print("\t  Copying Required Softwares Namenode ")
	print("\t -------------------------------------\n")
	os.system("tput setaf 7")
	os.system("scp /root/jdk-8u171-linux-x64.rpm {0}:/root".format(DD_ip))
	os.system("scp /root/hadoop-1.2.1-1.x86_64.rpm {0}:/root".format(DD_ip))
	os.system("scp /root/epel-release-latest-8.noarch.rpm {0}:/root".format(DD_ip))
	os.system("tput setaf 3")
	print("\t  Copying Required Softwares Namenode ")
	print("\t -------------------------------------\n")
	os.system("tput setaf 7")
	os.system("ssh root@{0} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force".format(DD_ip))
	os.system("ssh root@{0} rpm -ivh /root/jdk-8u171-linux-x64.rpm".format(DD_ip))

	#Folder Associate with Datanode
	os.system("tput setaf 3")
	ddfold = input("Enter the Folder Name to associate with Data Node : ")
	os.system("tput setaf 7")
	os.system("ssh {} mkdir /{}".format(DD_ip, ddfold))
	
    	
	#Create Datanode hdfs and core file
	os.system("touch nn-file_core.xml")
	my_file = open("nn-file_core.xml","r+")
	my_file.truncate(0)
	my_file.write("<?xml version='1.0'?>\n")
	my_file.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n")
	my_file.write("<configuration>\n")
	my_file.write("<property>\n")
	my_file.write("<name>fs.default.name</name>\n")
	my_file.write("<value>hdfs://{0}:9001</value>\n".format(NN_ip))
	my_file.write("</property>\n")
	my_file.write("</configuration>\n")
	my_file.close()

	#os.system("rm -rf nn-file_hdfs")
	os.system("touch nn-file_hdfs.xml")
	my_file = open("nn-file_hdfs.xml" , "r+")
	my_file.truncate(0)
	my_file.write("<?xml version='1.0'?>\n")
	my_file.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n")
	my_file.write("<configuration>\n")
	my_file.write("<property>\n")
	my_file.write("<name>dfs.name.dir</name>\n")
	my_file.write("<value>/{0}</value>\n".format(ddfold))
	my_file.write("</property>\n")
	my_file.write("</configuration>\n")
	my_file.close()
	
	#Copy files
	os.system("scp nn-file_hdfs.xml root@{0}:/etc/hadoop/hdfs-site.xml".format(DD_ip))
	os.system("scp nn-file_core.xml root@{0}:/etc/hadoop/core-site.xml".format(DD_ip))

	#Start Service
	#os.system("ssh root@{0} hadoop namenode -format".format(DD_ip))
	os.system("ssh root@{0} systemctl stop firewalld".format(DD_ip))
	os.system("ssh root@{0} hadoop-daemon.sh start datanode".format(DD_ip))
	os.system("ssh root@{0} jps".format(DD_ip))
	os.system("tput setaf 3")
	input("Press Enter to Continue")
	os.system("tput setaf 3")

# Configure Hadoop Client
def client_config():	
	# Remove all the files and software if exist	
	os.system("yum remove hadoop -y")
	os.system("yum remove jdk -y")
	os.system("rm -rf /etc/hadoop")
	os.system("tput setaf 3")
	print("\t  Installing Required Softwares Client ")
	print("\t -------------------------------------\n")
	os.system("tput setaf 7")
	os.system("rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force")
	os.system("rpm -ivh /root/jdk-8u171-linux-x64.rpm")
	
    	
	#Create Datanode hdfs and core file
	#os.system("rm -rf nn-file_core")
	os.system("touch nn-file_core.xml")
	my_file = open("nn-file_core.xml","r+")
	my_file.truncate(0)
	my_file.write("<?xml version='1.0'?>\n")
	my_file.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n")
	my_file.write("<configuration>\n")
	my_file.write("<property>\n")
	my_file.write("<name>fs.default.name</name>\n")
	my_file.write("<value>hdfs://{0}:9001</value>\n".format(NN_ip))
	my_file.write("</property>\n")
	my_file.write("</configuration>\n")
	my_file.close()

	#Copy the file to client
	os.system("cp nn-file_core.xml /etc/hadoop/core-site.xml")
	os.system("tput setaf 3")
	input("Press Enter to Continue")
	os.system("tput setaf 3")

# Hadoop Configuration Menu
def hadoop_config():
	while True:
		os.system("clear")
		os.system("tput setaf 1")
		print("\t\t    ------------------------------")
		print("\t\t    | Welcome to Remote Login !! |")
		print("\t\t    ------------------------------")
		os.system("tput setaf 7")

		os.system("tput setaf 2")
		print("""
		  Press 1 : To Configure Name Node
		  Press 2 : To Configure Data Node
		  Press 3 : To Return Previous Menu
		""")
		
		print()
		os.system("tput setaf 3")
		ch = input("\t\t  Enter your Choice : ")
		os.system("tput setaf 7")

		if int(ch) == 1:
			namenode_config()

		elif int(ch) == 2:
			datanode_config()
			
		elif int(ch) == 3:
			break

		else:
			os.system("tput setaf 3")
			print("Please Select Right Choice")
			os.system("tput setaf 7")
			input()
	
# Hadoop Main Menu
def hadoop_menu():
	while True:
		os.system("clear")
		os.system("tput setaf 1")
		print("\t\t   ----------------------------------")
		print("\t\t   | Welcome to Hadoop Assistant !! |")
		print("\t\t   ----------------------------------")
		os.system("tput setaf 7")

		os.system("tput setaf 2")
		print("""
		  Press 1 : To Configure Hadoop Cluster
		  Press 2 : To Configure Hadoop Client
		  Press 3 : To Check Hadoop Report
		  Press 4 : To Upload a File
		  Press 5 : To Create a File
		  Press 6 : To View a File
		  Press 7 : To Delete a File
		  Press 8 : To List Files
		  Press 9 : To Return to Previous Menu
		""")
		
		print()
		os.system("tput setaf 3")
		ch = input("\t\t  Enter your Choice : ")
		os.system("tput setaf 7")

		if int(ch) == 1:
			hadoop_config()
		
		elif int(ch) == 2:
			client_config()

		elif int(ch) == 3:
			print()
			os.system("hadoop dfsadmin -report") 
			os.system("tput setaf 3")
			input("Press Enter to continue")
			os.system("tput setaf 7")

		elif int(ch) == 4:
			print()
			os.system("tput setaf 3")
			file_name = input("Enter the File Name : ")
			os.system("tput setaf 7")
			os.system("hadoop fs -put {0} /".format(file_name)) 
			os.system("tput setaf 3")
			input("Press Enter to continue")
			os.system("tput setaf 7")

		elif int(ch) == 5:
			print()
			os.system("tput setaf 3")
			file_name = input("Enter the File Name : ")
			os.system("tput setaf 7")
			os.system("hadoop fs -touchz /{0}".format(file_name)) 
			os.system("tput setaf 3")
			input("Press Enter to continue")
			os.system("tput setaf 7")

		elif int(ch) == 6:
			print()
			os.system("tput setaf 3")
			file_name = input("Enter the File Name : ")
			os.system("tput setaf 7")
			os.system("hadoop fs -cat /{0}".format(file_name)) 
			os.system("tput setaf 3")
			input("Press Enter to continue")
			os.system("tput setaf 7")

		elif int(ch) == 7:
			print()
			os.system("tput setaf 3")
			file_name = input("Enter the File Name : ")
			os.system("tput setaf 7")
			os.system("hadoop fs -rm /{0}".format(file_name)) 
			os.system("tput setaf 3")
			input("Press Enter to continue")
			os.system("tput setaf 7")

		elif int(ch) == 8:
			print()
			os.system("hadoop fs -ls /") 
			os.system("tput setaf 3")
			input("Press Enter to continue")
			os.system("tput setaf 7")

		elif int(ch) == 9:
			break

		else:
			print("Please Select Correct Choice")
			input()



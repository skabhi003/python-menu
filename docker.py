import os

# Configure and Install Docker
def docker_config():
        print('yum should be configured before docker installation .')
        os.system('sudo yum config\-manager \-\-add\-repo\=https\:\/\download.docker.com\/linux\/centos\/docker\-ce\.repo')
        os.system('dnf install docker-ce --nobest -y')
        os.system('systemctl start docker')
        os.system('systemctl status docker')

# Configure Web Server on Docker
def docker_web():
	os.system('docker run -dit --name webos -p 8080:80 centos')
	os.system('docker exec webos yum install httpd -y')
	os.system('docker cp index.html webos:/var/www/html/')
	os.system('docker exec webos /usr/sbin/httpd')
	input()

# Launch Python Interpreter on Docker
def docker_py():
	os.system('docker run -dit --name pyos centos')
	os.system('docker exec pyos yum install python3 -y')
	os.system('docker cp hello.py pyos:/')
	print()
	os.system('docker exec pyos python3 /hello.py')
	input()

# Launch GUI APP inside Docker	
def docker_gui():
	os.system('docker run -it --name gui --env="DISPLAY" --net=host firefox:v1')
	input()

# Docker Menu
def docker_menu():
	while True:
		os.system("clear")
		os.system("tput setaf 1")
		print("\t\t  ----------------------------------")
		print("\t\t  | Welcome to Docker Assistant !! |")
		print("\t\t  ----------------------------------")
		os.system("tput setaf 7")

		os.system("tput setaf 2")
		print("""
		  Press 1 : To Configure Docker
		  Press 2 : To Search Docker Image
		  Press 3 : To Pull Docker Image
		  Press 4 : To List Container 
		  Press 5 : To Remove all the Container
		  Press 6 : To Configure Webserver on Docker
		  Press 7 : To Run Python Code on Docker
		  Press 8 : To Launch GUI program in Docker
		  Press 9 : To Return to Previous Menu
		""")
		
		print()
		os.system("tput setaf 3")
		ch = input("\t\t  Enter your Choice : ")
		os.system("tput setaf 7")

		if int(ch) == 1:
			docker_config()

		elif int(ch) == 2:
			os.system("tput setaf 3")
			image_name = input("Enter the OS Name : ")
			os.system("tput setaf 7")
			os.system("docker search {0}".format(image_name))
			input()

		elif int(ch) == 3:
			os.system("tput setaf 3")
			image_name = input("Enter the OS Name : ")
			os.system("tput setaf 7")
			os.system("docker pull {0}".format(image_name))
			input()

		elif int(ch) == 4:
			os.system("docker ps -a")
			input()

		elif int(ch) == 5:
			os.system("docker rm -f $(docker ps -aq)")
			input()

		elif int(ch) == 6:
			docker_web()

		elif int(ch) == 7:
			docker_py()
		
		elif int(ch) == 8:
			docker_gui()

		elif int(ch) == 9:
			break

		else:
			print("Please Select Correct Choice")
			input()



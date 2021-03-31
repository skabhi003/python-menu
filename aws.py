import os

# AWS Menu
def aws_menu():
	while True:
		os.system("clear")
		os.system("tput setaf 1")
		print("\t\t    -------------------------------")
		print("\t\t    | Welcome to AWS Assistant !! |")
		print("\t\t    -------------------------------")
		os.system("tput setaf 7")

		os.system("tput setaf 2")
		print("""
		  Press 1 : To Configure AWS
		  Press 2 : To Create Key-pair
		  Press 3 : To Create Security Group
		  Press 4 : To Launch an Instance
		  Press 5 : To Describe an Instance
		  Press 6 : To Return to Previous Menu
		""")
		
		print()
		os.system("tput setaf 3")
		ch = input("\t\t  Enter your Choice : ")
		os.system("tput setaf 7")

		if int(ch) == 1:
			print()
			os.system("aws configure")
			os.system("tput setaf 3")
			input("Press Enter to continue")
			os.system("tput setaf 7")

		elif int(ch) == 2:
			print()
			os.system("tput setaf 3")
			key_name = input("Enter Key-pair Name : ")
			os.system("tput setaf 7")
			os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
			os.system("tput setaf 3")
			input("Press Enter to continue")
			os.system("tput setaf 7")

		elif int(ch) == 3:
			print()
			os.system("tput setaf 3")
			sg_name = input("Enter Security Group Name : ")
			sg_desc = input("Enter the Description : ")
			os.system("tput setaf 7")
			os.system("aws ec2 create-security-group --group-name {0} --description {1}".format(sg_name, sg_desc))
			print("Add Rule to Security Group")
			os.system("tput setaf 3")
			protocol = input("Enter the Protocol : ")
			port = input("Enter the Port Number : ")
			cidr = input("Enter the CIDR : ")
			os.system("tput setaf 7")
			os.system('aws ec2 authorize-security-group-ingress --group-name {0} --protocol {1} --port {2} --cidr {3}'.format(sg_name, protocol, port, cidr))
			os.system("tput setaf 3")
			input("Press Enter to continue")
			os.system("tput setaf 7")

		elif int(ch) == 4:
			print()
			os.system("tput setaf 3")
			instance_type = input("Enter teh Instance Type : ")
			key_name = input("Enter the Key-pair Name : ")
			count = input("Enter the Count : ")
			os.system("tput setaf 7")
			os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type {0} --key-name {1} --subnet-id subnet-0a420fc4eb459022a --count {2}".format(instance_type, key_name, count))
			os.system("tput setaf 3")
			input("Press Enter to continue")
			os.system("tput setaf 7")

		elif int(ch) == 5:
			print()
			os.system("aws ec2 describe-instances")
			os.system("tput setaf 3")
			input("Press Enter to continue")
			os.system("tput setaf 7")

		elif int(ch) == 6:
			break

		else:
			print("Please Select right Choice")
			input()




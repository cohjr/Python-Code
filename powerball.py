
#!/usr/bin/env python

# Employee Powerball generator
# Chuck O'Hanlon
# 7-6-16

import random

emp_numbers = ""
all_employees = []
one_employee = []
powerball_numbers = []

def display_all_employees(emp_numbers):
	""" Print all employees and pb numbers """
	print('\n')
	for emp_number in emp_numbers:
		print(str(emp_number))
	#print('\n')
	
def validate_number(number):
	""" validate number is integer and in range """
	num = str(number)
	if num.isdigit() != True:
		return False
	if int(number) < 1:
		return False
	if int(number) > 69:
		return False
	return True

def validate_PB(number):
	""" validate PB number is integer and in range """
	num = str(number)
	if num.isdigit() != True:
		return False
	if number < 1:
		return False
	if number > 26:
		return False
	return True
	
def calculate_numbers(emp_numbers):
	""" generate powerball numbers check and count duplicates """
	num_dups1 = ""
	num_dups2 = ""
	curr_value = ""
	curr_group = []
	pb_num = ""
	high_dup = ""
	dup_count = 0   #use to keep track of dups
	dup_numbers = [] #use to keep track of dups
	
	number_count = len(emp_numbers)
	index = number_count - 1
	
	#print('Total ' + str(number_count))
	print('\n')
	
	# Loop through each employee and each group of numbers

	for i in range(1,7):
		# Fill list of current row
		for emp_number in emp_numbers:
			curr_value = emp_number[i]
			curr_group.append(curr_value)
		#print(curr_group)
		
		# Check for duplicate in current group if none generate randomly from row.
		num_dups1 = 0
		high_dup = 0 
		dup_count = 0
		dup_numbers = [] # keep track of dup number and occurances
		

		for cur_num in curr_group:
			#dup_count = 0
			#dup_numbers = []
			num_dups1 = curr_group.count(cur_num)
			
			#Get highest dup 
			if num_dups1 > high_dup:
				high_dup = num_dups1
				pb_num = cur_num
							
			#No Dups Generate randomly	
			if high_dup == 1:
			    #Generate randomly from list row numbers
				rn = random.randint(0,index)
				pb_num = curr_group[rn]
				
			# Keep track of duplicates handle tie (Not Working comment out)
			#if num_dups1 == high_dup and num_dups1 > 1:
			#	dup_count = num_dups1
			#	dup_numbers.append(cur_num)
			#	print(str(dup_count))
			#	print(dup_numbers)
				
		#print('# dups: ' + str(high_dup))
		#print('# PB number: ' + pb_num) 
		
		powerball_numbers.append(pb_num)
		# clear current list
		curr_group = []
		
	# Display winning number
	print('\nPowerball winning number:\n')
	print(str(powerball_numbers[0:5]) + ' Powerball: ' + str(powerball_numbers[5]))
		
def get_name_and_number():
	""" Prompt user for name and powerball numbers """
	prompt = ""
 
	while prompt != 'n':
	
		number_1 = "0"
		number_2 = "0"
		number_3 = "0"
		number_4 = "0"
		number_5 = "0"
		number_PB = "0"
	
	
		one_employee = []
		
		# Get Name and Number for each employee.
		first_name = input('\nEnter your first name: ')
		last_name = input('Enter your last name: ')
		one_employee.append(first_name + ' ' + last_name)
		
		while validate_number(number_1) == False:
			number_1 = input('select 1st # (1 thru 69): ')
		one_employee.append(number_1)
		while validate_number(number_2) == False:
			number_2 = input('select 2nd # (1 thru 69 excluding  ' + number_1 + '):')
			if number_2 == number_1:
				number_2 = "0"
		one_employee.append(number_2)
		while validate_number(number_3) == False:
			number_3 = input('select 3rd # (1 thru 69 excluding  ' + number_1 + ' and ' + number_2 + '):')
			if number_3 == number_2 or number_3 == number_1:
				number_3 = "0"
		one_employee.append(number_3)
		while validate_number(number_4) == False:
			number_4 = input('select 4th # (1 thru 69 excluding  ' + number_1 + ', ' + number_2 + ' and ' + number_3 + '):')
			if number_4 == number_3 or number_4 == number_2 or number_4 == number_1:
				number_4 = "0"
		one_employee.append(number_4)
		while validate_number(number_5) == False:
			number_5 = input('select 5th # (1 thru 69 excluding  ' + number_1 + ', ' + number_2 + ', ' + number_3 + ' and ' + number_4 + '):')
			if number_5 == number_4 or number_5 == number_3 or number_5 == number_2 or number_5 == number_1:
				number_5 = "0"
		one_employee.append(number_5)
		while validate_number(number_PB) == False:
			number_PB = input('select Power Ball # (1 thru 26): ')
		one_employee.append(number_PB)

		all_employees.append(one_employee)
		prompt = input('\nAdd another? (y or n):')

# Main Program
get_name_and_number()
display_all_employees(all_employees)
calculate_numbers(all_employees)
exit = input("\nPress Any Key To Continue ... ")
 
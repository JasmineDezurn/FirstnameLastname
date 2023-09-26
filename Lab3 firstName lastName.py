'''
09/21/2023

vj0100jc

CIS121
'''
earned_income = float(input())
maritial_status = float(input())

if(0 <= earned_income <= 11000) and (0 <= maritial_status <= 22000):
	print(f'10%')
elif(22001 <= earned_income <= 44725) and (22001 <= maritial_status <= 89450):
	print(f'12%')
elif(44726 <= earned_income <= 95375) and (89451 <= maritial_status <= 190750):
	print(f'22%')

x = { "name":"Vivek Shelke", 
		"assignment" : [80, 78,94, 85], 
		"test" : [82, 85], 
		"lab" : [88.25, 90.20] 
	} 
		

y = { "name":"Prateek Dutta", 
		"assignment" : [82, 76,90, 84], 
		"test" : [82, 88], 
		"lab" : [86.25, 89.60] 
		} 

z = { "name" : "Lana Rohdes", 
		"assignment" : [77, 82, 60,75], 
		"test" : [78, 77], 
		"lab" : [80, 80] 
		} 
		
p = { "name" : "Awa Adam", 
		"assignment" : [67, 55, 77, 65], 
		"test" : [60, 72], 
		"lab" : [69, 74.56] 
	} 
		 
q = { "name" : "Mia Khalifa", 
		"assignment" : [68, 89, 60, 90], 
		"test" : [65, 82], 
		"lab" : [76.29, 81.6] 
	} 

def get_average(marks): 
	total_sum = sum(marks) 
	total_sum = float(total_sum) 
	return total_sum / len(marks) 

def calculate_total_average(students): 
	assignment = get_average(students["assignment"]) 
	test = get_average(students["test"]) 
	lab = get_average(students["lab"]) 

	return (0.1 * assignment +
			0.7 * test + 0.2 * lab) 


def assign_letter_grade(score): 
	if score >= 90: return "A+"
	elif score >= 80: return "A"
	elif score >= 70: return "B"
	elif score >= 60: return "C"
	else : return "D"

def class_average_is(student_list): 
	result_list = [] 

	for student in student_list: 
		stud_avg = calculate_total_average(student) 
		result_list.append(stud_avg) 
		return get_average(result_list) 

students = [x,y,z,p,q] 
for i in students : 
	print(i["name"]) 
	print("*********//////////********") 
	print("Average marks of %s is : %s " %(i["name"], 
						calculate_total_average(i))) 
						
	print("Letter Grade of %s is : %s" %(i["name"], 
	assign_letter_grade(calculate_total_average(i)))) 
	
	print() 


class_av = class_average_is(students) 

print( "Class Average is %s" %(class_av)) 
print("Letter Grade of the class is %s "
		%(assign_letter_grade(class_av))) 

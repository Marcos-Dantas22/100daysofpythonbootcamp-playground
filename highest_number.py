student_scores = [158, 142, 185, 128, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

max_number = 0

for score in student_scores:
	if score > max_number:
		max_number = score

print(max_number)
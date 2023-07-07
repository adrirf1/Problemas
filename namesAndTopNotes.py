def top_note(student:dict):
	nombre = student["name"]
	highest = max(student.get("notes"))
	return {"name":nombre,"top_note":highest}

print(top_note({ "name": "John", "notes": [3, 5, 4] }))
student={"name":"Daksh","age":7,"grade":3,"subjects":["Maths","Science","English","Hindi"]}

students={"student1":"Harsh","student2":"Hitesh","student3":"Harsh"}
result={}
for key,value in students.items():

    if value not in result.values():
        result[key]=value
print(result)
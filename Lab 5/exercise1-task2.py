resources = [
[101, "Laptop", "Electronics", 8],
[102, "Projector", "Electronics", 0],
[103, "Whiteboard", "Classroom", 5],
[104, "Microphone", "Audio", 3],
[105, "Camera", "Electronics", 2],
]
def search_by_category(resources, category):
    found = False
    for x in  resources:
        if x[2].lower()==category.lower():
            print(x)
            found = True
    if found == False:
            print("Not Found")
search_by_category(resources,"Classroom")
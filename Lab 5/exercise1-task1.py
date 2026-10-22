resources = [[101, "Laptop", "Electronics", 8],
[102, "Projector", "Electronics", 0],
[103, "Whiteboard", "Classroom", 5],
[104, "Microphone", "Audio", 3],
[105, "Camera", "Electronics", 2]
]
def display_resources(resources):
    if len(resources)==0:
        print("Resources Not Available")
        return
    for x in resources:
        print("Id",x[0])
        print("Name",x[1])
        print("Category",x[2])
        print("Quantity",x[3])
display_resources(resources)
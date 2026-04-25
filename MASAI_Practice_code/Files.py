with open("family.txt","w") as file:
    file.write("Ramesh Polaveni\n")
    file.write("Anusha Polaveni\n")
    file.write("Rivansh Polaveni\n")
    file.write("Vrushali Polaveni\n")
    file.write("Varamma Polaveni\n")
with open("family.txt","r") as file:
    content=file.read()
    print(content)
with open("family.txt","a") as file:
    file.write("Dinnu and Vrushali")
with open("family.txt","r") as file:
    line1=file.readlines()
    print(line1)
with open("family.txt","r") as file:
    line2=file.readline()
    print(line2)
with open("family.txt","r") as file:
    for line in file.readlines():
        clean=line.strip()
        parts=clean.split(",")
        family=int(parts[0])

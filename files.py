# 10.1, 10.2

filename = 'file_to_read.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


work = ''
for line in lines:
    line = line.replace('debian', 'Windows')
    #print(line.replace('django','Windows').)
    work += line

print(work.replace('Windows', 'debian', 2))

# 10.3

imie = input("\nPodaj imię: ")
nazwisko = input("Podaj nazwisko: ")

guests = 'guest_book.txt'

#file_guest = imie + "." + nazwisko + ".txt"

#with open(file_guest,'w') as file_object:
#    file_object.write(imie.title() +' ' + nazwisko.title())

while True:
    imie = input("\nPodaj imię: (q for quit) ")
    if imie != "q":
        with open(guests, 'a') as file_object:
            file_object.write(imie + "\n")
    else:
        break




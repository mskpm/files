# 10.1, 10.2

#filename = 'file_to_read.txt'

#with open(filename) as file_object:
#    lines = file_object.readlines()


#work = ''
#for line in lines:
#    line = line.replace('debian', 'Windows')
#    #print(line.replace('django','Windows').)
#    work += line

#print(work.replace('Windows', 'debian', 2))

# 10.3, 10.5

#imie = input("\nPodaj imię: ")
#nazwisko = input("Podaj nazwisko: ")


#file_guest = "programming_pool.txt"

#poll_data = input("\nDlaczego lubisz programowanie?")

#with open(file_guest,'a') as file_object:
#    file_object.write(imie.title() +' ' + nazwisko.title() + '\n')
#    file_object.write("\t" + poll_data + '\n')

# 10.4

#guests = 'guest_book.txt'
#while True:
#    imie = input("\nPodaj imię: (q for quit) ")
#    if imie != "q":
#        with open(guests, 'a') as file_object:
#            file_object.write(imie + "\n")
#    else:
#        break

#10.6, 10.7

#print("Podaj dwie liczby. (aby zakończyć wpisz 'q')")
#while True:
#    liczba1 = input("Podaj pierwszą liczbę: ")
#    if liczba1 == 'q':
#        break
#    check1 = True
#    try:
#        liczba1 = int(liczba1)
#    except ValueError:
#        print("Podaj pierwszą liczbę: ", end='\r', flush=True)
#        check1 = False
#    if check1 == True:
#        break

#while True:
#    liczba2 = input("Podaj drugą liczbę: ")
#    if liczba2 == 'q':
#            break
#    check2 = True
#    try:
#        liczba2 = int(liczba2)
#    except ValueError:
#        print("Podaj drugą liczbę: ", end='\r', flush=True)
#        check2 = False
#    if check2 == True:
#        break
#print("Podałeś liczby: " + str(liczba1) + ", " + str(liczba2))
    
#10.8, 10.9

#filename_cats = 'cats.txt'
#filename_dogs = 'dogs.txt'
#cats = ''
#dogs = ''

#try:
#    with open(filename_cats) as file_object:
#        cats_lines = file_object.readlines()
#except FileNotFoundError:
#    #msg = "Nie mogę znaleźć pliku: " + filename_cats + "."
#    #print(msg)
#    pass
#else:
#    for cats_line in cats_lines:
#        cats += cats_line 
    
#try:
#    with open(filename_dogs) as file_object:
#        dogs_lines = file_object.readlines()
#except FileNotFoundError:
#    #msg = "Nie mogę znaleźć pliku: " + filename_dogs + "."
#    #print(msg)
#    pass
#else:
#    for dogs_line in dogs_lines:
#        cats += dogs_line

#print(cats)
#print("\n"+ dogs)

#10.10

#def count_words(filename):
#    """ Obliczanie przybliżonej liczby słów w danym pliku"""
#    try:
#        with open(filename) as f_obj:
#            contents = f_obj.read()
#    except FileNotFoundError:
#        msg = "Nie mogę znaleźć pliku: " + filename + "."
#        print(msg)
#    else:
#        # Obliczanie przybliżonej liczby słów w danym pliku
#        words = contents.split()
#        num_words = len(words)
#    return num_words

#ilość_słów = count_words("file_to_read.txt")
#print(ilość_słów)

#10.11

import json

def check_input_number(number):
    """ Sprawdza liczbę od użytkownika"""
    try:
        number = int(number)
    except ValueError:
        check = False 
    else:
        check = True
    return check


def store_number_json(filename, liczba):
    """ Zapisuje liczbę w pliku """
    with open(filename,'w') as jfile:
        json.dump(liczba, jfile)


def get_favorite_number(liczba, imie):
    """ Pobiera liczbę z pliku o nazwie imie.txt """
    while True:
        if liczba == 'q':
            break
        if check_input_number(liczba):
            store_number_json(imie + ".txt", liczba)
            print("Twója ulubiona liczba " + liczba + " została zapisana.")
            break
        else:
            print("Podałeś nieprawidłową liczbę.")

def show_gather_favourite_number(imie):
    """ Pobiera i wyświetla ulubioną liczbę z pliku imie.txt """
    try:
        with open(imie + ".txt") as f_obj:
            liczba = json.load(f_obj)
    except FileNotFoundError:
        print("\nMiło mi Cię poznać, ale nie znam Twojej ulubionej liczby.")
        liczba = input("\nPodaj ulubioną liczbę: ")
        get_favorite_number(liczba, imie)
    else:
        print("Witaj " + imie + ", Twoja ulubiona liczba to: " + liczba)

show_gather_favourite_number('Piotr')
show_gather_favourite_number('Adam')
show_gather_favourite_number('Małgorzata')
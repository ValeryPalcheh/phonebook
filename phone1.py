def show_menu():
    print('1. Распечатать справочник\n'
          '2. Найти телефон по фамилии\n'
          '3. Изменить номер телефона\n'
          '4. Удалить запись\n'
          '5. Найти абонента по номеру телефона\n'
          '6. Добавить абонента в справочник\n'
          '7. Закончить работу\n')
    choice=int(input('Выберите действие: '))
    return choice



def work_with_phonebook():

    choice=show_menu()
    phone_book=read_txt('phone_book.txt')
    while (choice!=7):
        if choice==1:
            print(phone_book)

        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))

        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new number ')
            print(change_number(phone_book,last_name,new_number))

        elif choice==4:
            last_name=input('lastname ')
            print(delete_by_lastname(phone_book,last_name)) 

        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))

        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phone_book.txt',phone_book)

        choice=show_menu()    



def write_txt(filename , phone_book):
    with open(filename , 'w' ,encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')

            

def read_txt(filename):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание' ]

    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields,   line.split(',')))
            phone_book.append(record)

    return phone_book

def find_by_lastname(phone_book, last_name):
    for item in phone_book:
        if last_name == item['Фамилия']:
            return item['Телефон']
    return 'Абонент не найден'

def add_user(phone_book, user_data):
    phone_book.append(user_data)
    write_txt(filename , phone_book)
    return 'Абонент ' + user_data['Имя'] + ' ' + user_data['Фамилия'] + ' добавлен'







work_with_phonebook()




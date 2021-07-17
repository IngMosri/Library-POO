import singin_user_menu

class Menu_user:
    def user_main_menu():
        
     
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num

    def show_menu_user():

        salir = False
        opcion = 0
        
        while not salir:
        
            print ("1. Login")
            print ("2. Sign")
            print ("3. Exit")
            
            print ("choose one option ")
        
            opcion = Menu_user.user_main_menu()
        
            if opcion == 1:
                print ("Option 1")
            elif opcion == 2:
                print ("Option 2")
            elif opcion == 3:
                print("Option 3")
                salir = True
            else:
                print ("Choose the option beetween 1 and 3")
        
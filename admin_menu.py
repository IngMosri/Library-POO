class Admin_menu:
    def main_admin_menu():
     
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num
     
    def show_admin_menu():
    
        salir = False
        opcion = 0
        
        while not salir:
        
            print ("1. inventory")
            print ("2. Account manegment")
            print ("3. book search")
            print ("4. exit ")
            
            print ("choose one option ")
        
            opcion = Admin_menu.main_admin_menu()
        
            if opcion == 1:
                print ("Option 1")
            elif opcion == 2:
                print ("Option 2")
            elif opcion == 3:
                print("Option 3")
            elif opcion == 4:
                salir = True
            else:
                print ("Choose the option beetween 1 and ")
        
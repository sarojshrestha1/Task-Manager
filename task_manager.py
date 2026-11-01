
def main():
    while True:
        print("\n\nTask manager")
        print("choose the option")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Display all task")
        print("4. Exit")
        try:
            choice= int(input("\nEnter your choice: "))

        except ValueError:
            print("The choice should be in integer")
            continue
        
        match choice:
            case 1:
                add_task()
                

            case 2:
                delete_task()
                

            case 3:
                display_task()
                

            case 4:
                break

            case _:
                print("Please enter the valid choice")
                
            

def add_task():
    print("\nYou wanna add task")
    try:
        n = int(input("Enter how many task you wanna enter: "))

    except ValueError:
        print("plese enter a integer")
        return

    if n<1:
        print("please Enter the number that is greater than 0")
        return

    try:
        with open("task.txt", 'r') as file:
            line = file.readlines()
            sn= len(line)
    except FileNotFoundError:
        sn=0
    

    for _ in range(n):
        sn=sn+1
        task= input("Enter the task: ")

        while True:
            try:
                imp= int(input("Enter the importance (0-10):"))

            except ValueError:
                print("Please enter in integer")
                continue
                
            
            if imp<0 or imp>10:
                print("Please enter the importance in range of (0-10)!")

            else:
                break
                
        
        with open("task.txt",'a') as file:
            file.writelines(f"{sn}. {task},{imp}"+"\n")
        
def delete_task():
    print("\nYou wanna delete task")
    try:
        with open("task.txt", 'r') as file:
            line = file.readlines()
            sn= len(line)
    except FileNotFoundError:
        print("There is no fileof this name")
        return

    try:
        num=int(input("Which line you wanna delete:"))
        
    except ValueError:
        print("Please write in integer")
        return

    if num<1 or sn<num:
        print("There is no line in file")
        return

    
    with open("task.txt", 'r') as file:
        line=file.readlines()

        line.pop(num-1)

        with open("task.txt", 'w') as file:
            file.writelines(line)


    

def display_task():
    print("\nYou wanna display task")
    try:
        with open("task.txt",'r') as file:
            while True:
                line=file.readline()
                
                if not line:
                    break
                print(line)  

    except FileNotFoundError:
        print("There is no file to display")
        return


if __name__=="__main__":
    main()
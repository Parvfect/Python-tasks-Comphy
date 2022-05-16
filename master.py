
import task1 as t1
import task2 as t2
import task3 as t3
import task4 as t4
import task5 as t5
import task6 as t6
import task7 as t7


def main(task=0):
    
    if task==0:
        print("Which task do you want to run?")
        print("1. Task 1\n 2. Task 2\n 3. Task 3\n 4. Task 4\n 5. Task 5\n 6. Task 6\n 7. Task 7")
        task = int(input("Enter task number: "))

    if task == 1:
        t1.main()
    elif task == 2:
        t2.main()
    elif task == 3:
        t3.main()
    elif task == 4:
        t4.main()
    elif task == 5:
        t5.main()
    elif task == 6:
        t6.main()
    elif task == 7:
        t7.main()

main()
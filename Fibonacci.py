'''
Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.
'''

#importing necessary libraries
import array

fibSequence = []

#main function
def main():
    global fibSequence
    n_value = input('Enter a value greater than 5, but up to 900, or \'Exit\' to exit: '); #Grabbing the users input

    #Ensuring users input is valid
    if(n_value == 'Exit' or n_value == 'exit'):
        exit()
        return
    elif (n_value.isdigit() == False):
        print('\nYou did not enter a valid number...')
        main()
    elif (int(n_value) <= 5):
        print('\nYou did not enter a value greater than 5...')
        main()
    elif (int(n_value) > 900):
        print('\nYou enter a value greater than 900...')
        main()
    else: 
        run_fib(n_value)
        n_value = input('\nWould you like to rerun? (Type \'Y \' to continue or \'N\' to exit): ');
        if (n_value == 'Y' or n_value == 'y'):
            print('\nRerunning the program...\n')
            fibSequence.clear() #Clearing the array on rerun
            main()
        else:
            print('\nExiting...')
            exit()
        
# Outputting the fibonacci run
def run_fib(n, run = 0): # n is the value entered by the users, run is the counter/tracker to ensure function is not executing more than needed
    #Returns if 'run' is at the value entered, else it will run the fibonacci function
    if (run >= int(n)):
        return
    elif (len(fibSequence) <= int(n)):
        fib(run) #Calling the fibonacci function
        print('fib run ' + str(run + 1) + ": " + str(fibSequence[run])) #Returns the value if 'run' is not at the value entered
        run_fib(int(n), run + 1) #Recalling  if 'run' is not at the value entered
        

# Fibonacci function
def fib(n): # n is the run value passed by run fib
    if int(n) <= 0: # If n is, or is less than, 0, return 0
        return fibSequence.append(0)
    elif int(n) == 1: # If n is 1, return
        return fibSequence.append(1)
    else: # If greater than one, than we will calculate as needed appropriately using recursion.
        # Running recursion here as well to get appropriate fibonacci values to
        # return appropriate value
        return fibSequence.append(fibSequence[n - 1] + fibSequence[n - 2])

# Exit function to end application
def exit():
    SystemExit()
    print('\nExited the application...')

# Calling the main function
main()
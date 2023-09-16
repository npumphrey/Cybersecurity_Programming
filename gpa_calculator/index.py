def get_grade_input(grade_dict):
  # TODO: Write a function that asks the user for a letter grade. 
  # If the letter grade is in the grade_dict, return it. 
  # Otherwise, ask the user again for a valid letter grade.

    while True:

        grade = input("Please enter a valid grade letter: ")

        if grade in grade_dict:

            return grade



def calculate_gpa(grade_value_list):
  # TODO: Write a function that calculates the GPA from a list of GPA values

    return sum(grade_value_list)/len(grade_value_list)



def main():
  # Dictionary that converts letter values to numeric equivalents
    grade_dict = {'A+':4.2, 'A':4, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+':2.3, 'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1.0, 'F':0}
  # List of all letter grades entered
    grade_list = []
  # List of all grade values based on letter grades entered
    grade_value_list = []
  
  # TODO: Write the primary logic of your program here

    while True:

        grade = get_grade_input(grade_dict)
        grade_list.append(grade)
        grade_value_list.append(grade_dict[grade])

        print ("Your grades are ", grade_list)
        print ("Your GPA is ", calculate_gpa(grade_value_list))
        
        while True:
            
            cont = input("Enter C to continue or X to finish: ")
            
            if cont == "C":
                break

            elif cont == "X":
                quit() 
  

if __name__== "__main__":
  main()
class StudentMarks:
    def __init__(self, marks):
        """Initializes the object with a list of marks."""
        self.marks = marks

    def last_three_avg(self):
        """Calculates the average of the last three marks using negative indexing."""
        try:
            # Check if we have at least 3 marks to avoid logical errors
            if len(self.marks) < 3:
                # Manually raise an IndexError to trigger the exception block
                raise IndexError
            
            # Using negative indexing to slice the last three elements
            # marks[-3:] starts 3 elements from the end and goes to the finish
            last_three = self.marks[-3:]
            avg = sum(last_three) / 3
            print(f"Average of last 3 marks is: {avg}")
            
        except IndexError:
            print("Not enough marks to calculate average")

def main():
    """Main method to execute the student marks logic."""
    # Define the input data
    marks_list = [50, 60, 70, 80, 90]
    
    # Instantiate the class
    student = StudentMarks(marks_list)
    
    # Execute the method
    student.last_three_avg()

if __name__ == "__main__":
    main()
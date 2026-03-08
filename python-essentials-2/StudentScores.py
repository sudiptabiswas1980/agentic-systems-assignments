class StudentScores:
    def __init__(self, scores):
        """Initializes the object with a list of scores."""
        self.scores = scores

    def highest_last_two(self):
        """Finds the highest of the last two scores using negative indexing."""
        try:
            # Check if we have at least 2 scores
            if len(self.scores) < 2:
                # Raise IndexError to trigger the exception block
                raise IndexError
            
            # Using negative indexing to get the last two elements
            # self.scores[-2:] creates a slice from the second-to-last item to the end
            last_two = self.scores[-2:]
            highest = max(last_two)
            
            print(f"Highest score among last two is: {highest}")
            
        except IndexError:
            print("Not enough scores to find highest value")

def main():
    """Main method to execute the student scores logic."""
    # Example Input
    scores = [45, 67, 89, 72]
    
    # Instantiate the class
    student_obj = StudentScores(scores)
    
    # Execute the method
    student_obj.highest_last_two()

if __name__ == "__main__":
    main()
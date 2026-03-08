class StudentPerformance:
    def __init__(self, scores):
        """Initializes the object with a list of scores."""
        self.scores = scores

    def score_difference(self):
        """Calculates the difference between the last and first score."""
        try:
            # Check if the list is empty
            if not self.scores:
                # Manually raise an IndexError to trigger the exception block
                raise IndexError
            
            # Using indexing to target first (0) and last (-1) elements
            first_score = self.scores[0]
            last_score = self.scores[-1]
            
            diff = last_score - first_score
            print(f"Difference between last and first score is: {diff}")
            
        except IndexError:
            print("No scores available to calculate difference")

def main():
    """Main method to execute the performance logic."""
    # Example Input
    scores = [55, 65, 75, 85]
    
    # Instantiate and execute
    performance = StudentPerformance(scores)
    performance.score_difference()

if __name__ == "__main__":
    main()
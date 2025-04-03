# Tuple Functions in Python

def tuple_operations():
    t = (5, 2, 8, 1, 7)
    print("Original Tuple:", t)
    
    # Length of tuple
    print("Length:", len(t))
    
    # Maximum and Minimum values
    print("Max:", max(t))
    print("Min:", min(t))
    
    # Sum of tuple elements
    print("Sum:", sum(t))
    
    # Sorted tuple (returns a list)
    print("Sorted:", sorted(t))
    
    # Tuple creation from a list
    lst = [10, 20, 30]
    t2 = tuple(lst)
    print("Tuple from list:", t2)
    
    # Indexing and Slicing
    print("First element:", t[0])
    print("Slice (1:4):", t[1:4])
    
    # Count occurrences of an element
    t3 = (1, 2, 3, 2, 2, 4)
    print("Count of 2:", t3.count(2))
    
    # Find index of an element
    print("Index of 3:", t3.index(3))
    
    # Tuple concatenation and repetition
    t4 = ("a", "b")
    print("Concatenation:", t + t4)
    print("Repetition:", t4 * 3)

if __name__ == "__main__":
    tuple_operations()

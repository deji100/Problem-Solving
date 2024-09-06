from itertools import combinations_with_replacement


if __name__ == "__main__":
    n = input()
    
    """Combinations with replacement"""
    
    elements = n[:len(n) - 2]
    num = int(n[len(elements)+1:])
        
    sorted_elements = "".join(sorted(elements))

    combined_sorted_list = combinations_with_replacement(sorted_elements, num)

    for i in combined_sorted_list:
        print("".join(i))
        

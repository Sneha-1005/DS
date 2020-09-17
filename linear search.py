def search(arr, a, b): 
  
    for i in range (0, a): 
        if (arr[i] == b): 
            return i; 
    return -1; 
  
arr = [ 2, 3, 4, 10, 40 ];

b = int(input("Enter the number:")); 
a = len(arr); 
result = search(arr, a, b) 

if(result == -1): 
    print("Oops . The Number is not here.Sorry!") 
else: 
    print("Element is present at index", result); 

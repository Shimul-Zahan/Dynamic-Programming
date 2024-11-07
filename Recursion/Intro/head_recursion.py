class Tail_Recursion():
    def tail(self, n):
        # Base case
        if n == 0:
            return 0
        
        print("Call stack here", n)
        
        # make the recursive function call
        self.tail(n-1) 
        
        # Then we do any operation
        print(n, "Final Result")
    
    
sol = Tail_Recursion()   
sol.tail(5)
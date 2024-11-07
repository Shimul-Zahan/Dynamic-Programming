class Tail_Recursion():
    def tail(self, n):
        # Base case
        if n == 0:
            return 0
        
        # make the recursive function call
        self.tail(n-1) 
        
        # Then we do any operation
        print(n, "call stack")
    
    
sol = Tail_Recursion()
sol.tail(5)
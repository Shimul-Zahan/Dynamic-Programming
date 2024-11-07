class Tail_Recursion():
    def tail(self, n):
        # Base case
        if n == 0:
            return 0
        
        print(n, "call stack")
        
        # make the recursive function call
        self.tail(n-1) 
    
    
sol = Tail_Recursion()
sol.tail(5)
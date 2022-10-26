def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_ = [digit for digit in str(num1)]
    num2_ = [digit for digit in str(num2)]

    if (len(num1_) == len(num2_)):
        num1_.sort()
        num2_.sort()
        if (num1_ == num1_):
          
            return True
        else:
       
            return False

    else:
      
        return False
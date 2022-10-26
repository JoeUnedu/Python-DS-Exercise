def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    
    # let use the key and object when number is the kay and string is the value
    
    days = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4: "Wednesday"
            ,5:"Thursday", 6:"Friday", 7: "Saturday"}
    
    return days.get(day_of_week,None)

weekday_ = ""
print(f"'{weekday_}': {weekday_name(weekday_)} ")
weekday_ = 0
print(f"{weekday_}: {weekday_name(weekday_)} ")
weekday_ += 1
  
    
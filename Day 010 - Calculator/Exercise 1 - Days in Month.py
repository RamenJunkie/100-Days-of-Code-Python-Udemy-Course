def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(yyyy, mm):
  """Returns the number of days in a month."""

  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  if(mm not in range(1,12)):
    return 0
  elif(is_leap(yyyy) and mm == 2):
    return month_days[mm-1] + 1
  else:
    return month_days[mm-1]   
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
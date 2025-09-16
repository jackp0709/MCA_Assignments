from datetime import datetime 
date1 = input("Enter first date in yyyy-mm-dd format: ") 
date2 = input("Enter second date in yyyy-mm-dd format: ") 
d1 = datetime.strptime(date1, "%Y-%m-%d") 
d2 = datetime.strptime(date2, "%Y-%m-%d") 
difference = d2 - d1 
print("Difference in Dates : ",difference.days ,"days")
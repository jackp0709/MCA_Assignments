import math 
 
print("Angle   Sin       Cos       Tan") 
print("--------------------------------") 
 
angles = [0, 30, 45, 60, 90] 
 
for angle in angles: 
    rad = math.radians(angle)    
 
    sin_val = round(math.sin(rad), 3) 
    cos_val = round(math.cos(rad), 3) 
 
     
    if angle == 90: 
        tan_val = "undefined" 
    else: 
        tan_val = round(math.tan(rad), 3) 

        print(f"{angle:3}°   {sin_val:<8} {cos_val:<8} {tan_val}")
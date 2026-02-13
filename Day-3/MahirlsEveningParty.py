def partysuccessCheck(day,attendees):
    days=["SUN","MON","TUE","WED","THU","FRI","SAT"]
    if day not in days or attendees<0:
        return "Invalid Input"
    
    if day in ["FRI","SAT","SUN"]:
        if attendees>=1500:
            return "Successful"
        else:
            return "Unsuccessful"
    else:
        if 700<=attendees<=100:
            return "Successful"
        else:
            return "Unsuccessful"
   
day=input("Enter the day:").strip().upper()
attendees=int(input("Enter the number of attendees:").strip())

CheckSuccess=partysuccessCheck(day,attendees)
print(CheckSuccess)
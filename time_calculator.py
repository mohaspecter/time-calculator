def add_time(start_time, add_time, day=None):
  def next_day(day):
    if day.upper() == "MONDAY":
      day = "Tuesday"
    elif day.upper() == "TUESDAY":
      day = "Wednesday"
    elif day.upper() == "WEDNESDAY":
      day = "Thursday"
    elif day.upper() == "THURSDAY":
      day = "Friday"
    elif day.upper() == "FRIDAY":
      day = "Saturday"
    elif day.upper() == "SATURDAY":
      day = "Sunday"
    elif day.upper() == "SUNDAY":
      day = "Monday"
    return day
      
  rstart_time = start_time.split() #['11:55', 'AM'] 11:55 AM
  radd_time = add_time.split(':') #['3', '12']
  realstart_time = rstart_time[0].split(':') #['11', '55']
  current_time=[] #liste dans laquelle on rentre le res

  ampm=rstart_time[1] #'AM'
  if ampm == 'AM':
    hours=int(realstart_time[0])+(int(radd_time[0])) #11+3=14
  elif ampm == 'PM':
    hours= 12 + int(realstart_time[0])+(int(radd_time[0])) 

  minutes=int(realstart_time[1])+(int(radd_time[1])) #55+12=67
  days=0
  
  while minutes >= 60: #67
    minutes = minutes - 60 #7
    hours = hours + 1 #14+1=15
  
  while hours >= 24: #non
    days = days + 1
    hours = hours - 24

  if hours<12: 
    ampm='AM'   
  elif hours>=12:
    hours = hours % 12 #5%12 = 3
    ampm='PM' #PM
      
  if hours == 0:
    hours = 12
    #if ampm=='AM':
      #ampm='PM'
    #elif ampm=='PM':
      #ampm='AM'     
  
  
  current_time.append(str(hours)) # append 3
  
  if minutes<60:
    if minutes<10:
        current_time.append("0"+str(minutes)) #append 07
    elif minutes>=10:
        current_time.append(str(minutes))
  
  new_time=current_time[0]+':'+current_time[1]+' '+ampm # new_time = 3:07 PM

  if day is not None:
    if days==0:
      new_time = new_time + ", "+day
  
  if days==1:
    if day is None:
      new_time = new_time+(" (next day)")
    if day is not None:
      day=next_day(day)
      new_time = new_time+(", %s (next day)"%day)
  if days>1:
    if day is None:
      new_time = new_time+(" (%s days later)"%days)
    for i in range(days):
      if day is not None:
        day=next_day(day)
    if day is not None:
      new_time = new_time+(", %s (%d days later)"%(day,days))

  return new_time

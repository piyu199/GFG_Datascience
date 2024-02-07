from datetime import datetime,timedelta
import math

event_date=datetime(2024,2,15,0,0,0)
current_date=datetime.now()
difference=event_date-current_date
remaining_days=difference.days
remaining_hours,remaining_second=divmod(difference.seconds,3600)
remaining_minutes=remaining_second//60

print(f"Remaining time until the event:{remaining_days} days,{remaining_hours} hours, {remaining_second} seconds")
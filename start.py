from datetime import datetime
import pytz

def get_india_time():
    # Get timezone for India
    india_tz = pytz.timezone('Asia/Kolkata')
    
    # Get current time in India
    india_time = datetime.now(india_tz)
    
    # Format the time
    formatted_time = india_time.strftime('%I:%M:%S %p')
    
    # Write time to file
    with open('time.txt', 'w') as f:
        f.write(f"Current time in India: {formatted_time}")

# Call the function
get_india_time()
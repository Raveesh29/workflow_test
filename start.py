from datetime import datetime
import pytz

def get_india_time():
    # Get timezone for India
    india_tz = pytz.timezone('Asia/Kolkata')
    
    # Get current time in India
    india_time = datetime.now(india_tz)
    
    # Format and display the time
    print(f"Current time in India: {india_time.strftime('%I:%M:%S %p')}")

# Call the function
get_india_time()
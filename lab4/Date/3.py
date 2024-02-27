from datetime import datetime

current_datetime = datetime.now()
stripped_datetime = current_datetime.replace(microsecond=0)
print("Stripped datetime:", stripped_datetime)

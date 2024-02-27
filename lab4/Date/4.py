from datetime import datetime

date1 = datetime(2024, 2, 27, 12, 0, 0)
date2 = datetime(2024, 2, 28, 12, 0, 0)

difference_seconds = abs((date1 - date2).total_seconds())
print("Difference in seconds:", difference_seconds)

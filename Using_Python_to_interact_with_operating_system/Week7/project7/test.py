import re

pattern = r"^[a-z0-9.]{3,16}$"
line = "ahmed.miller"
print(re.search(pattern, line))
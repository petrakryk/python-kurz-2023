data = """
2.2.2022
13. 8. 1999
4/5/2001
5.123.458.91
21.4
8./9
"""

import re

reg_express = re.compile(r"\d+\.? ?/?\d+\.? ?/?\d{4}")
check = reg_express.findall(data)

print(check)


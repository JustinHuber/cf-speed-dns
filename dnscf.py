Update error handling for `get_dns_records` to return an empty list on error. Also added error handling in `main` to check the DNS records are not empty.

Modified `get_dns_records` function:
---
48|         print('Error fetching DNS records:', response.text)
49|         return [] # Ensure an empty list is returned instead of None.

Modified `main` function:
---
90|     dns_records = get_dns_records(CF_DNS_NAME)
91|     if not dns_records:
92|         print("No DNS records found for the specified name.")
93|         return # Exit the function when dns_records is empty or None.
import random
import string
instances_count = int(input("How many EC2 names would you like to create? "))
team_name = input("What is your department's name? ").strip()
print("\nYour EC2 Instance Names:")
for _ in range(instances_count):
    unique_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    instance_name = f"{team_name}-{unique_id}"
    print(instance_name)

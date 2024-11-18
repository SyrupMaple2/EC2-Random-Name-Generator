import random
import string
def generate_ec2_names():
    allowed_departments = ['Marketing', 'Accounting', 'FinOps']
    instances_count = int(input("How many EC2 names would you like to create? "))
    team_name = input("Enter your department name: ").strip().capitalize()
    if team_name not in allowed_departments:
        print(f"Error: The department '{team_name}' is not allowed to use this name generator.")
        print("Allowed departments are: Marketing, Accounting, and FinOps.")
        return
    print("\nGenerated EC2 Instance Names:")
    for _ in range(instances_count):
        unique_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        instance_name = f"{team_name}-{unique_id}"
        print(instance_name)
generate_ec2_names()
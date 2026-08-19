# Machine facts

machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

# Apply rules

for machine, status in machines.items():

    if status == "Active":
        print(machine, "-> Producing")

    elif status == "Maintenance":
        print(machine, "-> Not Producing")

# Gear production example

machine = "M3"
product = "Gear"

if machines[machine] == "Maintenance":
    print("\n", product, "production is affected")
else:
    print("\n", product, "production is active")
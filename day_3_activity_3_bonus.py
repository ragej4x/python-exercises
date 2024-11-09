def calculate_bonus(years, office):
    bonus_structure = {
        "it": { ">=10": 10000, "<10": 5000 },
        "acct": { ">=10": 12000, "<10": 6000 },
        "hr": { ">=10": 15000, "<10": 7500 },
    }
    
    if years >= 10:
        bonus = bonus_structure[office][">=10"]
    else:
        bonus = bonus_structure[office]["<10"]
    
    return bonus

years = int(input("Enter years of service: "))
office = input("Enter office (IT, acct, hr): ").lower()

if office in ["it", "acct", "hr"]:
    bonus = calculate_bonus(years, office)
    print(f"The bonus for {years} years in {office.upper()} is: {bonus}")
else:
    print("Invalid office. Please enter 'IT', 'acct', or 'hr'.")

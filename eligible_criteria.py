#Given income, credit_score, and existing_debt, determine "Eligible", "Review", or "Reject" using sensible thresholds.

income=float(input("Enter your income: "))
credit_score=int(input("Enter your credit score: "))
debt=float(input("Enter your existing debt: "))

if income>=50000 and credit_score>=750 and debt<=20000:
    print("Eligible")
elif income>=30000 and credit_score>=650 and debt<=40000:
    print("Review")
else:
    print("Reject")
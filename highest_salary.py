# From a dictionary of employee salaries, find the employee with the highest salary.
emps={"Sivani":35000,"Bharathi":75000,"Jagadish":30000,"Shizuka":80000}
max_salary=max(emps.values())
emp_name=""
for key,val in emps.items():
    if val==max_salary:
        emp_name=key
print(emp_name)
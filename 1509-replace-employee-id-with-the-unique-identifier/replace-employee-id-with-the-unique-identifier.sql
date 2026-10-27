# Write your MySQL query statement below
select u.unique_id,e.name 
from EmployeeUNI u
right outer join Employees e
on e.id=u.id
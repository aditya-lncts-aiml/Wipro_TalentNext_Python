'''
Q1) 1.	create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.'''


def travel_advice(distance):
    while distance <= 0:
       print("Distance cannot be negative or zero. Please enter a valid distance.")
       distance = float(input("Enter the distance you want to travel (in miles): "))
    if distance < 3:
       return "You should ride a Bicycle."
    elif 3 <= distance and distance< 300:
       return "You should ride a Motor-cycle."
    else:
       return "You should drive a Super-Car."

distance = float(input("Enter the distance you want to travel (in miles): "))
print(travel_advice(distance))


'''
Q2) 2.	Let's assume you are planning to use your python skills to build an App for Mobile.
You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
Write a python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How much days can I operate one server with $918?

'''

def cloud_hosting_costs(hourly_rate=0.51, budget=918):
    daily_cost = hourly_rate * 24
    weekly_cost = daily_cost * 7
    monthly_cost = daily_cost * 30
    days_with_budget = int(budget / daily_cost)
    
    print(f"Cost to operate one server per day: ${daily_cost}")
    print(f"Cost to operate one server per week: ${weekly_cost}")
    print(f"Cost to operate one server per month: ${monthly_cost}")
    print(f"You can operate one server for {days_with_budget} days with $918.") 

cloud_hosting_costs()

ls = [1,2,3,4,5,6,7,8,9]
new_ls = [l*5 for l in ls]
print(new_ls)
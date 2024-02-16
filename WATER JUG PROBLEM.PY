'''Conditions
1.
Target !=0, -ve
2.
Target<Big jar
3. target should be multiple of GCD (Big jar, Small jar)'''




"""
 
target != 0, -ve
target < Big Jar
Trget should be multipled of GCD (big jar, small jar)
 
"""
 
 
def water_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    jug1 = 0
    jug2 = 0
    steps = 0
 
    while jug1 != target_amount and jug2 != target_amount:
        if jug2 == jug2_capacity:
            jug2 = 0
        elif jug1 != 0:
            if jug1 <= jug2_capacity - jug2:
                jug1, jug2 = 0, jug1 + jug2
            else:
                jug1, jug2 = jug1 - (jug2_capacity - jug2), jug2_capacity
        else:
            jug1 = jug1_capacity
 
        steps += 1
        print(f"Step {steps}: Jug 1 = {jug1} liters, Jug 2 = {jug2} liters")
 
    return steps
 
# Example usage
jug1_capacity = 3
jug2_capacity = 5
target_amount = 4
 
print("\nSolving Water Jug Problem:")
total_steps = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)
print(f"\nTotal steps taken: {total_steps}")

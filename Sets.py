E = {0,1,2,3}
N = {0,3,4,5}

union_set = E.union(N)
print(f"Union: {union_set}")

intersection_set = E.intersection(N)
print(f"Intersection: {intersection_set}")

difference_set_EN = E.difference(N)
difference_set_NE = N.difference(E)
print(f"Difference of E and N: {difference_set_EN}")
print(f"Difference of N and E: {difference_set_NE}")

symmetric_difference_set = E.symmetric_difference(N)
print(f"Symmetric Difference: {symmetric_difference_set}")

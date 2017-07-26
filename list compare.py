from collections import defaultdict

a = ["Maths_Algebra", "Physics_Astrophysics"]

b = ["Maths_Algebra_001", "Maths_Algebra_002", "Maths_Algebra_003", "Physics_Astrophysics_001", "Physics_Astrophysics_002"]

x = defaultdict(list)

([x[i].append(j) for i in a for j in b if i in j])

print dict(x)



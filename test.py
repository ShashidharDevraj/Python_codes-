a = ["Maths_Algebra", "Physics_Astrophysics"]

b = ["Maths_Algebra_001", "Maths_Algebra_002", "Maths_Algebra_003", "Physics_Astrophysics_001", "Physics_Astrophysics_002"]


x = {}
for i in a:
    for j in b:
        c=i.split('_')
        d=j.split('_')

        if c[:] == d[0:2]:
            #print "matched:", "_".join(c),' ',"_".join(d)
      	    x["_".join(c)] = ["_".join(d)] 
            #print g
            print x 
        else:
            pass


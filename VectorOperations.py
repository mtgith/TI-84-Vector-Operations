def retrieve_vector(vector):
   final_vector = []
   updated_vector = vector.replace("(", "")
   updated_vector = updated_vector.replace(")", "")
   vec = updated_vector.split(",")
   if len(vec) != 3:
      print("Invalid Dimensions: Vector should be of form '(x,y,z)'.")
   else:
      for elem in vec:
         final_vector.append(float(elem))
      return final_vector

def magnitude(vector):
   sum = ((vector[0]**2)+(vector[1]**2)+(vector[2]**2))
   mag = sum**(1/2)
   return [sum, mag]

def dot_prod(vector1, vector2):
   dot = (vector1[0]*vector2[0])+(vector1[1]*vector2[1])+(vector1[2]*vector2[2])
   return dot

def cross_prod(vector1, vector2):
   x_comp = (vector1[1]*vector2[2])-(vector1[2]*vector2[1])
   y_comp = (vector1[2]*vector2[0])-(vector1[0]*vector2[2])
   z_comp = (vector1[0]*vector2[1])-(vector1[1]*vector2[0])
   vec = [x_comp, y_comp, z_comp]
   return vec 

def scalar_triple_prod(vector1, vector2, vector3):
   result = dot_prod(vector1, cross_prod(vector2, vector3))
   print("a•(b x c) = " + str(result))

def unit_vector(vector):
   mag = magnitude(vector)
   mag_vec = mag[1]
   if mag_vec == 0:
      print("Division by zero error.")
   else:
      final_vector = "[" + str(vector[0]/mag_vec) + " " + str(vector[1]/mag_vec) + " " + str(vector[2]/mag_vec) + "]"
      raw_vector = "1/sqrt(" + str(mag[0]) + ")[" + str(vector[0]) + " " + str(vector[1]) + " " + str(vector[2]) + "]"
      print("u = " + raw_vector + " = " + final_vector)

def projection(vec1, vec2):
   mag = magnitude(vec1)
   vec = [vec1[0]*(dot_prod(vec1, vec2)/(mag[1]**2)), vec1[1]*(dot_prod(vec1, vec2)/(mag[1]**2)), vec1[2]*(dot_prod(vec1, vec2)/(mag[1]**2))]
   final_proj = "[" + str(vec1[0]*(dot_prod(vec1, vec2)/(mag[1]**2))) + " "+ str(vec1[1]*(dot_prod(vec1, vec2)/(mag[1]**2))) + " " + str(vec1[2]*(dot_prod(vec1, vec2)/(mag[1]**2))) + "]"
   raw_proj = str(dot_prod(vec1, vec2)) + "/" + str(mag[0]) + "[" + str(vec1[0]) + " "+ str(vec1[1]) + " " + str(vec1[2]) + "]"
   return [final_proj, raw_proj, vec]

def main():
   try:
      num = int(input("Enter the number associated with the task you wish to complete: "))
      print("Enter all vectors in form '(x,y,z)'.\n")
      if num == 1:
         print("Magnitude of a: ||a||")
         a = input("Enter vector a: ")
         vec = retrieve_vector(a)
         mag_vec = magnitude(vec)
         print("||a|| = " + "sqrt(" + str(mag_vec[0]) + ") = " + str(mag_vec[1]))
      elif num == 2:
         print("Dot product of a and b: (a•b)")
         a = input("Enter vector a: ")
         vec_a = retrieve_vector(a)
         b = input("Enter vector b: ")
         vec_b = retrieve_vector(b)
         dot = dot_prod(vec_a, vec_b)
         print("a•b = " + str(dot))
      elif num == 3:
         print("Cross product of a and b: (a x b)")
         a = input("Enter vector a: ")
         vec_a = retrieve_vector(a)
         b = input("Enter vector b: ")
         vec_b = retrieve_vector(b)      
         cross = cross_prod(vec_a, vec_b)
         print("a x b = [" + str(cross[0]) + " " + str(cross[1]) + " " + str(cross[2]) + "]")
         q = int(input("Enter '1' to see the magnitude, or '2' for the unit vector: "))
         if q == 1:
            mag_vec = magnitude(cross)
            print("||a x b|| = " + "sqrt(" + str(mag_vec[0]) + ") = " + str(mag_vec[1]))
         elif q == 2:
            unit_vector(cross)
      elif num == 4:
         print("Scalar triple product of a, b, c: a•(bxc)")
         a = input("Enter vector a: ")
         vec_a = retrieve_vector(a)
         b = input("Enter vector b: ")
         vec_b = retrieve_vector(b)
         c = input("Enter vector c: ")
         vec_c = retrieve_vector(c)   
         scalar_triple_prod(vec_a, vec_b, vec_c)
      elif num == 5:
         print("Unit vector of a: u")
         a = input("Enter vector a: ")
         vec_a = retrieve_vector(a)   
         unit_vector(vec_a)  
      elif num == 6:
         print("Projection of a onto b: Proj[a, b]")
         a = input("Enter vector a: ")
         vec_a = retrieve_vector(a)
         b = input("Enter vector b: ")
         vec_b = retrieve_vector(b)
         proj = projection(vec_a, vec_b)
         print("Proj[a, b] = " + proj[1] + " = " + proj[0])
         q = int(input("Enter '1' to see the magnitude, or '2' for the unit vector: "))
         if q == 1:
            mag_vec = magnitude(proj[2])
            print("||Proj[a, b]|| = " + "sqrt(" + str(mag_vec[0]) + ") = " + str(mag_vec[1]))
         elif q == 2:
            unit_vector(proj[2])
      else:
         print("Invalid input number.")
   except:
      print("Invalid input.")

print("Vector Operations Calculator")

print("\n1: Magnitude\n2: Dot Product\n3: Cross Product\n4: Scalar Triple Product\n5: Unit Vector\n6: Projection\n")
main()
from sre_constants import JUMP
#JZIHGFEDCBA

nric = input('Enter an NRIC number: ')

# Type your code below\\

Error_Format = "NRIC format is invalid."
Error_Nric = "NRIC is invalid"
Upper_nric = nric.upper()
prefix = Upper_nric[0]
string_nric1 = "JZIHGFEDCBA"
string_nric2 = "XWUTRQPNMLK"

digits = nric[1:8]
suffix = Upper_nric[8:]

if prefix == "T" or prefix == "S" or prefix == "G" or prefix == "F":
 if digits.isdigit() == False:
  print(Error_Format)
 else:
  if len(suffix) > 1:
   print(Error_Nric)
  else:
   print("NRIC format is valid.")
   if prefix == "T":
    quotient, remainder = divmod(int(nric[1])* 2 + int(nric[2])* 7 + int(nric[3])* 6 + int(nric[4])* 5 + int(nric[5])* 4 + int(nric[6])* 3 + int(nric[7])* 2 + 4, 11)
    string_nric = "JZIHGFEDCBA"
    suffix_check = string_nric[remainder]
    if suffix == suffix_check:
     print("NRIC is valid.")
    else:
     print(Error_Format)
   else: 
     if prefix == "S":
        quotient, remainder = divmod(int(nric[1])* 2 + int(nric[2])* 7 + int(nric[3])* 6 + int(nric[4])* 5 + int(nric[5])* 4 + int(nric[6])* 3 + int(nric[7])* 2, 11)
        suffix_check1 = string_nric1[remainder]
        if suffix_check1 == suffix:
          print("NRIC is valid.")
        else:
          print(Error_Nric)
     else:
      if prefix == "G":
        quotient, remainder = divmod(int(nric[1])* 2 + int(nric[2])* 7 + int(nric[3])* 6 + int(nric[4])* 5 + int(nric[5])* 4 + int(nric[6])* 3 + int(nric[7])* 2 + 4, 11)
        suffix_check = string_nric2[remainder]
        if suffix_check == suffix:
            print("NRIC is valid.")
        else:
            print(Error_Nric)
      else:  
             if prefix == "F":
              quotient, remainder = divmod(int(nric[1])* 2 + int(nric[2])* 7 + int(nric[3])* 6 + int(nric[4])* 5 + int(nric[5])* 4 + int(nric[6])* 3 + int(nric[7])* 2 , 11)
              suffix_check = string_nric2[remainder]
              if suffix_check == suffix:
                print("NRIC is valid.")
              else:
                print(Error_Nric)
     
        
else: 
 print(Error_Nric)
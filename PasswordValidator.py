print("Password Validator")
print("Want me to check if your password is valid or not?")

Password = input("Kindly put your password: ")
Special = 0
for I in range(len(Password)):
    if(len(Password) >= 15):
        Length = 1
    else:
        if(len(Password) <= 15):
            Length = 0

Capital = 0    
for I in range(len(Password)):
    if(Password[I] >= 'A' and Password[I] <= 'Z'):
        Capital = Capital + 1

Number = 0
for I in range(len(Password)):
    if(Password[I] >= '0' and Password[I] <= '9'):
        Number = Number + 1

Special = 0
for I in range(len(Password)):
    if(Password[I] == '!' or Password[I] == '@' or Password[I] == '#' or Password[I] == '$' or Password[I] == '%' or Password[I] == '^' or Password[I] == '&' or Password[I] == '*' or Password[I] == '(' or Password[I] == ')' or Password[I] == '-' or Password[I] == '_' or Password[I] == '=' or Password[I] == '+' or Password[I] == '<' or Password[I] == '>' or Password[I] == ',' or Password[I] == '.' or Password[I] == '/' or Password[I] == '[' or Password[I] == '{' or Password[I] == '}' or Password[I] == ']' or Password[I] == ';' or Password[I] == ':' or Password[I] == "'" or Password[I] == '"' or Password[I] == '.' or Password[I] == ',' or Password[I] == '?' ):
        Special = Special + 1
  
if Length == 1 and Capital >=1 and Number >= 1 and Special >= 1:
    print("Valid Password!")
else:
    if Length == 0 and Capital != 1 and Number != 1 and Special != 1:
        print("Invalid Password!")
        print("Your password must have:")
        print("a. Have greater than 15 characters")
        print("b. Have at least one capital letter")
        print("c. Have at least one number")
        print("d. Have at least one special char (!@#$%^&*()_+ etc)")
    else:
        if Length == 0 and Capital >=1 and Number >= 1 and Special >= 1:
            print("Invalid Password!")
            print("Your password must have:")
            print("a. Have greater than 15 characters")
            print("b. Have at least one capital letter")
            print("c. Have at least one number")
            print("d. Have at least one special char (!@#$%^&*()_+ etc)")
        else:
            if Length == 1 and Capital !=1 and Number != 1 and Special != 1:
                print("Invalid Password!")
                print("Your password must have:")
                print("a. Have greater than 15 characters")
                print("b. Have at least one capital letter")
                print("c. Have at least one number")
                print("d. Have at least one special char (!@#$%^&*()_+ etc)")
            else:
                if Length == 0 and Capital !=1 and Number >= 1 and Special >= 1:
                    print("Invalid Password!")
                    print("Your password must have:")
                    print("a. Have greater than 15 characters")
                    print("b. Have at least one capital letter")
                    print("c. Have at least one number")
                    print("d. Have at least one special char (!@#$%^&*()_+ etc)")
                else:
                    if Length == 1 and Capital >=1 and Number != 1 and Special != 1:
                        print("Invalid Password!")
                        print("Your password must have:")
                        print("a. Have greater than 15 characters")
                        print("b. Have at least one capital letter")
                        print("c. Have at least one number")
                        print("d. Have at least one special char (!@#$%^&*()_+ etc)")
                    else:
                        if Length == 1 and Capital !=1 and Number >= 1 and Special != 1:
                            print("Invalid Password!")
                            print("Your password must have:")
                            print("a. Have greater than 15 characters")
                            print("b. Have at least one capital letter")
                            print("c. Have at least one number")
                            print("d. Have at least one special char (!@#$%^&*()_+ etc)")
                        else:
                            if Length == 0 and Capital >=1 and Number != 1 and Special >= 1:
                                print("Invalid Password!")
                                print("Your password must have:")
                                print("a. Have greater than 15 characters")
                                print("b. Have at least one capital letter")
                                print("c. Have at least one number")
                                print("d. Have at least one special char (!@#$%^&*()_+ etc)")
                            else:
                                if Length == 0 and Capital !=1 and Number != 1 and Special >= 1:
                                    print("Invalid Password!")
                                    print("Your password must have:")
                                    print("a. Have greater than 15 characters")
                                    print("b. Have at least one capital letter")
                                    print("c. Have at least one number")
                                    print("d. Have at least one special char (!@#$%^&*()_+ etc)")
                                else:
                                    if Length == 0 and Capital !=1 and Number >= 1 and Special != 1:
                                        print("Invalid Password!")
                                        print("Your password must have:")
                                        print("a. Have greater than 15 characters")
                                        print("b. Have at least one capital letter")
                                        print("c. Have at least one number")
                                        print("d. Have at least one special char (!@#$%^&*()_+ etc)")
                                    else:
                                        if Length == 0 and Capital >=1 and Number != 1 and Special != 1:
                                            print("Invalid Password!")
                                            print("Your password must have:")
                                            print("a. Have greater than 15 characters")
                                            print("b. Have at least one capital letter")
                                            print("c. Have at least one number")
                                            print("d. Have at least one special char (!@#$%^&*()_+ etc)")
                                        else:
                                            if Length == 1 and Capital !=1 and Number != 1 and Special != 1:
                                                print("Invalid Password!")
                                                print("Your password must have:")
                                                print("a. Have greater than 15 characters")
                                                print("b. Have at least one capital letter")
                                                print("c. Have at least one number")
                                                print("d. Have at least one special char (!@#$%^&*()_+ etc)")
                                            else:
                                                if Length == 1 and Capital >=1 and Number >= 1 and Special != 1:
                                                    print("Invalid Password!")
                                                    print("Your password must have:")
                                                    print("a. Have greater than 15 characters")
                                                    print("b. Have at least one capital letter")
                                                    print("c. Have at least one number")
                                                    print("d. Have at least one special char (!@#$%^&*()_+ etc)")
                                                else:
                                                    if Length == 1 and Capital >=1 and Number != 1 and Special >= 1:
                                                        print("Invalid Password!")
                                                        print("Your password must have:")
                                                        print("a. Have greater than 15 characters")
                                                        print("b. Have at least one capital letter")
                                                        print("c. Have at least one number")
                                                        print("d. Have at least one special char (!@#$%^&*()_+ etc)")
                                                    else:
                                                        if Length == 1 and Capital !=1 and Number >= 1 and Special >= 1:
                                                            print("Invalid Password!")
                                                            print("Your password must have:")
                                                            print("a. Have greater than 15 characters")
                                                            print("b. Have at least one capital letter")
                                                            print("c. Have at least one number")
                                                            print("d. Have at least one special char (!@#$%^&*()_+ etc)")
                                                        else:
                                                            if Length == 0 and Capital >=1 and Number >= 1 and Special != 1:
                                                                print("Invalid Password!")
                                                                print("Your password must have:")
                                                                print("a. Have greater than 15 characters")
                                                                print("b. Have at least one capital letter")
                                                                print("c. Have at least one number")
                                                                print("d. Have at least one special char (!@#$%^&*()_+ etc)")
                                                            else:
                                                                if Length == 1 and Capital !=1 and Number != 1 and Special >= 1:
                                                                    print("Invalid Password!")
                                                                    print("Your password must have:")
                                                                    print("a. Have greater than 15 characters")
                                                                    print("b. Have at least one capital letter")
                                                                    print("c. Have at least one number")
                                                                    print("d. Have at least one special char (!@#$%^&*()_+ etc)")
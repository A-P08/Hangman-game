list1=["H_t",'c_t',"r_d",'p_rk']
list2=["o","a",'e','a']
list3=list(zip(list1,list2))
while True:
          print(""" 
1.for start game 
2.for exit game""")
          choice=int(input("enter your choice: "))
          if choice == 1:
                 right_count=0
                 wrong_count=0
                 print("for each question you have three attempts")
                 for x,y in enumerate(list3):
                     print(f"\n{x+1}. '{y[0]}' :")
                     for a in range(0,3):
                      z=input("your answer player1: ").strip().lower()
                      if z==y[1] :
                        print(f"Right guess! The word is '{y[0].replace('_', y[1])}'")
                        right_count+=1
                        break
                      else:
                           print("wrong guess")
                     else:
                       print("all attempts over and you guess wrong")
                       print(f"The correct answer was: '{y[1]}'")
                       wrong_count+=1
                 print(f"correct = {right_count} \n wrong ={wrong_count}")
          elif choice==2:
               print("thank you ")
               break
          else:
               print("invalid choice")
import turtle

#### BOARD DESIGN START ########
tim = turtle.Turtle()
tim.color('black')
tim.shape('turtle')
tim.speed(100)

for num in range(1, 6):
    tim.forward(100)
    tim.circle(radius=5)
    tim.right(72)
    
    

for num in range(1, 6):
    tim.left(72)
    tim.forward(161.8)
    tim.circle(radius=5)
    
    tim.right(144)
    tim.forward(161.8)
    

#### BOARD DESIGN ENDS ########
crows = []

star_points_arr = [[-3.0,1.0],[48.0,156.0],[100.0,8.0],[260.0,5.0],[136.0,-95.0],[186.0,-250.0],[54.0,-159.0],[-77.0,-252.0],[-36.0,-100.0],[-164.0,-5.0]]
##coordinates found by: turtle.onscreenclick(getcoor) and then noting the coordinates


def get_coor(x, y):
    print(x, y)

tt1 =  turtle.Turtle()
tt1.color('white')
tt1.shape('circle')
tt1.penup()
tt1.goto((-3.0,1.0))


tt2 =  turtle.Turtle()
tt2.color('white' )
tt2.shape('circle')
tt2.penup()
tt2.goto((48.0,156.0))


tt3 =  turtle.Turtle()
tt3.color('white')
tt3.shape('circle')
tt3.penup()
tt3.goto((100.0,8.0))


tt4 =  turtle.Turtle()
tt4.color('white')
tt4.shape('circle')
tt4.penup()
tt4.goto((260.0,5.0))


tt5 =  turtle.Turtle()
tt5.color('white')
tt5.shape('circle')
tt5.penup()
tt5.goto((136.0,-95.0))


tt6 =  turtle.Turtle()
tt6.color('white')
tt6.shape('circle')
tt6.penup()
tt6.goto((186.0,-250.0))


tt7 =  turtle.Turtle()
tt7.color('white')
tt7.shape('circle')
tt7.penup()
tt7.goto((54.0,-159.0))


tt8 =  turtle.Turtle()
tt8.color('white' )
tt8.shape('circle')
tt8.penup()
tt8.goto((-77.0,-252.0))


tt9 =  turtle.Turtle()
tt9.color('white')
tt9.shape('circle')
tt9.penup()
tt9.goto((-36.0,-100.0))


tt10 =  turtle.Turtle()
tt10.color('white' )
tt10.shape('circle')
tt10.penup()
tt10.goto((-164.0,-5.0))

tim.goto(tt1.xcor(),tt1.ycor())
turtles = []
turtles.append(tt1)
turtles.append(tt2)
turtles.append(tt3)
turtles.append(tt4)
turtles.append(tt5)
turtles.append(tt6)
turtles.append(tt7)
turtles.append(tt8)
turtles.append(tt9)
turtles.append(tt10)

class Vulture(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.penup()
        self.shape('square')

    def move(self, x, y):
        self.goto(x,y)        

class Crow(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.penup()
        self.shape('circle')

    def move(self, x, y):
        self.goto(x,y)

run = True
vu = Vulture()
vu.hideturtle()
current_player = 0
ct = 0
captured = 0
turn = 0
while run:
    player = [0,1]    
    print("Welcome to the Game!")
    # print("Available Points: ",visible)
    print("Captured  Crows: ",captured)
    if(current_player==0):
        print("It is Crow's Turn!")
    elif(current_player==1):
        print("It is Vulture's Turn!")

        
    if(current_player ==0):
        #crow
        
        if(ct<7):
            x = int(input("Enter the point where you wish to place your crow:"))
            cr  = Crow()
            crows.append(cr)
            ct+=1
            if(x==0):
                cr.move(tt1.xcor(),tt1.ycor())
            elif(x==1):
                cr.move(tt2.xcor(),tt2.ycor())
            elif(x==2):
                cr.move(tt3.xcor(),tt3.ycor())
            elif(x==3):
                cr.move(tt4.xcor(),tt4.ycor())
            elif(x==4):
                cr.move(tt5.xcor(),tt5.ycor())
            elif(x==5):
                cr.move(tt6.xcor(),tt6.ycor())
            elif(x==6):
                cr.move(tt7.xcor(),tt7.ycor())
            elif(x==7):
                cr.move(tt8.xcor(),tt8.ycor())
            elif(x==8):
                cr.move(tt9.xcor(),tt9.ycor())
            elif(x==9):
                cr.move(tt10.xcor(),tt10.ycor())
            else:
                print("Invalid input!!")
        elif(ct==7):
            ip1 = int(input("Enter the position of the crow you wish to move: "))
            if(ip1==0):
             for item in crows:
                    if item.xcor() == tt1.xcor() and item.ycor() == tt1.ycor():
                           ip2 = int(input("Enter the final location of the crow:"))
                           if(ip2==0):
                                item.move(tt1.xcor(),tt1.ycor())
                                break
                           elif(ip2==1):
                                item.move(tt2.xcor(),tt2.ycor())
                                break
                           elif(ip2==2):
                                item.move(tt3.xcor(),tt3.ycor())
                                break
                           elif(ip2==3):
                                item.move(tt4.xcor(),tt4.ycor())
                                break
                           elif(ip2==4):
                                item.move(tt5.xcor(),tt5.ycor())
                                break
                           elif(ip2==5):
                                item.move(tt6.xcor(),tt6.ycor())
                                break
                           elif(ip2==6):
                                item.move(tt7.xcor(),tt7.ycor())
                                break
                           elif(ip2==7):
                                item.move(tt8.xcor(),tt8.ycor())
                                break
                           elif(ip2==8):
                                item.move(tt9.xcor(),tt9.ycor())
                                break
                           elif(ip2==9):
                                item.move(tt10.xcor(),tt10.ycor())
                                break
                           else:
                               print("Invalid input!!")
                               break
            elif(ip1==1):
             for item in crows:
                    if item.xcor() == tt2.xcor() and item.ycor() == tt2.ycor():
                           ip2 = int(input("Enter the final location of the crow:"))
                           if(ip2==0):
                                item.move(tt1.xcor(),tt1.ycor())
                                break
                           elif(ip2==1):
                                item.move(tt2.xcor(),tt2.ycor())
                                break
                           elif(ip2==2):
                                item.move(tt3.xcor(),tt3.ycor())
                                break
                           elif(ip2==3):
                                item.move(tt4.xcor(),tt4.ycor())
                                break
                           elif(ip2==4):
                                item.move(tt5.xcor(),tt5.ycor())
                                break
                           elif(ip2==5):
                                item.move(tt6.xcor(),tt6.ycor())
                                break
                           elif(ip2==6):
                                item.move(tt7.xcor(),tt7.ycor())
                                break
                           elif(ip2==7):
                                item.move(tt8.xcor(),tt8.ycor())
                                break
                           elif(ip2==8):
                                item.move(tt9.xcor(),tt9.ycor())
                                break
                           elif(ip2==9):
                                item.move(tt10.xcor(),tt10.ycor())
                                break
                           else:
                               print("Invalid input!!")
                               break
            elif(ip1==2):
             for item in crows:
                    if item.xcor() == tt3.xcor() and item.ycor() == tt3.ycor():
                           ip2 = int(input("Enter the final location of the crow:"))
                           if(ip2==0):
                                item.move(tt1.xcor(),tt1.ycor())
                                break
                           elif(ip2==1):
                                item.move(tt2.xcor(),tt2.ycor())
                                break
                           elif(ip2==2):
                                item.move(tt3.xcor(),tt3.ycor())
                                break
                           elif(ip2==3):
                                item.move(tt4.xcor(),tt4.ycor())
                                break
                           elif(ip2==4):
                                item.move(tt5.xcor(),tt5.ycor())
                                break
                           elif(ip2==5):
                                item.move(tt6.xcor(),tt6.ycor())
                                break
                           elif(ip2==6):
                                item.move(tt7.xcor(),tt7.ycor())
                                break
                           elif(ip2==7):
                                item.move(tt8.xcor(),tt8.ycor())
                                break
                           elif(ip2==8):
                                item.move(tt9.xcor(),tt9.ycor())
                                break
                           elif(ip2==9):
                                item.move(tt10.xcor(),tt10.ycor())
                                break
                           else:
                               print("Invalid input!!")
                               break
            elif(ip1==3):
             for item in crows:
                    if item.xcor() == tt4.xcor() and item.ycor() == tt4.ycor():
                           ip2 = int(input("Enter the final location of the crow:"))
                           if(ip2==0):
                                item.move(tt1.xcor(),tt1.ycor())
                                break
                           elif(ip2==1):
                                item.move(tt2.xcor(),tt2.ycor())
                                break
                           elif(ip2==2):
                                item.move(tt3.xcor(),tt3.ycor())
                                break
                           elif(ip2==3):
                                item.move(tt4.xcor(),tt4.ycor())
                                break
                           elif(ip2==4):
                                item.move(tt5.xcor(),tt5.ycor())
                                break
                           elif(ip2==5):
                                item.move(tt6.xcor(),tt6.ycor())
                                break
                           elif(ip2==6):
                                item.move(tt7.xcor(),tt7.ycor())
                                break
                           elif(ip2==7):
                                item.move(tt8.xcor(),tt8.ycor())
                                break
                           elif(ip2==8):
                                item.move(tt9.xcor(),tt9.ycor())
                                break
                           elif(ip2==9):
                                item.move(tt10.xcor(),tt10.ycor())
                                break
                           else:
                               print("Invalid input!!")
                               break                     
            elif(ip1==4):
             for item in crows:
                    if item.xcor() == tt5.xcor() and item.ycor() == tt5.ycor():
                           ip2 = int(input("Enter the final location of the crow:"))
                           if(ip2==0):
                                item.move(tt1.xcor(),tt1.ycor())
                                break
                           elif(ip2==1):
                                item.move(tt2.xcor(),tt2.ycor())
                                break
                           elif(ip2==2):
                                item.move(tt3.xcor(),tt3.ycor())
                                break
                           elif(ip2==3):
                                item.move(tt4.xcor(),tt4.ycor())
                                break
                           elif(ip2==4):
                                item.move(tt5.xcor(),tt5.ycor())
                                break
                           elif(ip2==5):
                                item.move(tt6.xcor(),tt6.ycor())
                                break
                           elif(ip2==6):
                                item.move(tt7.xcor(),tt7.ycor())
                                break
                           elif(ip2==7):
                                item.move(tt8.xcor(),tt8.ycor())
                                break
                           elif(ip2==8):
                                item.move(tt9.xcor(),tt9.ycor())
                                break
                           elif(ip2==9):
                                item.move(tt10.xcor(),tt10.ycor())
                                break
                           else:
                               print("Invalid input!!")
                               break
            elif(ip1==5):
             for item in crows:
                    if item.xcor() == tt6.xcor() and item.ycor() == tt6.ycor():
                           ip2 = int(input("Enter the final location of the crow:"))
                           if(ip2==0):
                                item.move(tt1.xcor(),tt1.ycor())
                                break
                           elif(ip2==1):
                                item.move(tt2.xcor(),tt2.ycor())
                                break
                           elif(ip2==2):
                                item.move(tt3.xcor(),tt3.ycor())
                                break
                           elif(ip2==3):
                                item.move(tt4.xcor(),tt4.ycor())
                                break
                           elif(ip2==4):
                                item.move(tt5.xcor(),tt5.ycor())
                                break
                           elif(ip2==5):
                                item.move(tt6.xcor(),tt6.ycor())
                                break
                           elif(ip2==6):
                                item.move(tt7.xcor(),tt7.ycor())
                                break
                           elif(ip2==7):
                                item.move(tt8.xcor(),tt8.ycor())
                                break
                           elif(ip2==8):
                                item.move(tt9.xcor(),tt9.ycor())
                                break
                           elif(ip2==9):
                                item.move(tt10.xcor(),tt10.ycor())
                                break
                           else:
                               print("Invalid input!!")
                               break
            elif(ip1==6):
             for item in crows:
                    if item.xcor() == tt7.xcor() and item.ycor() == tt7.ycor():
                           ip2 = int(input("Enter the final location of the crow:"))
                           if(ip2==0):
                                item.move(tt1.xcor(),tt1.ycor())
                                break
                           elif(ip2==1):
                                item.move(tt2.xcor(),tt2.ycor())
                                break
                           elif(ip2==2):
                                item.move(tt3.xcor(),tt3.ycor())
                                break
                           elif(ip2==3):
                                item.move(tt4.xcor(),tt4.ycor())
                                break
                           elif(ip2==4):
                                item.move(tt5.xcor(),tt5.ycor())
                                break
                           elif(ip2==5):
                                item.move(tt6.xcor(),tt6.ycor())
                                break
                           elif(ip2==6):
                                item.move(tt7.xcor(),tt7.ycor())
                                break
                           elif(ip2==7):
                                item.move(tt8.xcor(),tt8.ycor())
                                break
                           elif(ip2==8):
                                item.move(tt9.xcor(),tt9.ycor())
                                break
                           elif(ip2==9):
                                item.move(tt10.xcor(),tt10.ycor())
                                break
                           else:
                               print("Invalid input!!")
                               break
            elif(ip1==7):
             for item in crows:
                    if item.xcor() == tt8.xcor() and item.ycor() == tt8.ycor():
                           ip2 = int(input("Enter the final location of the crow:"))
                           if(ip2==0):
                                item.move(tt1.xcor(),tt1.ycor())
                                break
                           elif(ip2==1):
                                item.move(tt2.xcor(),tt2.ycor())
                                break
                           elif(ip2==2):
                                item.move(tt3.xcor(),tt3.ycor())
                                break
                           elif(ip2==3):
                                item.move(tt4.xcor(),tt4.ycor())
                                break
                           elif(ip2==4):
                                item.move(tt5.xcor(),tt5.ycor())
                                break
                           elif(ip2==5):
                                item.move(tt6.xcor(),tt6.ycor())
                                break
                           elif(ip2==6):
                                item.move(tt7.xcor(),tt7.ycor())
                                break
                           elif(ip2==7):
                                item.move(tt8.xcor(),tt8.ycor())
                                break
                           elif(ip2==8):
                                item.move(tt9.xcor(),tt9.ycor())
                                break
                           elif(ip2==9):
                                item.move(tt10.xcor(),tt10.ycor())
                                break
                           else:
                               print("Invalid input!!")
                               break
            elif(ip1==8):
             for item in crows:
                    if item.xcor() == tt9.xcor() and item.ycor() == tt9.ycor():
                           ip2 = int(input("Enter the final location of the crow:"))
                           if(ip2==0):
                                item.move(tt1.xcor(),tt1.ycor())
                                break
                           elif(ip2==1):
                                item.move(tt2.xcor(),tt2.ycor())
                                break
                           elif(ip2==2):
                                item.move(tt3.xcor(),tt3.ycor())
                                break
                           elif(ip2==3):
                                item.move(tt4.xcor(),tt4.ycor())
                                break
                           elif(ip2==4):
                                item.move(tt5.xcor(),tt5.ycor())
                                break
                           elif(ip2==5):
                                item.move(tt6.xcor(),tt6.ycor())
                                break
                           elif(ip2==6):
                                item.move(tt7.xcor(),tt7.ycor())
                                break
                           elif(ip2==7):
                                item.move(tt8.xcor(),tt8.ycor())
                                break
                           elif(ip2==8):
                                item.move(tt9.xcor(),tt9.ycor())
                                break
                           elif(ip2==9):
                                item.move(tt10.xcor(),tt10.ycor())
                                break
                           else:
                               print("Invalid input!!")
                               break
            elif(ip1==9):
             for item in crows:
                    if item.xcor() == tt10.xcor() and item.ycor() == tt10.ycor():
                           ip2 = int(input("Enter the final location of the crow:"))
                           if(ip2==0):
                                item.move(tt1.xcor(),tt1.ycor())
                                break
                           elif(ip2==1):
                                item.move(tt2.xcor(),tt2.ycor())
                                break
                           elif(ip2==2):
                                item.move(tt3.xcor(),tt3.ycor())
                                break
                           elif(ip2==3):
                                item.move(tt4.xcor(),tt4.ycor())
                                break
                           elif(ip2==4):
                                item.move(tt5.xcor(),tt5.ycor())
                                break
                           elif(ip2==5):
                                item.move(tt6.xcor(),tt6.ycor())
                                break
                           elif(ip2==6):
                                item.move(tt7.xcor(),tt7.ycor())
                                break
                           elif(ip2==7):
                                item.move(tt8.xcor(),tt8.ycor())
                                break
                           elif(ip2==8):
                                item.move(tt9.xcor(),tt9.ycor())
                                break
                           elif(ip2==9):
                                item.move(tt10.xcor(),tt10.ycor())
                                break
                           else:
                               print("Invalid input!!")
                               break                          
       
                                
              

    elif(current_player==1):
        #vulture
     #    vu.showturtle()
        aan,bha = vu.xcor(),vu.ycor()
        ps1 = 0
        for item in turtles:
          if item.xcor() == aan and item.ycor() == bha:
              ps1 = turtles.index(item)
              break
        x = int(input("Enter the position where the vulture is:"))
        vu.showturtle()
        if turn >=0.5:
         if(ps1%2!=0):
           if(x==(ps1+3)%10):
             ab = (ps1+1)%10
             xp,yp = turtles[ab].xcor(),turtles[ab].ycor()
             for item in crows:
                  if item.xcor() == xp and item.ycor() ==yp:
                       captured+=1
                       item.hideturtle()
                       crows.remove(item)
                       break
             if captured ==4:
                  print("4 crows have been captured! Player 2 wins!")
                  run  = False
                  
           if(x == (ps1-3)%10):
             ab = (ps1-1)%10
             xp,yp = turtles[ab].xcor(),turtles[ab].ycor()
             for item in crows:
                  if item.xcor() == xp and item.ycor() ==yp:
                       captured+=1
                       item.hideturtle()
                       crows.remove(item)
                       break
             if captured ==4:
                  print("4 crows have been captured! Player 2 wins!")
                  run  = False
                  
         elif(ps%2==0):
              if(x==(ps1+3)%10):
               ab = (ps+2)%10
               xp,yp = turtles[ab].xcor(),turtles[ab].ycor()
               for item in crows:
                  if item.xcor() == xp and item.ycor() ==yp:
                       captured+=1
                       item.hideturtle()
                       crows.remove(item)
                       break
               if captured ==4:
                  print("4 crows have been captured! Player 2 wins!")
                  run  = False
                  
              if(x == (ps1-3)%10):
               ab = (ps-2)%10
               xp,yp = turtles[ab].xcor(),turtles[ab].ycor()
               for item in crows:
                  if item.xcor() == xp and item.ycor() ==yp:
                       captured+=1
                       item.hideturtle()
                       crows.remove(item)
                       break
               if captured ==4:
                  print("4 crows have been captured! Player 2 wins!")
                  run  = False
                  
              
        if(x==0):
                vu.move(tt1.xcor(),tt1.ycor())
        elif(x==1):
                vu.move(tt2.xcor(),tt2.ycor())
        elif(x==2):
                vu.move(tt3.xcor(),tt3.ycor())
        elif(x==3):
                vu.move(tt4.xcor(),tt4.ycor())
        elif(x==4):
                vu.move(tt5.xcor(),tt5.ycor())
        elif(x==5):
                vu.move(tt6.xcor(),tt6.ycor())
        elif(x==6):
                vu.move(tt7.xcor(),tt7.ycor())
        elif(x==7):
                vu.move(tt8.xcor(),tt8.ycor())
        elif(x==8):
                vu.move(tt9.xcor(),tt9.ycor())
        elif(x==9):
                vu.move(tt10.xcor(),tt10.ycor())
        else:
                print("Invalid input!!")
     
    x_o, y_o = vu.xcor(),vu.ycor()
    ps = 0
    for item in turtles:
         if item.xcor() == x_o and item.ycor() == y_o:
              ps = turtles.index(item)
              break
    if(ps%2==0):
         n1 = (ps+1)%10
         n2 = (ps+2)%10
         n3 = (ps-1)%10
         n4 = (ps-2)%10
         n5 = (ps+3)%10
         n6 = (ps-3)%10
         t1 = turtles[n1]
         t2 = turtles[n2]
         t3 = turtles[n3]
         t4 = turtles[n4]
         t5 = turtles[n5]
         t6 = turtles[n6]
         b1 = False
         b2 = False
         b3 = False
         b4 = False
         b5 = False
         b6 = False
         for item in crows:
              if item.xcor()==t1.xcor() and item.ycor() == t1.ycor():
                   b1 = True
                   break
         for item in crows:
              if item.xcor() == t2.xcor() and item.ycor() ==t2.ycor():
                   b2 = True
                   break
         for item in crows:
              if item.xcor() == t3.xcor() and item.ycor() == t3.ycor():
                   b3 = True
                   break
         for item in crows:
              if item.xcor() == t4.xcor() and item.ycor() == t4.ycor():
                   b4 = True
                   break
         for item in crows:
              if item.xcor() == t5.xcor() and item.ycor() == t5.ycor():
                   b5 = True
                   break
         for item in crows:
              if item.xcor() == t6.xcor() and item.ycor() == t6.ycor():
                   b6 = True
                   break
         if(b1 and b2 and b3 and b4 and b5 and b6):
              print("Vulture blocked! Player 1 wins the Game!")
              run = False
              break
    elif(ps%2!=0):
         n1 = (ps+1)%10
         n2 = (ps+3)%10
         n3 = (ps-1)%10
         n4 = (ps-3)%10
         t1 = turtles[n1]
         t2 = turtles[n2]
         t3 = turtles[n3]
         t4 = turtles[n4]
         b1 = False
         b2 = False
         b3 = False
         b4 = False
         for item in crows:
              if item.xcor()==t1.xcor() and item.ycor() == t1.ycor():
                   b1 = True
                   break
         for item in crows:
              if item.xcor() == t2.xcor() and item.ycor() == t2.ycor():
                   b2 = True
                   break
         for item in crows:
              if item.xcor() == t3.xcor() and item.ycor() == t3.ycor():
                   b3 = True
                   break
         for item in crows:
              if item.xcor() == t4.xcor() and item.ycor() == t4.ycor():
                   b4 = True
                   break
         if(b1 and b2 and b3 and b4):
              print("Vulture blocked! Player 1 wins the Game!")
              run = False
              break

                   
     
    current_player = (current_player+1)%2
    turn+=0.25

    
turtle.done()

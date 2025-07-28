##def odd_or_even(num):
    ##return num % 2
##
##my_num = int(input("Please provide an integer: "))
##if odd_or_even(my_num) == 0:
    ##print(f"Your number {my_num} is even.")
##else:
    ##print(f"Your number {my_num} is odd.")
#
#print("Welcome to the Python Pizza Ordering System")
#print("Small pizza (S): $15\nMedium pizza (M): $20\nLarge pizza (L): $25")
#size = input("What size pizza do you want (S,M,L): ")
#pepperoni_cost = 0
#size_selected = ""
#
#if size == "S":
    #pizza_cost = 15
    #pepperoni_cost = 2
    #size_selected = "small"
#elif size == "M":
    #pizza_cost = 20
    #pepperoni_cost = 3
    #size_selected = "medium"
#else:
    #pizza_cost = 25
    #pepperoni_cost = 3
    #size_selected = "large"
#
#
#
#add_pepperoni = input(f"Would you like to add pepperoni to your {size_selected} pizza (Y or N): +${pepperoni_cost}")
#if add_pepperoni == "Y":
    #pizza_cost += pepperoni_cost
#add_cheese = input(f"Would you like to add extra cheese to your {size_selected} pizza (Y or N): +$1")
#if add_cheese == "Y":
    #pizza_cost += 1
#print(f"Your final bill is ${pizza_cost}")

def print_eagle():
    print('''
                                   /T /I
                              / |/ | .-~/
                          T\ Y  I  |/  /  _
         /T               | \I  |  I  Y.-~/
        I l   /I       T\ |  |  l  |  T  /
     T\ |  \ Y l  /T   | \I  l   \ `  l Y
 __  | \l   \l  \I l __l  l   \   `  _. |
 \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |
  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./
 >--.  ~-.   ._  ~>-"    "\\   7   7   ]
^.___~"--._    ~-{  .-~ .  `\ Y . /    |
 <__ ~"-.  ~       /_/   \   \I  Y   : |
   ^-.__           ~(_/   \   >._:   | l______
       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.
              (_/ .  ~(   /'     "~"--,Y   -=b-. _)
               (_/ .  \  :           / l      c"~o \
                \ /    `.    .     .^   \_.-~"~--.  )
                 (_/ .   `  /     /       !       )/
                  / / _.   '.   .':      /        '
                  ~(_/ .   /    _  `  .-<_
                    /_/ . ' .-~" `.  / \  \          ,z=.
                    ~( /   '  :   | K   "-.~-.______//
                      "-,.    l   I/ \_    __{--->._(==.
                       //(     \  <    ~"~"     //
                      /' /\     \  \     ,v=.  ((
                    .^. / /\     "  }__ //===-  `
                   / / ' '  "-.,__ {---(==-
                 .^ '       :  T  ~"   ll
                / .  .  . : | :!        \\
               (_/  /   | | j-"          ~^
                 ~-<_(_.^-~"''')

def print_tiger():
    print('''
                            __,,,,_
          _ __..-;''`--/'/ /.',-`-.
      (`/' ` |  \ \ \\ / / / / .-'/`,_
     /'`\ \   |  \ | \| // // / -.,/_,'-,
    /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')
   /  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\'
   `-`  f/ ;      / __/ \__ `/ |__/ |
        `-'      |  -| =|\_  \  |-' |
              __/   /_..-' `  ),'  //
             ((__.-'((___..-'' \__.'
    ''')

def print_crocodile():
    print('''
                         _.---._     .---.
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
             ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
    ''')

def print_bees():
    print('''
                                    _.-~7
      .                      ,-"   /
      \\                   .^     / _.-~7
       \\                 /      /-"   /
        \\               /\.  _.^     /
 ________\\          .--" _>-"/      /
`--------\"\  ___   / .-~"_~"/l  _.-^-.
          \.\" _/7-{ / /'~ ~/_.-"--._ /
          /_.-~ \|~~Y Y   _// "~-.   ~
         <"_ __'_I__I |  (_/     \\
          \_/_.~ j I~-'           )Y
            ">-'Y\//\     _.     ( j__
            /7--l //"\j|_/// ._  _7   ~"-.
           //    "/,^. | 7/--||-~__)      \
         .//     // //"'//   l`"~_ Y     .-Y
         3/    .//_//  //     ~7` ||--._/  |
               3/ L/ _//      /` /||       !
                     L/      /` / !j      /
                     i      /` / //      /
                     l\    /` '_//     .^   
                      \"--"`   L/  _.-~     
                       "-.____.--"~

    ''')

def print_door():
    print('''
      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |______________|
    ''')

winner = 0
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
print("You come to a fork in the road")
direction = input("Which direction do you go? (L for Left, R for Right): ")
if direction == "R":
    print("You've come to a lake.")
    direction = input("Do you swim across (S) or wait for the boat (W): ")
    if direction == "S":
        print("You were eaten by a crocodile and died.")
        print_crocodile()
    elif direction == "W":
        print("You've come to 3 doors.")
        direction = input("Which door do you choose (B for Blue, R for Red, P for Purple): ")
        if direction == "R" or direction == "B":
            print("You picked the wrong door and were sucked into a void and died")
            print_door()
        elif direction == "P":
            print("You found the treasure!")
            winner = 1
        else:
            print("You picked an invalid door and was grabbed by a giant eagle and fed to its babies.")
            print_eagle()
    else:
        print("You picked an invalid option and died by quicksand")
elif direction == "L":
    print("You came across a tiger and he ate you")
    print_tiger()
else:
    print("You picked an invalid direction and were killed by a swarm of bees")
    print_bees()

if winner == 1:
    print("Congratulations! You survived the treasure hunt.")
elif winner == 0:
    print("I'm sorry. You did not survive.")


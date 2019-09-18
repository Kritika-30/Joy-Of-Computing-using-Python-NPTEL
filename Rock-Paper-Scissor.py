''' In this game each player is entering a string of number and secret digit. Therefore other player doesn't know what has been chosen. Then 
we calculate the digit at the secret bit in string. As per th chosen value winner is declared.'''

def rock_paper_scissor(num1,num2,bit_one,bit_two):
    p1=int(num1[bit_one])%3
    p2=int(num2[bit_two])%3
    
    if(player_one[p1] == player_two[p2]):
        print('Draw')
    elif(player_one[p1]=='Rock' and player_two[p2]=='Scissor'):
        print("Player one wins")
    elif(player_one[p1]=='Rock' and player_two[p2]=='Paper'):
        print("Player two wins")
    elif(player_one[p1]=='Scissor' and player_two[p2]=='Paper'):
        print("Player one wins")
    elif(player_one[p1]=='Scissor' and player_two[p2]=='Rock'):
        print("Player two wins")
    elif(player_one[p1]=='Paper' and player_two[p2]=='Scissor'):
        print("Player two wins")
    elif(player_one[p1]=='Paper' and player_two[p2]=='Rock'):
        print("Player one wins")

player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={0:'Paper',1:'Scissor',2:'Rock'}
while(1):
    num1=input('Enter your choice player one') 
    num2=input('Enter your choice player two')
    bit_one=int(input('Enter your secret bit player one'))
    bit_two=int(input('Enter your secret bit player two'))
    rock_paper_scissor(num1,num2,bit_one,bit_two)
    ch=input("Do you want to continue y/n")
    if ch=='n':
        break

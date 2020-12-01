from random import randint

hidden=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

shown=[["□","□","□","□","□","□"],["□","□","□","□","□","□"],["□","□","□","□","□","□"],["□","□","□","□","□","□"],["□","□","□","□","□","□"],["□","□","□","□","□","□"]]

def fonction(morpion):
  print("  1 2 3 4 5 6")
  for ligne in range (0,len(morpion)):
   print(ligne+1,end=" ")
   for colonne in range(0,len(morpion[0])):
     print(morpion[ligne][colonne],end=" ")
   print("")


def ajoutcase(mat,lig,col):

  if(lig-1 >= 0 and col-1 >= 0):

    if (mat[lig-1][col-1] !="💣"):
      mat[lig-1][col-1]+=1

  if(lig-1 >= 0):

    if (mat[lig-1][col] !="💣"):
      mat[lig-1][col]+=1
  
  if(lig-1 >= 0 and col+1 <6):

    if (mat[lig-1][col+1] !="💣"):
      mat[lig-1][col+1]+=1

  if(col-1 >= 0):

    if (mat[lig][col-1] !="💣"):
      mat[lig][col-1]+=1

  if(col+1 <6):

    if (mat[lig][col+1] !="💣"):
      mat[lig][col+1]+=1

  if(lig+1 <6 and col-1 >= 0):

    if (mat[lig+1][col-1] !="💣"):
      mat[lig+1][col-1]+=1

  if(lig+1 <6):

    if (mat[lig+1][col] !="💣"):
     mat[lig+1][col]+=1

  if(lig+1 <6 and col+1 <6):

    if (mat[lig+1][col+1] !="💣"):
      mat[lig+1][col+1]+=1


def bombes():
  bombe=0
  while bombe < 6 :
    ligne = randint(0,5)
    colonne= randint(0,5)
    if(hidden[ligne][colonne] != "💣"):
      hidden[ligne][colonne]="💣"
      bombe +=1
      ajoutcase(hidden,ligne,colonne)


def interact(hidden):
  choixL=int(input("choix de la ligne :"))-1
  choixC=int(input("choix de la colonne :"))-1
  shown[choixL][choixC]=hidden[choixL][choixC]
  fonction(shown)
  if(hidden[choixL][choixC] == "💣"):
    print("you exploded")
    return False
  return True


bombes()
fonction(shown)
victory = True
while (victory):
  victory=interact(hidden)

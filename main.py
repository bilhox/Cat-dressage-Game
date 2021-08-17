#coding UTF-8
import time
import settings;
from cat import * ;

def startDialogue():
     print("0>0 [ Game Master ] << Welcome to the tea room !")
     time.sleep(1.5)
     print("0>0 [ Game Master ] << Exit the tea room on becomming the best tamer of cats !")
     time.sleep(1.5)
     print("0>0 [ Game Master ] << You begin with the rank <Simple One> , tame your cat to uprank !")
     time.sleep(1.5)

def experienceCheck(catExperience , experienceRequirement):
     
     if((experienceRequirement - catExperience ) <= 0):
          return True
     else:
          return False

def seeExperience(catExperience , experienceRequirement):

     if(catExperience != -1):
          print("Game << Experience progression : {} / {}".format(catExperience , experienceRequirement))
     else:
          print("Game << Experience progression : {} / {}".format(settings.ExpBars[4],settings.ExpBars[4]))

def seeRanks():
     print("0>0 [ Game Master ] << This is the list of all ranks :")

     for i in range(0,6):
          print("\t> Level {} = {}".format(i+1 , settings.Ranks[i]))

def cmdlist():

     for a in range(len(settings.cmdlist)):
          for b in range(len(settings.cmdlist[a])):
               print("\t",settings.cmdlist[a][b])

def main():

     startDialogue()
     catName = input("0>0 [ Game Master ] << Enter the name of your cat ! -> ")

     cat = Cat(personalname=catName)
     experienceRequirement = settings.ExpBars[cat.expLevel]
     cat.rank = settings.Ranks[cat.expLevel]
     running = 1
     caressCooldown = False
     eatCooldown = False
     washCooldown = False
     walkCooldown = False
     aTime = 0
     bTime = 0
     cTime = 0
     dTime = 0

     while running:
          
          if(experienceCheck(cat.loveExperience , experienceRequirement)):
               cat.expLevel = cat.expLevel + 1
               cat.rank = settings.Ranks[cat.expLevel]
               print("0>0 [ Game Master ] << Felicitations ! You upranked {} !".format(cat.rank))
               if(cat.expLevel == 5):
                    print("0>0 [ Game Master ] << Congrulations to have finished the game !")
                    time.sleep(1)
                    print("0>0 [ Game Master ] << You will no longer receive experience points !")
                    time.sleep(0.5)
                    cat.loveExperience = -1
                    cat.canGetExperience = False
               else:
                    experienceRequirement = settings.ExpBars[cat.expLevel]

          ask = input("You [ {} ] << What should I do to my cat ? (Write <cmd-list> to see all you can do !) -> ".format(cat.rank))

          if((int(time.time()) - aTime) > settings.caressCooldown):caressCooldown = False
          if((int(time.time()) - bTime) > settings.eatCooldown):eatCooldown = False
          if((int(time.time()) - cTime) > settings.washCooldown):washCooldown = False
          if((int(time.time()) - dTime) > settings.walkCooldown):walkCooldown = False

          if(ask == "see experience" or ask == "see exp"):
               i = cat.expLevel
               seeExperience(cat.loveExperience , experienceRequirement)
          
          if(ask == "see Ranks" or ask == "see ranks"):
               seeRanks()

          if(ask == "caress"):
               if(caressCooldown == False):
                    cat.caress()
                    aTime = int(time.time())
                    caressCooldown = True
               else:
                    print("Game << On cooldown !")
          
          if(ask == "eat"):
               if(eatCooldown == False):
                    cat.eat()
                    bTime = int(time.time())
                    eatCooldown = True
               else:
                    print("Game << On cooldown !")
          
          if(ask == "wash"):
               if(washCooldown == False):
                    cat.wash()
                    cTime = int(time.time())
                    washCooldown = True
               else:
                    print("Game << On cooldown !")
          
          if(ask == "walk"):
               if(walkCooldown == False):
                    cat.walk()
                    dTime = int(time.time())
                    walkCooldown = True
               else:
                    print("Game << On cooldown !")
          
          if(ask == "cmd-list"):
               cmdlist()

          if(ask == "exit"):
               running = 0
               print("0>0 [ Game Master ] << You left the game !")

if __name__ == "__main__":

     main()
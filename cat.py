import time;
import settings;
class Cat:
     
     def __init__(self , personalname):
          self.personalname = personalname
          self.loveExperience = 0
          self.expLevel = 0
          self.rank = "Simple One"
          self.canGetExperience = True
          print("0>0 [ Game Master ] <<  {} is now your cat !".format(self.personalname))
          return
     
     def caress(self):
          #Action time = 3 seconds
          print("UwU [ {} ] << RoNrOnRoNrOn . ".format(self.personalname))
          time.sleep(1)
          print("UwU [ {} ] << RoNrOnRoNrOn . .".format(self.personalname))
          time.sleep(1)
          print("UwU [ {} ] << RoNrOnRoNrOn . . .".format(self.personalname))
          time.sleep(1)

          if(self.canGetExperience):
               print("Game << + {} exp points".format(settings.caressExperience))
               self.loveExperience = self.loveExperience + settings.caressExperience
          else:
               print("Game << + 0 exp points (Max Level)")
     
     def eat(self):
          #Action time = 10 seconds
          if(self.expLevel >= 1):
               print("Game << You feed your cat ...")
               time.sleep(2.5)
               print("Game << .")
               time.sleep(2.5)
               print("Game << . .")
               time.sleep(2.5)
               print("Game << . . .")
               time.sleep(2.5)
               if(self.canGetExperience):
                    print("Game << + {} exp points".format(settings.eatExperience))
                    self.loveExperience = self.loveExperience + settings.eatExperience
               else:
                    print("Game << + 0 exp points (Max Level)")
          else:
               print("Game << Your cat don't trust you a lot for this !")
               print("Game << You need to have a higher rank to make that !")
     
     def wash(self):
          
          #Action time = 16 seconds
          if(self.expLevel >= 2):
               print("Game << You are washing your cat ...")
               time.sleep(4)
               print("UwU [ {} ] << O O o O o O Miaou! O o O o O O .".format(self.personalname))
               time.sleep(4)
               print("UwU [ {} ] << O O o O o O Miaou! O o O o O O . .".format(self.personalname))
               time.sleep(4)
               print("UwU [ {} ] << O O o O o O Miaou! O o O o O O . . .".format(self.personalname))
               time.sleep(4)
               if(self.canGetExperience):
                    print("Game << + {} exp points".format(settings.washExperience))
                    self.loveExperience = self.loveExperience + settings.washExperience
               else:
                    print("Game << + 0 exp points (Max Level)")
          else:
               print("Game << Your cat don't trust you a lot for this !")
               print("Game << You need to have a higher rank to make that !")
     
     def walk(self):
          #Action time = 10.5 seconds
          if(self.expLevel >= 3):
               print("Game << You go out of the tea room , walking your cat ...")
               time.sleep(5)
               print("Game << You examine the sky , which beautiful blue color !")
               time.sleep(2)
               print("Game << And this green color on the park , WOA !")
               time.sleep(3)
               print("Game << Time to get back to the tea room !")
               time.sleep(0.5)
               if(self.canGetExperience):
                    print("Game << + {} exp points".format(settings.walkExperience))
                    self.loveExperience = self.loveExperience + settings.walkExperience
               else:
                    print("Game << + 0 exp points (Max Level)")
          else:
               print("Game << Your cat don't trust you a lot for this !")
               print("Game << You need to have a higher rank to make that !")
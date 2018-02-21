class MusicalInstrument:
      numberOfMusicKey = 12

class StringInstrument(MusicalInstrument):
      typeOfWood = "ToneWood"

class Guitar(StringInstrument):
      def __init__(self):
          self.numberOfString = 6
          print("This is guitar consists of {} keys and it is made up of {} and it can play {} number of Music key".format(self.numberOfString,self.typeOfWood,self.numberOfMusicKey))

guitar = Guitar()

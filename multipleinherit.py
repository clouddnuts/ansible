class OperatingSystem:

      multitasking = True
      name = "Mach OS"
class Apple:

      website = "www.apple.com"
      name = "Apple"

class MachBook(OperatingSystem,Apple):

      def __init__(self):
          if self.multitasking is True:
             print("This is a multitasking system,you can visit {}: ".format(self.website))
          print(self.name)

macbook = MachBook()



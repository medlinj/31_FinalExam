"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and JD Medlin.  May 2018.

"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# DONE: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################


def main():
    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------

    print(Pig(5).get_weight())  # this should simply be the weight that was put in, so 5
    print(Pig(5).eat(10))  # should be 10 + 5, which is 15
    print(Pig(0).eat_for_a_year())  # should print 66795, which is all the numbers from 1 to 365 combined
    print(Pig(5).heavier_pig(100))  # if it prints this: <class '__main__.Pig'>, then it is the object
    print(Pig(5).new_pig(1000000))  # if it prints this: <class '__main__.Pig'>, then it is the object


class Pig(object):
    def __init__(self, weight):
        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        # DONE: Implement and test this method.

        self.weight = weight
        self.pig_new = 0

    def get_weight(self):
        """ Returns this Pig's weight. """
        # DONE: Implement and test this method.

        return self.weight

    def eat(self, pounds_of_slop):
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        # DONE: Implement and test this method.

        self.weight = self.weight + pounds_of_slop
        return self.weight

    def eat_for_a_year(self):
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        # DONE: Implement and test this method.

        for k in range(365):
            self.weight = Pig.eat(self, k + 1)
        return self.weight

    def heavier_pig(self, other_pig):
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        # DONE: Implement and test this method.
        if other_pig > self.weight:
            return Pig(other_pig)
        else:
            return Pig(self.weight)

    def new_pig(self, other_pig):
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        # DONE: Implement and test this method.

        if other_pig > self.weight:
            newp = Pig(other_pig)
            return newp
        else:
            new = Pig(self.weight)
            return new


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()

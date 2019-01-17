"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Jacey.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
window = rg.TurtleWindow()
window.tracer(2)
zariyah = rg.SimpleTurtle
zariyah = rg.SimpleTurtle('turtle')
zariyah.pen = rg.Pen('blue',1)
zariyah.backward(50)
for k in range(500):
    zariyah.left(90)
    zariyah.forward(k)
myon = rg.SimpleTurtle
myon = rg.SimpleTurtle('turtle')
myon.pen = rg.Pen('maroon',1)
for k in range(3000):
    myon.right(30)
    myon.backward(k)

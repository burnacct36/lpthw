name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 # lbs
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not that heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right 
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)


# convert Zed's weight and height into metric

metric_weight = weight * 2.2
print "Zed's weight is %s kg." % metric_weight

metric_height = height * 2.54
print "Zed's height is %s cm." % metric_height

#let's round Zed's height
print round(metric_height, 1)


class Parent(object):

  def implicit(self):
    print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child ()

dad.implicit()
son.implicit()

$ python ex44a.py
PARENT implicit()
PARENT implicit()

class Parent(object):

  def override(self):
    print "PARENT override()"

class Child(Parent):

  def override(self):
    print ”CHILD override()”

dad = Parent()
son = Child()

dad.override()
son.override()



class Parent(object):

    def altered(self):
        print ”PARENT altered()”

class Child(Parent):

    def altered(self):
        print ”CHILD, BEFORE PARENT altered()”
        super(Child, self).altered()
        print ”CHILD, AFTER PARENT altered()”

dad = Parent()
son = Child()

dad.altered()
son.altered()


class Parent(object):

  def override(self):
    print ”PARENT override()”

  def implicit(self):
    print ”PARENT implicit()”

  def altered(self):
    print ”PARENT altered()”

class Child(Parent):

   def override(self):
    print ”CHILD override()”

   def altered(self):
    print ”CHILD, BEFORE PARENT altered()”
    super(Child, self).altered()
    print ”CHILD, AFTER PARENT altered()”

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


class Other(object):

  def override(self)
    print ”OTHER override()”

  def implicit(self):
    print ”OTHER implicit()”

  def altered(self):
    print ”OTHER altered()”

   class Child(object):
   def




   son = Child()



  def __init__(self):
self.other = Other()
implicit(self):
self.other.implicit()
override(self):
print ”CHILD override()”
altered(self):
print ”CHILD, BEFORE OTHER altered()”
self.other.altered()
print ”CHILD, AFTER OTHER altered()”

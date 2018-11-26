"""
print("<[100]> evalsupport module start")
print("<[400]> MetaAleph body")
print("<[700]> evalsupport module end")
print("<[1]> evaltime module start")
print("<[2]> ClassOne body")
print('<[7]> ClassThree body')
print("<[200]> deco_alpha")
print("<[9]> ClassFour body")
print("<[11]> ClassOne tests", 30 * '.')
print("<[3]> ClassOne.__init__")
print("<[5]> ClassOne.method_x")
print("<[12]> ClassThree tests", 30 * '.')
print('<[8]> ClassThree.method_y')
print("<[13]> ClassFour tests", 30 * '.')
print("<[300]> deco_alpha:inner_1")
"""

from evalsupport import deco_alpha

print("<[1]> evaltime module start")


class ClassOne():
    print("<[2]> ClassOne body")

    def __init__(self):
        print("<[3]> ClassOne.__init__")

    def __del__(self):
        print("<[4]> ClassOne.__del__")

    def method_x(self):
        print("<[5]> ClassOne.method_x")

    class ClassTwo(object):
        print('<[6]> ClassTwo body')


@deco_alpha
class ClassThree():
    print('<[7]> ClassThree body')

    def method_y(self):
        print('<[8]> ClassThree.method_y')


class ClassFour(ClassThree):
    print("<[9]> ClassFour body")

    def method_y(self):
        print("<[10]> ClassFour.method_y")


if __name__ == "__main__":
    print("<[11]> ClassOne tests", 30 * '.')
    one = ClassOne()

    one.method_x()
    print("<[12]> ClassThree tests", 30 * '.')

    three = ClassThree()
    three.method_y()

    print("<[13]> ClassFour tests", 30 * '.')

    four = ClassFour()
    four.method_y()

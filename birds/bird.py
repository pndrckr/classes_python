class Bird:
    def __init__(self, kind, call, feather_color="white"):
        self.kind = kind
        self.call = call
        self.the_color_of_feathers = feather_color

    def do_call(self):
        return 'a %s goes %s and has %s feathers' % \
               (self.kind, self.call, self.the_color_of_feathers)

class Seabird(Bird):
    def __init__(self, kind, call, diving_depth, feather_color="Red"):
        self.the_diving_depth = diving_depth
        Bird.__init__(self, kind, call, feather_color)

    def do_call(self):
        return Bird.do_call(self) + ", and dives to the depth of %s meters" % \
                                    self.the_diving_depth






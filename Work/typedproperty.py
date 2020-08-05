# Exercise 7.9

def typedproperty(name, expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'expected {expected_type}')
        setattr(self, private_name, val)

    return prop


String = lambda name: typedproperty(name, str)
Integer = lambda name:  typedproperty(name, int)
Float = lambda name:  typedproperty(name, float)
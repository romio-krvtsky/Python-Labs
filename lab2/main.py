import math

from tests import objects_for_testing
from parser.factory.factory import SerializerFactory, SerializerTypes

c = 2


def butoma(a, b):
    return math.sin(a * b * c)


class A:

    def f(self):
        return 5


class B(A):

    def __init__(self):
        pass


if __name__ == '__main__':
    json_serializer = SerializerFactory.create_serializer(SerializerTypes.json)
    yaml_serializer = SerializerFactory.create_serializer(SerializerTypes.toml)

    s = B()
    json_serializer.dump(s, 'temp.json')
    res = json_serializer.load('temp.json')
    print(res.f())

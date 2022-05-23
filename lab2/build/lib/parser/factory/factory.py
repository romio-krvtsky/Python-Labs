import enum
from parser.serializers import serializers


class SerializerTypes(enum.Enum):
    json = 3
    yaml = 2
    toml = 1


class SerializerFactory:

    @staticmethod
    def create_serializer(serializer_type):
        if serializer_type == SerializerTypes.json:
            return serializers.JsonSerializer()

        elif serializer_type == SerializerTypes.yaml:
            return serializers.YamlSerializer()

        elif serializer_type == SerializerTypes.toml:
            return serializers.TomlSerializer()

        else:
            return None

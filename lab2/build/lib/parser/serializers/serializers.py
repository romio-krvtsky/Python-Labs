import abc
import inspect
import toml
import tomli
import types
import yaml

from parser.exceptions.parsing_exception import ParsingException
from parser.json_properties.json_types_deserializer import JsonTypesDeserializer
from parser.json_properties.json_types_serializer import JsonTypesSerializer
from parser.yaml_toml_properties import yaml_toml_types_serializer, yaml_toml_types_deserializer


class Serializer:

    @abc.abstractmethod
    def dump(self, obj, filename: str, mode='w'):
        pass

    @abc.abstractmethod
    def dumps(self, obj):
        pass

    @abc.abstractmethod
    def load(self, filename: str, mode='r'):
        pass

    @abc.abstractmethod
    def loads(self, s: str):
        pass


class JsonSerializer(Serializer):

    def dump(self, obj, filename: str, mode='w'):
        res = self.dumps(obj)

        with open(filename, mode) as file:
            file.write(res)

    def dumps(self, obj):

        try:

            res = ''
            if isinstance(obj, types.FunctionType):
                res = JsonTypesSerializer.function_serializer(obj)

            elif isinstance(obj, types.LambdaType):
                res = JsonTypesSerializer.lambda_function_serializer(obj)

            elif isinstance(obj, types.BuiltinFunctionType):
                res = JsonTypesSerializer.builtin_function_serializer(obj)

            elif isinstance(obj, int):
                temp = JsonTypesSerializer.int_serializer(obj)
                res = temp

            elif isinstance(obj, float):
                temp = JsonTypesSerializer.float_serializer(obj)
                res = temp

            elif isinstance(obj, str):
                res = f'"{obj}"'

            elif isinstance(obj, list):
                res = JsonTypesSerializer.list_serializer(obj)

            elif isinstance(obj, dict):
                res = JsonTypesSerializer.dict_serializer(obj)

            elif isinstance(obj, tuple):
                res = JsonTypesSerializer.tuple_serializer(obj)

            elif isinstance(obj, bool):
                temp = JsonTypesSerializer.bool_serializer(obj)
                res = temp

            elif isinstance(obj, types.NoneType):
                temp = JsonTypesSerializer.none_serializer()
                res = temp

            elif inspect.isclass(obj):
                res = JsonTypesSerializer.class_serializer(obj)

            elif inspect.isclass(type(obj)):
                res = JsonTypesSerializer.class_instance_serializer(obj)

            elif inspect.iscode(obj):
                res = JsonTypesSerializer.code_object_serializer(obj)

            else:
                raise TypeError(f'Object of {type(obj)} is not JSON serializable')

        except TypeError as err:
            print(err)

        finally:

            if not res:
                res = JsonTypesSerializer.none_serializer()

            return res

    def load(self, filename: str, mode='r'):
        with open(filename, mode) as file:
            buffer_value = file.read()
        res = self.loads(buffer_value)

        return res

    def loads(self, s: str):

        try:

            res = JsonTypesDeserializer.json_string_deserializer(s)

            return res

        except ParsingException as err:

            print(err)
            raise SystemExit(1)


class YamlSerializer(Serializer):

    def dump(self, obj, filename: str, mode='w'):
        res = yaml_toml_types_serializer.YamlTomlTypesSerializer.get_type(obj)
        with open(filename, mode) as file:
            yaml.dump(res, file)

    def dumps(self, obj) -> str:
        res = yaml_toml_types_serializer.YamlTomlTypesSerializer.get_type(obj)
        res = yaml.dump(res)

        return res

    def load(self, filename: str, mode='r'):
        with open(filename, mode) as file:
            buffer_value = yaml.unsafe_load(file)

        try:
            res = yaml_toml_types_deserializer.YamlTomlTypesDeserializer.get_type(buffer_value)

        except ParsingException as err:
            print(err)

            return None

        return res

    def loads(self, s: str):
        buffer_value = yaml.safe_load(s)

        try:
            res = yaml_toml_types_deserializer.YamlTomlTypesDeserializer.get_type(buffer_value)

        except ParsingException as err:
            print(err)

            return None

        return res


class TomlSerializer(Serializer):

    def dump(self, obj, filename: str, mode='w'):
        res = yaml_toml_types_serializer.YamlTomlTypesSerializer.get_type(obj)
        with open(filename, mode) as file:
            toml.dump(res, file)

    def dumps(self, obj):
        res = yaml_toml_types_serializer.YamlTomlTypesSerializer.get_type(obj)
        res = toml.dumps(res)

        return res

    def load(self, filename: str, mode='rb'):
        """needed binary file object for reading"""
        with open(filename, mode) as file:
            buffer_value = tomli.load(file)

        try:
            res = yaml_toml_types_deserializer.YamlTomlTypesDeserializer.get_type(buffer_value)

        except ParsingException as err:
            print(err)

            return None

        return res

    def loads(self, s: str):
        """needed binary file object for reading"""
        buffer_value = tomli.loads(s)

        try:
            res = yaml_toml_types_deserializer.YamlTomlTypesDeserializer.get_type(buffer_value)

        except ParsingException as err:
            print(err)

            return None

        return res

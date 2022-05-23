import inspect
import types


class JsonTypesSerializer:

    @staticmethod
    def function_serializer(func: types.FunctionType):
        result_string = ''

        """start of object recording"""
        result_string += '{ '

        """this item needed to define type of the object"""
        result_string += '"type": "FunctionType", '

        """write necessary modules for working"""
        globals = JsonTypesSerializer.globals_serializer(func)
        result_string += f'"__globals__": {globals}, '

        """is the number of local variables used by the function"""
        co_nlocals = func.__code__.co_nlocals  # other items needed to serialize function
        buffer_value = JsonTypesSerializer.int_serializer(co_nlocals)
        result_string += f'"co_nlocals": {buffer_value}, '

        """is the total number of positional arguments"""
        co_argcount = func.__code__.co_argcount
        buffer_value = JsonTypesSerializer.int_serializer(co_argcount)
        result_string += f'"co_argcount": {buffer_value}, '

        """is a tuple containing the names of the local variables"""
        co_varnames = func.__code__.co_varnames
        buffer_value = JsonTypesSerializer.tuple_serializer(co_varnames)
        result_string += f'"co_varnames": {buffer_value}, '

        """is a tuple containing the names used by the bytecode"""
        co_names = func.__code__.co_names
        buffer_value = JsonTypesSerializer.tuple_serializer(co_names)
        result_string += f'"co_names": {buffer_value}, '

        """is a tuple containing the names of local variables that are
         referenced by nested functions"""
        co_cellvars = func.__code__.co_cellvars
        buffer_value = JsonTypesSerializer.tuple_serializer(co_cellvars)
        result_string += f'"co_cellvars": {buffer_value}, '

        """is a tuple containing the names of free variables"""
        co_freevars = func.__code__.co_freevars
        buffer_value = JsonTypesSerializer.tuple_serializer(co_freevars)
        result_string += f'"co_freevars": {buffer_value}, '

        """is the number of positional-only arguments"""
        co_posonlyargcount = func.__code__.co_posonlyargcount
        buffer_value = JsonTypesSerializer.int_serializer(co_posonlyargcount)
        result_string += f'"co_posonlyargcount": {buffer_value}, '

        """is the number of keyword-only arguments"""
        co_kwonlyargcount = func.__code__.co_kwonlyargcount
        buffer_value = JsonTypesSerializer.int_serializer(co_kwonlyargcount)
        result_string += f'"co_kwonlyargcount": {buffer_value}, '

        """is the first line number of the function"""
        co_firstlineno = func.__code__.co_firstlineno
        buffer_value = JsonTypesSerializer.int_serializer(co_firstlineno)
        result_string += f'"co_firstlineno": {buffer_value}, '

        """is a string encoding the mapping from bytecode offsets to line numbers"""
        co_lnotab = func.__code__.co_lnotab
        buffer_value = JsonTypesSerializer.list_serializer(list(co_lnotab))
        result_string += f'"co_lnotab": {buffer_value}, '

        """is the required stack size"""
        co_stacksize = func.__code__.co_stacksize
        buffer_value = JsonTypesSerializer.int_serializer(co_stacksize)
        result_string += f'"co_stacksize": {buffer_value}, '

        """is a string representing the sequence of bytecode instructions"""
        co_code = func.__code__.co_code
        buffer_value = JsonTypesSerializer.list_serializer(list(co_code))
        result_string += f'"co_code": {buffer_value}, '

        """it gives the name of the function"""
        co_name = func.__code__.co_name
        result_string += f'"co_name": "{co_name}", '

        """is a tuple containing the literals used by the bytecode"""
        co_consts = func.__code__.co_consts
        buffer_value = JsonTypesSerializer.tuple_serializer(co_consts)
        result_string += f'"co_consts": {buffer_value}, '

        """is an integer encoding a number of flags for the interpreter"""
        co_flags = func.__code__.co_flags
        buffer_value = JsonTypesSerializer.int_serializer(co_flags)
        result_string += f'"co_flags": {buffer_value} '

        """end of object recording"""
        result_string += '}'

        return result_string

    """method type - the type of methods of user-defined class instances"""

    @staticmethod
    def class_instance_method_serializer(mthd: types.MethodType):
        res = JsonTypesSerializer.function_serializer(mthd)

        return res

    @staticmethod
    def code_object_serializer(code_object: types.CodeType):
        result_string = ''

        """start of object recording"""
        result_string += '{ '

        """this item needed to define type of the object"""
        result_string += '"type": "CodeType", '

        """is the number of local variables used by the function"""
        co_nlocals = code_object.co_nlocals  # other items needed to serialize function
        buffer_value = JsonTypesSerializer.int_serializer(co_nlocals)
        result_string += f'"co_nlocals": {buffer_value}, '

        """it gives the name of the function"""
        co_name = code_object.co_name
        result_string += f'"co_name": "{co_name}", '

        """is the total number of positional arguments"""
        co_argcount = code_object.co_argcount
        buffer_value = JsonTypesSerializer.int_serializer(co_argcount)
        result_string += f'"co_argcount": {buffer_value}, '

        """is a tuple containing the names of the local variables"""
        co_varnames = code_object.co_varnames
        buffer_value = JsonTypesSerializer.tuple_serializer(co_varnames)
        result_string += f'"co_varnames": {buffer_value}, '

        """is a tuple containing the names used by the bytecode"""
        co_names = code_object.co_names
        buffer_value = JsonTypesSerializer.tuple_serializer(co_names)
        result_string += f'"co_names": {buffer_value}, '

        """is a tuple containing the names of local variables that are
         referenced by nested functions"""
        co_cellvars = code_object.co_cellvars
        buffer_value = JsonTypesSerializer.tuple_serializer(co_cellvars)
        result_string += f'"co_cellvars": {buffer_value}, '

        """is a tuple containing the names of free variables"""
        co_freevars = code_object.co_freevars
        buffer_value = JsonTypesSerializer.tuple_serializer(co_freevars)
        result_string += f'"co_freevars": {buffer_value}, '

        """is the number of positional-only arguments"""
        co_posonlyargcount = code_object.co_posonlyargcount
        buffer_value = JsonTypesSerializer.int_serializer(co_posonlyargcount)
        result_string += f'"co_posonlyargcount": {buffer_value}, '

        """is the number of keyword-only arguments"""
        co_kwonlyargcount = code_object.co_kwonlyargcount
        buffer_value = JsonTypesSerializer.int_serializer(co_kwonlyargcount)
        result_string += f'"co_kwonlyargcount": {buffer_value}, '

        """is the first line number of the function"""
        co_firstlineno = code_object.co_firstlineno
        buffer_value = JsonTypesSerializer.int_serializer(co_firstlineno)
        result_string += f'"co_firstlineno": {buffer_value}, '

        """is a string encoding the mapping from bytecode offsets to line numbers"""
        co_lnotab = code_object.co_lnotab
        buffer_value = JsonTypesSerializer.list_serializer(list(co_lnotab))
        result_string += f'"co_lnotab": {buffer_value}, '

        """is the required stack size"""
        co_stacksize = code_object.co_stacksize
        buffer_value = JsonTypesSerializer.int_serializer(co_stacksize)
        result_string += f'"co_stacksize": {buffer_value}, '

        """is a string representing the sequence of bytecode instructions"""
        co_code = code_object.co_code
        buffer_value = JsonTypesSerializer.list_serializer(list(co_code))
        result_string += f'"co_code": {buffer_value}, '

        """is a tuple containing the literals used by the bytecode"""
        co_consts = code_object.co_consts
        buffer_value = JsonTypesSerializer.tuple_serializer(co_consts)
        result_string += f'"co_consts": {buffer_value}, '

        """is an integer encoding a number of flags for the interpreter"""
        co_flags = code_object.co_flags
        buffer_value = JsonTypesSerializer.int_serializer(co_flags)
        result_string += f'"co_flags": {buffer_value} '

        """end of object recording"""
        result_string += '}'

        return result_string

    @staticmethod
    def lambda_function_serializer(func: types.LambdaType):
        res = JsonTypesSerializer.function_serializer(func)

        return res

    @staticmethod
    def builtin_function_serializer(func: types.BuiltinFunctionType):
        """in module that represent BuiltinFunctionType specified only name and type
        we will find it by name in the builtins module"""
        result_string = ''

        result_string += '{ '

        result_string += '"type": "BuiltinFunctionType", '

        result_string += f'"name": "{func.__name__}" '

        result_string += '}'

        return result_string

    @staticmethod
    def globals_serializer(func: types.FunctionType):
        result_string = ''
        globals = func.__globals__
        global_names = list(func.__code__.co_names)

        """if globals is empty write down the dict()"""
        if globals:
            result_string += '{ '

        else:
            result_string += '{'

        buffer_value = None
        counter = 0
        for name in global_names:
            counter += 1

            try:
                obj = globals[name]

            except KeyError as err:
                continue

            try:
                """the beginning of a series of conditional operators to 
                determine the global object type"""
                if isinstance(obj, int):
                    buffer_value = JsonTypesSerializer.int_serializer(obj)

                elif isinstance(obj, types.FunctionType):
                    buffer_value = JsonTypesSerializer.function_serializer(obj)
                elif isinstance(obj, types.MethodType):
                    buffer_value = JsonTypesSerializer.class_instance_method_serializer(obj)

                elif isinstance(obj, types.LambdaType):
                    buffer_value = JsonTypesSerializer.lambda_function_serializer(obj)

                elif isinstance(obj, types.BuiltinFunctionType):
                    buffer_value = JsonTypesSerializer.builtin_function_serializer(obj)

                elif isinstance(obj, float):
                    buffer_value = JsonTypesSerializer.float_serializer(obj)

                elif isinstance(obj, str):
                    buffer_value = f'"{obj}"'

                elif isinstance(obj, list):
                    buffer_value = JsonTypesSerializer.list_serializer(obj)

                elif isinstance(obj, dict):
                    buffer_value = JsonTypesSerializer.dict_serializer(obj)

                elif isinstance(obj, tuple):
                    buffer_value = JsonTypesSerializer.tuple_serializer(obj)

                elif isinstance(obj, bool):
                    buffer_value = JsonTypesSerializer.bool_serializer(obj)

                elif isinstance(obj, types.NoneType):
                    buffer_value = JsonTypesSerializer.none_serializer()

                elif inspect.isclass(obj):
                    buffer_value = JsonTypesSerializer.class_serializer(obj)

                elif inspect.iscode(obj):
                    buffer_value = JsonTypesSerializer.code_object_serializer(obj)

                elif isinstance(obj, types.ModuleType):
                    continue

                elif inspect.isclass(type(obj)):
                    buffer_value = JsonTypesSerializer.class_instance_serializer(obj)

                else:

                    raise TypeError(f'Object of {type(obj)} is not JSON serializable')

            except TypeError as err:
                print(err)

                raise SystemExit(1)

            if counter == len(global_names):
                result_string += f'"{name}": {buffer_value} '
            else:
                result_string += f'"{name}": {buffer_value}, '

        """we need this conditional operator to close the dict"""
        if len(result_string) > 2:

            if result_string[-2] != ',':
                result_string = result_string[:-1]
                result_string += ', '

        """save the names of the modules connected in this module so that we can load them later"""
        value = 'module'
        for key in globals.keys():

            if isinstance(globals[key], types.ModuleType):
                name = globals[key].__name__
                result_string += f'"{name}": "{value}", '

            else:
                continue

        """we need this conditional operator to close the dict"""
        if result_string[-2] == ',':
            result_string = result_string[:-2]
            result_string += ' '

        if result_string == '{ ':
            result_string = 'dict()'

        else:
            result_string += '}'

        return result_string

    @staticmethod
    def class_serializer(obj: type):
        result_string = ''

        if obj:
            result_string += '{ '

        else:
            result_string += '{'

        result_string += f'"type": "ClassType", '

        if obj.__name__ != 'object':

            buffer_value = obj.__name__
            result_string += f'"name": "{buffer_value}", '

            buffer_value = JsonTypesSerializer.list_serializer(list(obj.__bases__))
            result_string += f'"bases": {buffer_value}, '

            buffer_value = JsonTypesSerializer.dict_serializer(obj.__dict__)
            result_string += f'"type_definition": {buffer_value} '

        else:

            buffer_value = obj.__name__
            result_string += f'"name": "{buffer_value}" '

        result_string += '}'

        return result_string

    @staticmethod
    def class_instance_serializer(obj: type):
        result_string = ''

        if obj:
            result_string += '{ '

        else:
            result_string += '{'

        result_string += f'"type": "ClassInstanceType", '

        buffer_value = obj.__class__.__name__
        result_string += f'"class_name": "{buffer_value}", '

        buffer_value = JsonTypesSerializer.class_serializer(obj.__class__)
        result_string += f'"class_definition": {buffer_value}, '

        buffer_value = JsonTypesSerializer.dict_serializer(obj.__dict__)
        result_string += f'"object_definition": {buffer_value} '

        result_string += '}'

        return result_string

    @staticmethod
    def int_serializer(obj: int):

        if isinstance(obj, bool):
            res = JsonTypesSerializer.bool_serializer(obj)

        else:
            res = str(obj)

        return res

    @staticmethod
    def list_serializer(obj: list):
        result_string = ''

        if obj:
            result_string += '[ '

        else:
            result_string += '['

        counter = 0
        for item in obj:
            counter += 1

            try:

                if isinstance(item, types.FunctionType):
                    buffer_value = JsonTypesSerializer.function_serializer(item)

                elif isinstance(item, types.MethodType):
                    buffer_value = JsonTypesSerializer.class_instance_method_serializer(item)

                elif isinstance(item, types.LambdaType):
                    buffer_value = JsonTypesSerializer.lambda_function_serializer(item)

                elif isinstance(item, types.BuiltinFunctionType):
                    buffer_value = JsonTypesSerializer.builtin_function_serializer(item)

                elif isinstance(item, int):
                    temp = JsonTypesSerializer.int_serializer(item)
                    buffer_value = temp

                elif isinstance(item, float):
                    temp = JsonTypesSerializer.float_serializer(item)
                    buffer_value = temp

                elif isinstance(item, str):
                    buffer_value = f'"{item}"'

                elif isinstance(item, list):
                    buffer_value = JsonTypesSerializer.list_serializer(item)

                elif isinstance(item, dict):
                    buffer_value = JsonTypesSerializer.dict_serializer(item)

                elif isinstance(item, tuple):
                    buffer_value = JsonTypesSerializer.tuple_serializer(item)

                elif isinstance(item, bool):
                    temp = JsonTypesSerializer.bool_serializer(item)
                    buffer_value = temp

                elif isinstance(item, types.NoneType):
                    temp = JsonTypesSerializer.none_serializer()
                    buffer_value = temp

                elif inspect.isclass(item):
                    buffer_value = JsonTypesSerializer.class_serializer(item)

                elif inspect.iscode(item):
                    buffer_value = JsonTypesSerializer.code_object_serializer(item)

                elif inspect.isclass(type(item)):
                    buffer_value = JsonTypesSerializer.class_instance_serializer(item)

                else:

                    raise TypeError(f'Object of {type(item)} is not JSON serializable')

            except TypeError as err:
                print(err)

                raise SystemExit(1)

            finally:

                if counter != len(obj):
                    result_string += f'{buffer_value}, '

                else:
                    result_string += f'{buffer_value} '

        result_string += ']'

        return result_string

    @staticmethod
    def dict_serializer(obj: dict):
        result_string = ''

        """if obj is empty write down the dict()"""
        if obj:
            result_string += '{ '

        else:
            result_string += '{'

        key_buffer_value, buffer_value = '', ''
        counter = 0  # this counter need to find the last element
        for key, value in obj.items():
            counter += 1
            """if the key is in the extra_keys then we will not serialize this item"""
            extra_keys = [
                '__module__',
                '__dict__',
                '__weakref__',
                '__doc__',
                '__hash__'
            ]
            if key not in extra_keys:

                try:

                    """the beginning of a series of conditional operators to 
                    determine the key type"""
                    if isinstance(key, int):
                        temp = JsonTypesSerializer.int_serializer(key)
                        key_buffer_value = f'"{temp}"'

                    elif isinstance(key, float):
                        temp = JsonTypesSerializer.float_serializer(key)
                        key_buffer_value = f'"{temp}"'

                    elif isinstance(key, str):
                        key_buffer_value = f'"{key}"'

                    elif isinstance(key, bool):
                        temp = JsonTypesSerializer.bool_serializer(key)
                        key_buffer_value = f'"{temp}"'

                    elif isinstance(key, types.NoneType):
                        temp = JsonTypesSerializer.none_serializer()
                        key_buffer_value = f'"{temp}"'

                    else:

                        raise TypeError(f'keys must be str, int, float, bool or None, not {type(key)}')

                except TypeError as err:
                    print(err)

                    raise SystemExit(1)
                    """end of a series of conditional operators to 
                    determine the key type"""

                try:

                    """the beginning of a series of conditional operators to 
                    determine the value type"""
                    if isinstance(value, int):
                        temp = JsonTypesSerializer.int_serializer(value)
                        buffer_value = temp

                    elif isinstance(value, types.FunctionType):
                        buffer_value = JsonTypesSerializer.function_serializer(value)

                    elif isinstance(value, types.MethodType):
                        buffer_value = JsonTypesSerializer.class_instance_method_serializer(value)

                    elif isinstance(value, types.LambdaType):
                        buffer_value = JsonTypesSerializer.lambda_function_serializer(value)

                    elif isinstance(value, types.BuiltinFunctionType):
                        buffer_value = JsonTypesSerializer.builtin_function_serializer(value)

                    elif isinstance(value, float):
                        temp = JsonTypesSerializer.float_serializer(value)
                        buffer_value = temp

                    elif isinstance(value, str):
                        buffer_value = f'"{value}"'

                    elif isinstance(value, list):
                        buffer_value = JsonTypesSerializer.list_serializer(value)

                    elif isinstance(value, dict):
                        buffer_value = JsonTypesSerializer.dict_serializer(value)

                    elif isinstance(value, tuple):
                        buffer_value = JsonTypesSerializer.tuple_serializer(value)

                    elif isinstance(value, bool):
                        temp = JsonTypesSerializer.bool_serializer(value)
                        buffer_value = temp

                    elif isinstance(value, types.NoneType):
                        temp = JsonTypesSerializer.none_serializer()
                        buffer_value = temp

                    elif inspect.isclass(value):
                        buffer_value = JsonTypesSerializer.class_serializer(value)

                    elif inspect.iscode(value):
                        buffer_value = JsonTypesSerializer.code_object_serializer(value)

                    elif inspect.isclass(type(value)):
                        buffer_value = JsonTypesSerializer.class_instance_serializer(value)

                    else:

                        raise TypeError(f'Object of {type(value)} is not JSON serializable')

                except TypeError as err:
                    print(err)

                    raise SystemExit(1)

                finally:

                    if counter == len(obj):
                        result_string += f'{key_buffer_value}: {buffer_value} '

                    else:
                        result_string += f'{key_buffer_value}: {buffer_value}, '

        """we need this conditional operator to close the dict"""
        if len(result_string) > 2:

            if result_string[-2] == ',':
                result_string = result_string[:-2]
                result_string += ' '

        if result_string == '{ ':
            result_string = 'dict()'

        else:

            if result_string == '{':
                result_string += '}'

            else:

                result_string += '}'

        return result_string

    @staticmethod
    def tuple_serializer(obj: tuple):
        res = JsonTypesSerializer.list_serializer(list(obj))

        return res

    @staticmethod
    def bool_serializer(obj: bool):
        return str(obj).lower()

    @staticmethod
    def float_serializer(obj: float):
        return str(obj)

    @staticmethod
    def none_serializer():
        return 'null'

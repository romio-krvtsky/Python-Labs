import inspect
import types


class YamlTomlTypesSerializer:

    @staticmethod
    def get_type(obj):

        if isinstance(obj, int) or \
                isinstance(obj, float) or \
                isinstance(obj, str) or \
                isinstance(obj, bool) or \
                isinstance(obj, types.NoneType):
            res = obj

        elif isinstance(obj, types.FunctionType):
            res = YamlTomlTypesSerializer.function_serializer(                obj            )

        elif isinstance(obj, types.LambdaType):
            res = YamlTomlTypesSerializer.lambda_function_serializer(                obj            )

        elif isinstance(obj, types.BuiltinFunctionType):
            res = YamlTomlTypesSerializer.builtin_function_serializer(                obj            )

        elif isinstance(obj, types.MethodType):
            res = YamlTomlTypesSerializer.class_instance_method_serializer(obj)

        elif isinstance(obj, list):
            res = YamlTomlTypesSerializer.list_serializer(                obj            )

        elif isinstance(obj, dict):
            res = YamlTomlTypesSerializer.dict_serializer(                obj            )

        elif isinstance(obj, tuple):
            res = YamlTomlTypesSerializer.tuple_serializer(                obj            )

        elif isinstance(obj, types.ModuleType):
            res = 'module'

        elif inspect.isclass(obj):
            res = YamlTomlTypesSerializer.class_serializer(                obj            )

        elif inspect.iscode(obj):
            res = YamlTomlTypesSerializer.code_object_serializer(                obj            )

        elif inspect.isclass(type(obj)):
            res = YamlTomlTypesSerializer.class_instance_serializer(                obj            )

        else:

            raise TypeError(f'Object of {type(obj)} is not YAML serializable')

        return res

    @staticmethod
    def function_serializer(func: types.FunctionType):
        func_obj = dict()

        func_obj['type'] = 'FunctionType'

        """write necessary modules for working"""
        globs = YamlTomlTypesSerializer.globals_serializer(func)
        func_obj['__globals__'] = globs

        """write the code_object of function"""
        code = YamlTomlTypesSerializer.code_object_serializer(func.__code__)
        func_obj['__code__'] = code

        return func_obj

    @staticmethod
    def lambda_function_serializer(func: types.LambdaType):
        res = YamlTomlTypesSerializer.function_serializer(            func,        )

        return res

    @staticmethod
    def builtin_function_serializer(func: types.BuiltinFunctionType):
        """
        in module that represent BuiltinFunctionType specified only name and type
        we will find it by name in the builtins module
        """
        builtin_func_obj = {
            'type': 'BuiltinFunctionType',
            'name': func.__name__
        }

        return builtin_func_obj

    @staticmethod
    def class_instance_method_serializer(mthd: types.MethodType):
        res = YamlTomlTypesSerializer.function_serializer(            mthd        )

        return res

    @staticmethod
    def list_serializer(obj: list):

        list_obj = list()
        for item in obj:

            try:

                buffer_value = YamlTomlTypesSerializer.get_type(item)
                list_obj.append(buffer_value)

            except TypeError as err:
                print(err)

                raise SystemExit(1)

        return list_obj

    @staticmethod
    def dict_serializer(obj: dict):

        dict_obj = dict()
        key_buffer_value, buffer_value = None, None
        for key, value in obj.items():

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

                    """determine the key type"""
                    if isinstance(key, int) or \
                            isinstance(key, float) or \
                            isinstance(key, str) or \
                            isinstance(key, bool) or \
                            isinstance(key, types.NoneType):
                        key_buffer_value = key

                    else:

                        raise TypeError(f'keys must be str, int, float, bool or None, not {type(key)}')

                except TypeError as err:
                    print(err)

                    raise SystemExit(1)

                try:

                    """determine the value type"""
                    buffer_value = YamlTomlTypesSerializer.get_type(value)

                except TypeError as err:
                    print(err)

                    raise SystemExit(1)

                finally:
                    dict_obj[key_buffer_value] = buffer_value

        return dict_obj

    @staticmethod
    def tuple_serializer(obj: tuple):
        res = YamlTomlTypesSerializer.list_serializer(list(obj))

        return res

    @staticmethod
    def class_serializer(obj: type):
        """
        in key 'type' we will record 'ClassType' to determine that our object is class
        also key 'name' store the name of the class
        key 'bases' - list of the base classes
        key 'type_definition' - dict of methods and class attrs
        """
        class_obj = dict()
        class_obj['type'] = 'ClassType'

        if obj.__name__ != 'object':

            buffer_value = obj.__name__
            class_obj['name'] = buffer_value

            buffer_value = YamlTomlTypesSerializer.list_serializer(
                list(obj.__bases__),
            )
            class_obj['bases'] = buffer_value

            buffer_value = YamlTomlTypesSerializer.dict_serializer(
                obj.__dict__,
            )
            class_obj['type_definition'] = buffer_value

        else:

            buffer_value = obj.__name__
            class_obj['name'] = buffer_value

        return class_obj

    @staticmethod
    def class_instance_serializer(obj: type):
        """
        in the key 'type' wi will record 'ClassInstanceType'
        to determine that our object is class instance
        also key 'class_definition' store all information about class to create it
        key 'object_definition' - dict of methods and attrs of class instance
        """
        class_instance_obj = dict()
        class_instance_obj['type'] = 'ClassInstanceType'

        buffer_value = YamlTomlTypesSerializer.class_serializer(
            obj.__class__,
        )
        class_instance_obj['class_definition'] = buffer_value

        buffer_value = YamlTomlTypesSerializer.dict_serializer(
            obj.__dict__,
        )
        class_instance_obj['object_definition'] = buffer_value

        return class_instance_obj

    @staticmethod
    def code_object_serializer(obj: types.CodeType):
        code_object = dict()

        """this item needed to define type of the object"""
        code_object['type'] = 'CodeType'

        """is the number of local variables used by the function"""
        co_nlocals = obj.co_nlocals
        code_object['co_nlocals'] = co_nlocals

        """it gives the name of the function"""
        co_name = obj.co_name
        code_object['co_name'] = co_name

        co_filename = obj.co_filename
        code_object['co_filename'] = co_filename

        """is the total number of positional arguments"""
        co_argcount = obj.co_argcount
        code_object['co_argcount'] = co_argcount

        """is a tuple containing the names of the local variables"""
        co_varnames = obj.co_varnames
        buffer_value = YamlTomlTypesSerializer.tuple_serializer(co_varnames)
        code_object['co_varnames'] = buffer_value

        """is a tuple containing the names used by the bytecode"""
        co_names = obj.co_names
        buffer_value = YamlTomlTypesSerializer.tuple_serializer(co_names)
        code_object['co_names'] = buffer_value

        """is a tuple containing the names of local variables that are
         referenced by nested functions"""
        co_cellvars = obj.co_cellvars
        buffer_value = YamlTomlTypesSerializer.tuple_serializer(co_cellvars)
        code_object['co_cellvars'] = buffer_value

        """is a tuple containing the names of free variables"""
        co_freevars = obj.co_freevars
        buffer_value = YamlTomlTypesSerializer.tuple_serializer(co_freevars)
        code_object['co_freevars'] = buffer_value

        """is the number of positional-only arguments"""
        co_posonlyargcount = obj.co_posonlyargcount
        code_object['co_posonlyargcount'] = co_posonlyargcount

        """is the number of keyword-only arguments"""
        co_kwonlyargcount = obj.co_kwonlyargcount
        code_object['co_kwonlyargcount'] = co_kwonlyargcount

        """is the first line number of the function"""
        co_firstlineno = obj.co_firstlineno
        code_object['co_firstlineno'] = co_firstlineno

        """is a string encoding the mapping from bytecode offsets to line numbers"""
        co_lnotab = obj.co_lnotab
        buffer_value = YamlTomlTypesSerializer.list_serializer(list(co_lnotab))
        code_object['co_lnotab'] = buffer_value

        """is the required stack size"""
        co_stacksize = obj.co_stacksize
        code_object['co_stacksize'] = co_stacksize

        """is a string representing the sequence of bytecode instructions"""
        co_code = obj.co_code
        buffer_value = YamlTomlTypesSerializer.list_serializer(list(co_code))
        code_object['co_code'] = buffer_value

        """is a tuple containing the literals used by the bytecode"""
        co_consts = obj.co_consts
        buffer_value = YamlTomlTypesSerializer.tuple_serializer(co_consts)
        code_object['co_consts'] = buffer_value

        """is an integer encoding a number of flags for the interpreter"""
        co_flags = obj.co_flags
        code_object['co_flags'] = co_flags

        return code_object

    @staticmethod
    def globals_serializer(func: types.FunctionType):
        globs_obj = dict()
        globs = func.__globals__
        global_names = list(func.__code__.co_names)

        for name in global_names:

            try:
                obj = globs[name]

            except KeyError:
                continue

            try:
                buffer_value = YamlTomlTypesSerializer.get_type(obj)
                globs_obj[name] = buffer_value

            except TypeError as err:
                print(err)

                raise SystemExit(1)

        return globs_obj

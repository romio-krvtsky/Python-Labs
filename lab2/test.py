from parser.factory.factory import SerializerFactory, SerializerTypes
from tests import objects_for_testing
from unittest import TestCase, main


class SerializerTest(TestCase):

    def setUp(self):
        self.json_serializer = SerializerFactory.create_serializer(SerializerTypes.json)
        self.yaml_serializer = SerializerFactory.create_serializer(SerializerTypes.yaml)
        self.toml_serializer = SerializerFactory.create_serializer(SerializerTypes.toml)
        self.json_filename = 'tests/file.json'
        self.yaml_filename = 'tests/file.yaml'
        self.toml_filename = 'tests/file.toml'

    def test_function(self):
        """
        Testing serialization of function with builtin function inside
        """

        """JSON test"""
        print(objects_for_testing.Processor.__dict__)
        self.json_serializer.dump(
            objects_for_testing.func_with_builtin_func,
            self.json_filename
        )

        res = self.json_serializer.load(self.json_filename)

        non_sorted_list = [9, 8, 7, 14, 28, 2, 3]
        sorted_list = res(non_sorted_list)
        non_sorted_list.sort()
        self.assertEqual(sorted_list, non_sorted_list)

        """YAML test"""

        self.yaml_serializer.dump(
            objects_for_testing.func_with_builtin_func,
            self.yaml_filename
        )

        res = self.yaml_serializer.load(self.yaml_filename)

        non_sorted_list = [9, 8, 7, 14, 28, 2, 3]
        sorted_list = res(non_sorted_list)
        non_sorted_list.sort()
        self.assertEqual(sorted_list, non_sorted_list)

        """TOML test"""

        self.toml_serializer.dump(
            objects_for_testing.func_with_builtin_func,
            self.toml_filename
        )

        res = self.toml_serializer.load(self.toml_filename)

        non_sorted_list = [9, 8, 7, 14, 28, 2, 3]
        sorted_list = res(non_sorted_list)
        non_sorted_list.sort()
        self.assertEqual(sorted_list, non_sorted_list)

    def test_serialization_builtin_function(self):
        """
        Testing serialization of builtin function
        """

        """JSON test"""

        self.json_serializer.dump(abs, self.json_filename)

        res = self.json_serializer.load(self.json_filename)

        for i in range(-5, 5):
            self.assertEqual(res(i), abs(i))

        """YAML test"""
        self.yaml_serializer.dump(abs, self.yaml_filename)

        res = self.yaml_serializer.load(self.yaml_filename, )

        for i in range(-5, 5):
            self.assertEqual(res(i), abs(i))

        """TOML test"""
        self.toml_serializer.dump(abs, self.toml_filename)

        res = self.toml_serializer.load(self.toml_filename)

        for i in range(-5, 5):
            self.assertEqual(res(i), abs(i))

    def test_Butoma_function(self):
        """
        Testing serialization with function from other package inside
        """

        """JSON test"""

        self.json_serializer.dump(
            objects_for_testing.Butoma_function,
            self.json_filename
        )

        res = self.json_serializer.load(self.json_filename)

        for i in range(1, 5):
            self.assertEqual(
                res(i, i + 1),
                objects_for_testing.Butoma_function(i, i + 1)
            )

        """YAML test"""

        self.yaml_serializer.dump(
            objects_for_testing.Butoma_function,
            self.yaml_filename
        )

        res = self.yaml_serializer.load(self.yaml_filename)

        for i in range(1, 5):
            self.assertEqual(
                res(i, i + 1),
                objects_for_testing.Butoma_function(i, i + 1)
            )

        """TOML test"""
        self.toml_serializer.dump(
            objects_for_testing.Butoma_function,
            self.toml_filename
        )

        res = self.toml_serializer.load(self.toml_filename)

        for i in range(1, 5):
            self.assertEqual(
                res(i, i + 1),
                objects_for_testing.Butoma_function(i, i + 1)
            )

    def test_lambda_function(self):
        """Testing serialization of function defined like lambda"""
        func = lambda x, y: x * y

        """JSON test"""

        self.json_serializer.dump(func, self.json_filename)

        res = self.json_serializer.load(self.json_filename)

        for i in range(1, 15):
            self.assertEqual(func(i, i + 5), res(i, i + 5))

        """YAML test"""

        self.yaml_serializer.dump(func, self.yaml_filename)

        res = self.yaml_serializer.load(self.yaml_filename)

        for i in range(1, 15):
            self.assertEqual(func(i, i + 5), res(i, i + 5))

        """TOML test"""

        self.toml_serializer.dump(func, self.toml_filename)

        res = self.toml_serializer.load(self.toml_filename)

        for i in range(1, 15):
            self.assertEqual(func(i, i + 5), res(i, i + 5))

    def test_function_with_closure(self):
        """Testing serialization of closures"""

        """JSON test"""
        self.json_serializer.dump(
            objects_for_testing.func_with_closure,
            self.json_filename)

        res = self.json_serializer.load(self.json_filename)

        for i in range(1, 20):
            self.assertEqual(res(i), objects_for_testing.func_with_closure(i))

        """YAML test"""

        self.yaml_serializer.dump(
            objects_for_testing.func_with_closure,
            self.yaml_filename
        )

        res = self.yaml_serializer.load(self.yaml_filename)

        for i in range(1, 20):
            self.assertEqual(res(i), objects_for_testing.func_with_closure(i))

    def test_class_instance(self):

        processor = objects_for_testing.Processor(2700)
        pc = objects_for_testing.PC(
            'NZXT',
            'H440z',
            43.5,
            2020,
            1500,
            processor
        )

        """JSON test"""
        self.json_serializer.dump(pc, self.json_filename)

        res = self.json_serializer.load(self.json_filename)

        self.assertEqual(res, pc)

        buffer_value = self.json_serializer.dumps(pc)
        res = self.json_serializer.loads(buffer_value)

        self.assertEqual(res, pc)

        """YAML test"""
        self.yaml_serializer.dump(pc, self.yaml_filename)

        res = self.yaml_serializer.load(self.yaml_filename)

        self.assertEqual(res, pc)

        buffer_value = self.yaml_serializer.dumps(pc)
        res = self.yaml_serializer.loads(buffer_value)

        self.assertEqual(res, pc)

        """TOML serializer"""
        self.toml_serializer.dump(pc, self.toml_filename)

        res = self.toml_serializer.load(self.toml_filename)

        self.assertEqual(res, pc)

        buffer_value = self.toml_serializer.dumps(pc)
        res = self.toml_serializer.loads(buffer_value)

        self.assertEqual(res, pc)

    def test_exception(self):
        dict1 = {
            'str1': 1,
            'str2': 2,
            'str3': 3,
            'str4': 4
        }
        with open(self.json_filename, 'w') as file:
            file.write('}')

        self.json_serializer.dump(dict1, self.json_filename, mode='a')

        with self.assertRaises(SystemExit) as context:
            res = self.json_serializer.load(self.json_filename)
            print(res)

            self.assertEqual(context.exception.code, 1)

    def test_primitive_type(self):
        test_dict = {
            'list': [
                1.1,
                2,
                {
                    'str1': 1,
                    'str2': None
                },
                [
                    None,
                    'str3'
                ]
            ],
            'dict': {
                'str1': 1,
                'str2': 2.2,
                'empty_list': list()
            },
            'end_dict': None
        }
        test_list = [
            'first_list',
            [1, 2, 3, 2.24, 'str', None],
            {
                'str1': 1,
                'str2': 2,
                'None': None
            }
        ]

        test_tuple = (
            1,
            'str',
            None,
            list(),
            dict(),
            True
        )

        """JSON test"""

        """dict test"""
        self.json_serializer.dump(test_dict, self.json_filename)

        res = self.json_serializer.load(self.json_filename)

        self.assertEqual(test_dict, res)

        """list test"""
        self.json_serializer.dump(test_list, self.json_filename)

        res = self.json_serializer.load(self.json_filename)

        self.assertEqual(test_list, res)

        """tuple test"""
        self.json_serializer.dump(test_tuple, self.json_filename)

        res = self.json_serializer.load(self.json_filename)

        self.assertEqual(list(test_tuple), res)

        """YAML test"""

        """dict test"""
        self.yaml_serializer.dump(test_dict, self.yaml_filename)

        res = self.yaml_serializer.load(self.yaml_filename)

        self.assertEqual(test_dict, res)

        """list test"""
        self.yaml_serializer.dump(test_list, self.yaml_filename)

        res = self.yaml_serializer.load(self.yaml_filename)

        self.assertEqual(test_list, res)

        """tuple test"""
        self.yaml_serializer.dump(test_tuple, self.yaml_filename)

        res = self.yaml_serializer.load(self.yaml_filename)

        self.assertEqual(list(test_tuple), res)


if __name__ == '__main__':
    main()

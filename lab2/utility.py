import argparse
import os


from parser.factory.factory import SerializerFactory, SerializerTypes

parser = argparse.ArgumentParser()

parser.add_argument(
    '-f',
    '--filepath',
    type=str,
    required=True,
    help='absolute or relative path to the file with the serialized object'
)
parser.add_argument(
    '-m',
    '--mode',
    type=str,
    choices=[
        'json',
        'yaml',
        'toml'
    ],
    help='the format to be serialized to'
)

args = parser.parse_args()


if __name__ == '__main__':

    if os.path.exists(args.file):

        filename, file_extension = os.path.splitext(args.file)
        if file_extension == '.json' \
                and args.mode == 'json':
            print('the file is already in json format')

            raise SystemExit(0)

        if file_extension == '.yaml' \
                and args.mode == 'yaml':
            print('the file is already in yaml format')

            raise SystemExit(0)

        if file_extension == '.toml' \
                and args.mode == 'toml':
            print('the file is already in toml format')

            raise SystemExit(0)

        if file_extension == '.json':
            json = SerializerFactory.create_serializer(SerializerTypes.json)

            # with open(args.file, 'r') as file:
            buffer_value = json.load(args.file)

            new_filename = ''
            if args.mode == 'yaml':
                new_filename = filename + '.yaml'

            elif args.mode == 'toml':
                new_filename = filename + '.toml'

            os.rename(args.file, new_filename)

            # with open(new_filename, 'w') as file:

            if args.mode == 'yaml':
                yaml = SerializerFactory.create_serializer(SerializerTypes.yaml)
                yaml.dump(buffer_value, new_filename)

            elif args.mode == 'toml':
                toml = SerializerFactory.create_serializer(SerializerTypes.toml)
                toml.dump(buffer_value, new_filename)

        elif file_extension == '.yaml':
            yaml = SerializerFactory.create_serializer(SerializerTypes.yaml)

            # with open(args.file, 'r') as file:
            buffer_value = yaml.load(args.file)

            new_filename = ''
            if args.mode == 'json':
                new_filename = filename + '.json'

            elif args.mode == 'toml':
                new_filename = filename + '.toml'

            os.rename(args.file, new_filename)

            # with open(new_filename, 'w') as file:

            if args.mode == 'json':
                json = SerializerFactory.create_serializer(SerializerTypes.json)
                json.dump(buffer_value, new_filename)

            elif args.mode == 'toml':
                toml = SerializerFactory.create_serializer(SerializerTypes.toml)
                toml.dump(buffer_value, new_filename)

        elif file_extension == '.toml':
            toml = SerializerFactory.create_serializer(SerializerTypes.toml)

            # with open(args.file, 'rb') as file:
            buffer_value = toml.load(args.file)

            new_filename = ''
            if args.mode == 'json':
                new_filename = filename + '.json'

            elif args.mode == 'yaml':
                new_filename = filename + '.yaml'

            os.rename(args.file, new_filename)

            # with open(new_filename, 'w') as file:

            if args.mode == 'json':
                json = SerializerFactory.create_serializer(SerializerTypes.json)
                json.dump(buffer_value, new_filename)

            elif args.mode == 'yaml':
                yaml = SerializerFactory.create_serializer(SerializerTypes.yaml)
                yaml.dump(buffer_value, new_filename)

    else:
        print('File does not exist')

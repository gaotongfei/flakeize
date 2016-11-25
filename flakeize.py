import yapf
import sys
import click
import os


@click.group()
def cli():
    pass


@click.command()
@click.option('--directory', '-d', help='target directory name')
def check(directory):
    file_paths = []
    exclude = ['migrations']

    for root, directories, files in os.walk(directory):
        directories[:] = [d for d in directories if d not in exclude]
        for filename in files:
            if filename.endswith('.py'):
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)

    for file_path in file_paths:

        with open(file_path, 'r') as f:
            target_content = f.read()

        formatted_code = yapf.yapf_api.FormatCode(target_content)

        with open(file_path, 'w+') as w_f:
            w_f.write(formatted_code[0])

cli.add_command(check)

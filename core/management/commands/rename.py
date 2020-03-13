import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Renames a Django project'

    def add_arguments(self, parser):
        parser.add_argument('old_project_name', type=str, help='The old Django project name')
        parser.add_argument('new_project_name', type=str, help='The new Django project name')

    def handle(self, *args, **kwargs):
        old_project_name = kwargs['old_project_name']
        new_project_name = kwargs['new_project_name']
        files_to_rename = [f'{old_project_name}/settings/base.py', f'{old_project_name}/wsgi.py', f'{old_project_name}/asgi.py', 'manage.py']
        folder_to_rename = f'{old_project_name}'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()
            filedata = filedata.replace(f'{old_project_name}', new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS(f'Project has been renamed to {new_project_name}'))

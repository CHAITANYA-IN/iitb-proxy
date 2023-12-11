#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sso.settings")

    from django.core.management import execute_from_command_line
    # for i, j in os.environ.items():
    #     print(f"{i} = {j}")
    execute_from_command_line(sys.argv)

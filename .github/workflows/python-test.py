import os

print(f"::error file={os.environ.get('file')},line={os.environ.get('line')}:: Error mate")
exit(1)
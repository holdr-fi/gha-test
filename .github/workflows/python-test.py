import os

print(f"::error file={__file__},line={os.environ.get('line')}:: Error mate")
exit(1)
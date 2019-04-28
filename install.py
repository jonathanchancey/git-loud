
import os

coruhook = "pre-commit"

# TODO change to real names
src = "../.git/hooks/pre-commit"
dst = "../.git/hooks/pre-commit.old"


# checks if user already has pre-commit hook and backs up old version
exists = os.path.isfile(src)

if exists:
    print("Renaming old hook {} as to {}".format(src,dst))
    os.rename(src, dst)

print("Creating file {}".format(coruhook))
os.rename(coruhook, src)

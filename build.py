from conan.packager import ConanMultiPackager
from platform import system

if __name__ == "__main__":
    builder = ConanMultiPackager(
        username="xwvvvvwx"
    )

    builder.add_common_builds(pure_c=False)
    builder.run()

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='janus-highvar',
      version='0.0.1',
      description='Dungeons and Dragons High Variance Die Roller',
      author='Alex Philpott',
      url='https://github.com/alexphi314/janus',
      packages=find_packages(),
      entry_points={
            "console_scripts": [
                  "janus = janus.main:roll_die"
            ]
      },
      extras_require={":python_version<'3.3'": ["mock"]},
      )

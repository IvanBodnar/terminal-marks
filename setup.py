from setuptools import setup, find_packages

setup(
    name='python-template',
    version='0.1',
    install_requires=[
            'click',
        ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points='''
        [console_scripts]
        run=terminal_marks.cli.cli:run
    ''',
)

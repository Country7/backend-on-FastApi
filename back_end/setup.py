from setuptools import setup

setup(
    name='app-Personnel_Report-back_end',
    version='0.0.1',
    author='Vadim',
    author_email='vadim-vvs@gmail.com',
    description='FastApi app',
    install_requires=[
        'fastapi',
        'uvicorn',
        'SQLAlchemy',
        'pytest',
        'requests',
    ],
    scripts=[
        'app/main.py',
        'scripts/create_db.py'
    ]
)

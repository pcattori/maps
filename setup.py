from setuptools import setup

setup(
    name='maps',
    version='5.0.0',
    description='Maps: flavors of Python dictionaries',
    url='https://github.com/pcattori/maps',
    author='Pedro Cattori',
    author_email='pcattori@gmail.com',
    license='MIT',
    packages=['maps'],
    test_suite='tests',
    extras_require={'dev': ['codecov==2.0.5', 'sphinx==1.5.1']},
    keywords = ['maps', 'namddict', 'frozendict', 'fixedkey', 'fixeddict'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6']
)

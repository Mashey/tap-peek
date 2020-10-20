from setuptools import setup

setup(
    name="tap-peek",
    version="0.1.0",
    description="Singer.io tap for extracting data from the Peek API",
    author="Michael Cooper and Jordan Williams",
    url="https://www.peek.com/pro/",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_peek"],
    install_requires=[
        "singer-python==5.9.0",
        "requests"
    ],
    entry_points="""
    [console_scripts]
    tap-peek=tap_peek:main
    """,
    packages=["tap_peek"],
    package_data = {
        "schemas": ["tap_peek/schemas/*.json"]
    },
    include_package_data=True,
)
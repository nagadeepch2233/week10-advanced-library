from setuptools import setup, find_packages

setup(
    name="my_advanced_lib",
    version="0.1.0",
    description="Advanced Python library demonstrating decorators, generators, context managers, and metaclasses",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "requests>=2.31",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "flake8>=6.0",
            "black>=23.0",
            "mypy>=1.5",
            "isort>=6.0",
            "sphinx>=7.0",
            "hypothesis>=6.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "my-advanced-lib=src.my_advanced_lib.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

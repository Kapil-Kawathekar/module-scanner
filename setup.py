import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="module-scan",
    version="0.0.2",
    author="Rajesh Gopinathapai",
    author_email="mgrajesh@hotmail.com",
    description="Repository scanner for module imports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cetcs92/module-scanner",
    project_urls={
        "Bug Tracker": "https://github.com/cetcs92/module-scanner/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywrods='BOM, SBOM, import, module, scan',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'module-scan = module_scan.scan:main'
        ]
    },
)

from setuptools import setup, find_packages

setup(
    name="agent-os",
    version="0.1.0",
    author="Your Name",
    description="Canonical naming and discovery system for AI agents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/agent-os",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pyyaml>=6.0",
    ],
)

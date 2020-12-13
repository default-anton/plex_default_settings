from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='plex_default_settings',
    version='0.1.3',
    author='Anton Kuzmenko',
    author_email='hotk@hey.com',
    description='Plex default settings',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/antonlabs/plex_default_settings',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Video :: Display',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='plex, subtitles, dubbing, subs, dubs',
    packages=find_packages(),
    python_requires='>=3.8, <4',
    install_requires=[
        'plexapi==4.2.0',
        'typer==0.3.2',
    ],
    tests_require=[],
    entry_points={
        'console_scripts': [
            'plex_default_settings=plex_default_settings.main:app',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/antonlabs/plex_default_settings/issues',
        'Source': 'https://github.com/antonlabs/plex_default_settings',
    },
)

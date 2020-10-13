import setuptools
import versioneer

NAME = 'demo'

setuptools.setup(
    name=NAME,
    version='0.0.1',
    cmdclass=versioneer.get_cmdclass(),
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'demo = demo.workflow:demo_workflow'
        ],
    },
)


Publish sf-elastic-apm pip package
==============
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![pypi-package](https://img.shields.io/badge/pypi-green)](https://pypi.org/project/sf-elastic-apm/)

Build Info
---------

- Before publishing update package version in [in elasticapm/version.py ](#) file located in root folder of application.

- There are two ways to build package: Automatic and Manual.

- Automatic build will be trigger when new github release is created.

Manual Steps
--------------


- Open [SF-ELASTIC-APM Github Repo](https://github.com/snappyflow/sftrace-python-agent)

- Go to [Actions](https://github.com/snappyflow/sftrace-python-agent/actions) tab and select <b>Build and publish Python 🐍 distributions 📦 to PyPI</b> or <b>Build and publish Python 🐍 distributions 📦 to TestPyPI</b> action and click on <i>Run workflow</i>

- Select the desired branch e.g <i>main</i> or <i>master</i> branch and finally click on <b> Run workflow</b> button.<br>
Above process will start building and then publishing your package. 

- Once build result of workflow is successful, Check published version of pip package in pypi or test.pypi repo based on selected action.


<br>
<i>Note: Please make sure package version is updated to newer version before publishing. </i>
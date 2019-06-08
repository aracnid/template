# How to Setup Documents

## Setup Procedure

This procedure describes how to setup documentation. The project name, `TEMPLATE`, used in this procedure is a placehold and should be replaced. (Capitalization of `TEMPLATE` is only used for emphasis.)

### 1. Setup project repository on GitHub

After the project's initial commit, push the project to GitHub. 

```bash
$ git remote add origin https://github.com/<profile>/TEMPLATE.git
$ git push origin master
```

### 1. Setup Sphinx within project repository

From the project repository:

```bash
$ mkdir docs
$ cd docs
$ sphinx-quickstart # accept the defaults
```

### 2. Setup separate "-docs" repository

Clone the project repository from GitHub to create the docs repository. The docs directory should be at the same level as the project directory. Note that the root directory of the docs repository will actually be one level down in the `TEMPLATE-docs/html` directory.

```bash
$ # change to the appropriate parent directory
$ mkdir TEMPLATE-docs
$ cd TEMPLATE-docs
$ git clone https://github.com/<profile>/TEMPLATE.git html
$ git branch gh-pages
$ git symbolic-ref HEAD refs/head/gh-pages
$ rm .git/index
$ git clean -fdx
```

### 3. Update `Makefile`

Update `Makefile` to set the build directory to the path of the new docs directory.

```make
BUILDDIR = ../../TEMPLATE-docs
```

### 4. Update `index.rst`

The root directory of the project repository should have a `README.rst` file. Update the `docs/index.rst` file to include `README.rst` into the main documentation.

```rst
.. include:: ../../README.rst
```

### 5. Create initial documentation

Commit all the code in the project repository. Then create the documentation and push it to the `gh-pages` branch.

```bash
$ # change to the project repository directory
$ git commit -am "setup initial docs"
$ cd docs
$ make html
$ # change to the TEMPLATE-docs/html directory
$ git commit -am "rebuild docs"
$ git push origin gh-pages
```

### 6. Add a `.nojekyll` file

Add a `.nojekyll` file to the docs repository. This signals to GitHub Pages to bypass Jekyll processing and ignore Sphinx-generated pages.

```bash
$ # change to the TEMPLATE-docs/html directory
$ touch .nojekyll
$ git commit -am "add .nojekyll"
```

## Workflow

* From the project repository:
	- Commit changes
	- Push changes to remote, if necessary
	- Change to the `docs` directory
	- Run `make html` to generate the html docs into the docs repository

* From the docs repository:
	- Change to the `html` directory
	- Make sure the active branch is "gh-pages"
	- Commit changes: `$ git commit -am "rebuild docs"`
	- Push changes to GitHub Pages: `$ git push origin gh-pages`

```bash
$ # change to the project repository directory
$ git commit -am "add comment message"
$ git push # if necessary
$ cd docs
$ make html
$ cd ../../TEMPLATE-docs/html # change to the docs repository
$ # make sure the active branch is "gh-pages"
$ git commit -am "rebuild docs"
$ git push origin gh-pages
```

## Directory Structure

The final directory structure looks like the following. Files and directories not related to documentation are not shown.

```
TEMPLATE/              # project repository
├── TEMPLATE/          # main python package
│   ├── __init__.py    # python module package file
│   └── app.py         # main application program
├── docs/              # documentation source directory
│   ├── conf.py        # Sphinx configuration file
│   ├── index.rst      # master document
│   ├── make.bat       # batch file to build documentation
│   └── Makefile       # contains build directives
└── README.rst         # project repository readme file
```

%global srcname ipython_genutils

Name:           python-%srcname
Version:        0.2.0
Release:        4
Summary:        A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions
Group:          Development/Python
License:        BSD
URL:            https://github.com/ipython/%srcname
Source0:        http://pypi.python.org/packages/source/i/%srcname/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	graphviz

BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)

Obsoletes:	python2-%{srcname} < %{EVRD}

%description
This package is a stop-gap that contains some common utilities shared by
Jupyter and IPython projects during The Big Split™. As soon as possible,
those packages will remove their dependency on this, and this repo will go
away.

No functionality should be added to this repository, and no packages outside
IPython/Jupyter should depend on it.

%files
%doc README.md CONTRIBUTING.md COPYING.md
%{python_sitelib}/*.egg-info
%{python_sitelib}/%srcname

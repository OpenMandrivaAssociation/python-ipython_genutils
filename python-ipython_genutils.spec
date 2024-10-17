%global srcname ipython_genutils

Name:           python-%srcname
Version:        0.2.0
Release:        2
Summary:        A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions
Group:          Development/Python
License:        BSD
URL:            https://github.com/ipython/%srcname
Source0:        http://pypi.python.org/packages/source/i/%srcname/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	graphviz

BuildRequires:	python-setuptools
BuildRequires:	python-devel

BuildRequires:	python2-setuptools
BuildRequires:	python2-devel

%description
This package is a stop-gap that contains some common utilities shared by
Jupyter and IPython projects during The Big Split™. As soon as possible,
those packages will remove their dependency on this, and this repo will go
away.

No functionality should be added to this repository, and no packages outside
IPython/Jupyter should depend on it.

%package -n python2-%srcname
Summary:        A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions

%description -n python2-%srcname
This package is a stop-gap that contains some common utilities shared by
Jupyter and IPython projects during The Big Split™. As soon as possible,
those packages will remove their dependency on this, and this repo will go
away.


%prep
%setup -q -n %{srcname}-%{version}

%autopatch -p1

cp -a . %py2dir

%build
%{__python} setup.py build

pushd %py2dir
%{__python2} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

pushd %py2dir
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.md CONTRIBUTING.md COPYING.md
%{python_sitelib}/*.egg-info
%{python_sitelib}/%srcname

%files -n python2-%srcname
%doc README.md CONTRIBUTING.md COPYING.md
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/%srcname


# Conditional build:
%bcond_without	tests	# unit tests

%define		module	expandvars
Summary:	Expand system variables Unix style
Name:		python3-%{module}
Version:	0.12.0
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	8091f578a547e2b4b9df59100a179266
URL:		https://pypi.org/project/expandvars/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
%if %{with tests}
#BuildRequires:	python3-
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
# replace with other requires if defined in setup.py
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is inspired by GNU bash's variable expansion features. It
can be used as an alternative to Python's os.path.expandvars function.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CODE_OF_CONDUCT.md README.md
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}*.py*
%{py3_sitescriptdir}/%{module}-%{version}.dist-info

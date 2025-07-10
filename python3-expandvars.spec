#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	expandvars
Summary:	Expand system variables Unix style
Summary(pl.UTF-8):	Rozwijanie zmiennych systemowych w stylu Uniksa
Name:		python3-%{module}
Version:	1.0.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/expandvars/
Source0:	https://files.pythonhosted.org/packages/source/e/expandvars/%{module}-%{version}.tar.gz
# Source0-md5:	8f36c472b29b8c83a1585dd53b4ed0d1
URL:		https://pypi.org/project/expandvars/
BuildRequires:	python3-build
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is inspired by GNU bash's variable expansion features. It
can be used as an alternative to Python's os.path.expandvars function.

%description -l pl.UTF-8
Ten moduł jest inspirowany funkcjonalnością rozwijania zmiennych GNU
basha. Może być alternatywą dla funkcji Pythona os.path.expandvars.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/expandvars.py
%{py3_sitescriptdir}/__pycache__/expandvars.cpython-*.py[co]
%{py3_sitescriptdir}/%{module}-%{version}.dist-info

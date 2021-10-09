Name:		python3-augeas
Version:	1.1.0
Release:	1%{?dist}
Summary:	Python 3 bindings to augeas
License:	LGPLv2+
URL:		https://augeas.net/
Source0:	https://github.com/hercules-team/python-augeas/archive/v%{version}/python-augeas-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
BuildRequires:	augeas
BuildRequires:	python3-pytest
BuildRequires:	python3-cffi

Requires:	augeas-libs
Requires:	python3-cffi
%{?python_provide:%python_provide python3-augeas}

%description
python3-augeas is a set of Python bindings around augeas.

%prep
%autosetup -n python-augeas-%{version} -p1

%build
%{py3_build}

%install
%{py3_install}

%check
pytest-3

%files -n python3-augeas
%license COPYING
%doc AUTHORS README.txt
%{python3_sitelib}/augeas.py
%{python3_sitelib}/augeas/*
%{python3_sitelib}/python_augeas-*.egg-info
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/test/*


%changelog
* Sun Oct 10 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.0-1
- initial package based on Fedora's spec file


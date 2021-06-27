%global pypi_name dns-lexicon
%global modname lexicon

# tests can not be run on Fedora's infrastructure as some tests need additional
# dependencies which are not present in EPEL.
# Packagers can run the test suite manually though:
#   fedpkg mockbuild --enable-network --with tests
%bcond_with tests

%bcond_without python2
%bcond_without python2_extras

# EPEL8 is currently missing dependencies used by the extras metapackages
# EPEL7: no Python 3 package for "boto3" yet (also we might want to limit the
# packaged extras to reduce maintenance complexity)
%bcond_with python3_extras

%global py3_prefix python%{python3_pkgversion}

Name:           python-%{pypi_name}
Version:        3.3.28
Release:        1%{?dist}
Summary:        Manipulate DNS records on various DNS providers in a standardized/agnostic way

License:        MIT
URL:            https://github.com/AnalogJ/lexicon
# pypi releases don't contain necessary data to run the tests
Source0:        https://github.com/AnalogJ/lexicon/archive/v%{version}/lexicon-%{version}.tar.gz
BuildArch:      noarch

Patch0:         0000-remove-shebang.patch
Patch1:         0001-fix-requirements.patch

%if %{with python2}
BuildRequires:  python-beautifulsoup4
# do not install python-boto3 as vcr will try to patch botocore then
# (but EPEL's botocore is too old to be patched)
#BuildRequires:  python-boto3
BuildRequires:  python2-devel
# EL7 doesn't have a current enough version of python2-dns
BuildRequires:  python2-setuptools
BuildRequires:  python2-cryptography
BuildRequires:  python2-future
BuildRequires:  python2-pyyaml
BuildRequires:  python2-tldextract
BuildRequires:  python-virtualenv
BuildRequires:  python-xmltodict
# EL7 has an unversioned name for this package
BuildRequires:  pyOpenSSL
# }}}
%endif

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_prefix}-beautifulsoup4
BuildRequires:  %{py3_prefix}-cryptography
BuildRequires:  python3-dns >= 1.15.0
BuildRequires:  python3-future
BuildRequires:  %{py3_prefix}-pyOpenSSL
BuildRequires:  %{py3_prefix}-tldextract
BuildRequires:  %{py3_prefix}-PyYAML
BuildRequires:  %{py3_prefix}-xmltodict

# Extras requirements
# {{{
%if %{with python3_extras}
BuildRequires:  python3-boto3
%endif
# }}}

%description
Lexicon provides a way to manipulate DNS records on multiple DNS providers in a
standardized way. Lexicon has a CLI but it can also be used as a python
library.

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-cryptography
Requires:       python2-future
Requires:       python2-requests
Requires:       python2-setuptools
Requires:       python2-pyyaml
Requires:       python2-tldextract
# EL7 has an unversioned name for this package
Requires:       pyOpenSSL

# Both packages install a Python module named lexicon
# TODO: Remove this once resolved upstream (see upstream #222)
Conflicts:      python-lexicon

%description -n python2-%{pypi_name}
Lexicon provides a way to manipulate DNS records on multiple DNS providers in a
standardized way. Lexicon has a CLI but it can also be used as a python
library.

This is the Python 2 version of the package.


# Extras meta-packages (Python 2)
# {{{
%if %{with python2_extras}
%package -n     python2-%{pypi_name}+easyname
Summary:        Meta-package for python2-%{pypi_name} and easyname provider
%{?python_provide:%python_provide python2-%{pypi_name}+easyname}

Requires:       python2-%{pypi_name} = %{version}-%{release}
# EL7 has an unversioned name for this package
Requires:       python-beautifulsoup4

%description -n python2-%{pypi_name}+easyname
This package installs no files. It requires python2-%{pypi_name} and all
dependencies necessary to use the easyname provider.


%package -n     python2-%{pypi_name}+gratisdns
Summary:        Meta-package for python2-%{pypi_name} and gratisdns provider
%{?python_provide:%python_provide python2-%{pypi_name}+gratisdns}

Requires:       python2-%{pypi_name} = %{version}-%{release}
# EL7 has an unversioned name for this package
Requires:       python-beautifulsoup4

%description -n python2-%{pypi_name}+gratisdns
This package installs no files. It requires python2-%{pypi_name} and all
dependencies necessary to use the gratisdns provider.


%package -n     python2-%{pypi_name}+henet
Summary:        Meta-package for python2-%{pypi_name} and Hurricane Electric provider
%{?python_provide:%python_provide python2-%{pypi_name}+henet}

Requires:       python2-%{pypi_name} = %{version}-%{release}
# EL7 has an unversioned name for this package
Requires:       python-beautifulsoup4

%description -n python2-%{pypi_name}+henet
This package installs no files. It requires python2-%{pypi_name} and all
dependencies necessary to use the Hurricane Electric provider.


%package -n     python2-%{pypi_name}+plesk
Summary:        Meta-package for python2-%{pypi_name} and Plesk provider
%{?python_provide:%python_provide python2-%{pypi_name}+plesk}

Requires:       python2-%{pypi_name} = %{version}-%{release}
# EL7 has an unversioned name for this package
Requires:       python-xmltodict

%description -n python2-%{pypi_name}+plesk
This package installs no files. It requires python2-%{pypi_name} and all
dependencies necessary to use the Plesk provider.


%package -n     python2-%{pypi_name}+route53
Summary:        Meta-package for python2-%{pypi_name} and Route 53 provider
%{?python_provide:%python_provide python2-%{pypi_name}+route53}

Requires:       python2-%{pypi_name} = %{version}-%{release}
# EL7 has an unversioned name for this package
Requires:       python-boto3

%description -n python2-%{pypi_name}+route53
This package installs no files. It requires python2-%{pypi_name} and all
dependencies necessary to use the Route 53 provider.

%endif
# }}}
%endif




%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       %{py3_prefix}-cryptography
Requires:       python3-future
Requires:       python3-requests
Requires:       python3-setuptools
Requires:       %{py3_prefix}-pyOpenSSL
Requires:       %{py3_prefix}-tldextract
Requires:       %{py3_prefix}-PyYAML

# Both packages install a Python module named lexicon
# TODO: Remove this once resolved upstream (see upstream #222)
Conflicts:      python3-lexicon

%description -n python3-%{pypi_name}
Lexicon provides a way to manipulate DNS records on multiple DNS providers in a
standardized way. Lexicon has a CLI but it can also be used as a python
library.

This is the Python 3 version of the package.


# Extras meta-packages (Python 3)
# {{{
%if %{with python3_extras}
%package -n     python3-%{pypi_name}+easyname
Summary:        Meta-package for python3-%{pypi_name} and easyname provider
%{?python_provide:%python_provide python3-%{pypi_name}+easyname}

Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       %{py3_prefix}-beautifulsoup4

%description -n python3-%{pypi_name}+easyname
This package installs no files. It requires python3-%{pypi_name} and all
dependencies necessary to use the easyname provider.


%package -n     python3-%{pypi_name}+gratisdns
Summary:        Meta-package for python3-%{pypi_name} and gratisdns provider
%{?python_provide:%python_provide python3-%{pypi_name}+gratisdns}

Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       %{py3_prefix}-beautifulsoup4

%description -n python3-%{pypi_name}+gratisdns
This package installs no files. It requires python3-%{pypi_name} and all
dependencies necessary to use the gratisdns provider.


%package -n     python3-%{pypi_name}+henet
Summary:        Meta-package for python3-%{pypi_name} and Hurricane Electric provider
%{?python_provide:%python_provide python3-%{pypi_name}+henet}

Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       %{py3_prefix}-beautifulsoup4

%description -n python3-%{pypi_name}+henet
This package installs no files. It requires python3-%{pypi_name} and all
dependencies necessary to use the Hurricane Electric provider.


%package -n     python3-%{pypi_name}+plesk
Summary:        Meta-package for python3-%{pypi_name} and Plesk provider
%{?python_provide:%python_provide python3-%{pypi_name}+plesk}

Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       %{py3_prefix}-xmltodict

%description -n python3-%{pypi_name}+plesk
This package installs no files. It requires python3-%{pypi_name} and all
dependencies necessary to use the Plesk provider.


%package -n     python3-%{pypi_name}+route53
Summary:        Meta-package for python3-%{pypi_name} and Route 53 provider
%{?python_provide:%python_provide python3-%{pypi_name}+route53}

Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       python3-boto3

%description -n python3-%{pypi_name}+route53
This package installs no files. It requires python3-%{pypi_name} and all
dependencies necessary to use the Route 53 provider.
%endif
# }}}



%prep
%autosetup -n %{modname}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%py2_build
%endif

%py3_build


%if %{with tests}
# We can not run the test suite on EPEL 7 when using Fedora's infrastructure:
# - no python3-vcrpy (and hence no python3-pytest-vcr) in EPEL 7
# - pytest-vcr requires pytest >= 3.0 even for the oldest public version but
#   EPEL 7 ships pytest 2.7.0 (Python 2) / 2.9.2 (Python 3.6)
# - dns-lexicon requires mock >= 3.0 but EPEL 7 ships python36-mock 2.0.0-2.el7
# - python-vcr does not work for requests < 2.16.0
#
# Also the upstream tarballs don't include required vcr fixture files
# ("cassettes") though that could be fixed by using a different tarball.
%check
# lexicon providers which do not work due to missing dependencies:
# - TransipProviderTests
# - SoftLayerProviderTests
# - NamecheapProviderTests
# - NamecheapManagedProviderTests
# - GransyProviderTests
# - LocalzoneProviderTests
TEST_SELECTOR="not AutoProviderTests and not GoDaddyProviderTests and not TransipProviderTests and not SoftLayerProviderTests and not NamecheapProviderTests and not NamecheapManagedProviderTests and not GransyProviderTests and not LocalzoneProviderTests"
%if %{with python2}
/usr/bin/virtualenv --system-site-packages venv.py2
# dnspython 2.0 dropped Python 2 support
./venv.py2/bin/pip install pytest pytest-vcr 'mock >= 3.0' 'requests == 2.16' 'dnspython < 2'
# - Route53ProviderTests needs boto3
# - python-vcr tries to patch botocore if boto3 is installed but only works for
#   botocore >= 1.11.0 (EPEL 7 currently has python2-botocore 1.6.0)
PY2_TEST_SELECTOR="${TEST_SELECTOR} and not Route53ProviderTests"
./venv.py2/bin/pytest -v -k "${PY2_TEST_SELECTOR}" lexicon
%endif

%if %{with python3}
%{python3} -m venv --system-site-packages venv.py3
./venv.py3/bin/pip install pytest pytest-vcr 'mock >= 3.0' 'requests == 2.16'
# TODO: Route53ProviderTests needs boto3
TEST_SELECTOR="${TEST_SELECTOR} and not Route53ProviderTests"
./venv.py3/bin/pytest -v -k "${TEST_SELECTOR}" lexicon
%endif
%endif


%install
%if %{with python2}
%py2_install
install -pm 0755 %{buildroot}/%{_bindir}/lexicon %{buildroot}/%{_bindir}/lexicon-%{python2_version}
ln -s %{_bindir}/lexicon-%{python2_version} %{buildroot}/%{_bindir}/lexicon-2
%endif

%py3_install
install -pm 0755 %{buildroot}/%{_bindir}/lexicon %{buildroot}/%{_bindir}/lexicon-%{python3_version}
ln -s %{_bindir}/lexicon-%{python3_version} %{buildroot}/%{_bindir}/lexicon-3

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/lexicon-2
%{_bindir}/lexicon-%{python2_version}
%{python2_sitelib}/%{modname}
%{python2_sitelib}/dns_lexicon-%{version}-py?.?.egg-info

# Extras meta-packages
# {{{
%files -n python2-%{pypi_name}+easyname
%files -n python2-%{pypi_name}+gratisdns
%files -n python2-%{pypi_name}+henet
%files -n python2-%{pypi_name}+plesk
%files -n python2-%{pypi_name}+route53
# }}}
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/lexicon
%{_bindir}/lexicon-3
%{_bindir}/lexicon-%{python3_version}
%{python3_sitelib}/%{modname}
%{python3_sitelib}/dns_lexicon-%{version}-py?.?.egg-info

# Extras meta-packages
# {{{
%if %{with python3_extras}
%files -n python3-%{pypi_name}+easyname
%files -n python3-%{pypi_name}+gratisdns
%files -n python3-%{pypi_name}+henet
%files -n python3-%{pypi_name}+plesk
%files -n python3-%{pypi_name}+route53
%endif
# }}}

%changelog
* Sun Jun 27 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 3.3.28-1
- update to 3.3.28

* Sun May 16 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 3.3.17-4
- rebuilt

* Sun May 16 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 3.3.17-3
- enable Python 3 subpackage for EPEL 7

* Wed Mar 04 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 3.3.17-2
- add missing sources

* Tue Mar 03 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 3.3.17-1
- Update to 3.3.17 (#1764339)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Eli Young <elyscape@gmail.com> - 3.3.4-2
- Rebuild due to Koji issues

* Mon Oct 07 2019 Eli Young <elyscape@gmail.com> - 3.3.4-1
- Update to 3.3.4 (#1725208)
- Support EPEL8 builds

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.8-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Eli Young <elyscape@gmail.com> - 3.2.8-1
- Update to 3.2.8 (#1722190)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 3.2.6-1
- Update to 3.2.6 (#1685778)

* Fri Feb 15 2019 Eli Young <elyscape@gmail.com> - 3.1.5-1
- Update to 3.1.5 (#1671162)
- Add meta-subpackages for specific providers

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 14 2018 Eli Young <elyscape@gmail.com> - 3.0.6-1
- Update to 3.0.6
- Declare conflict with python-lexicon
- Remove Python 2 package in Fedora 30+

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 3.0.2-2
- Fix dependencies on Fedora 28

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Mon Oct 08 2018 Eli Young <elyscape@gmail.com> - 2.7.9-1
- Update to 2.7.9 (#1637142)

* Mon Aug 27 2018 Eli Young <elyscape@gmail.com> - 2.7.0-2
- Add dependency on python-cryptography (#1622418)

* Mon Jul 23 2018 Nick Bebout <nb@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Eli Young <elyscape@gmail.com> - 2.4.5-1
- Update to 2.4.5 (#1599479)

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.4-3
- Rebuilt for Python 3.7

* Tue Jun 26 2018 Eli Young <elyscape@gmail.com> - 2.4.4-2
- Remove unnecessary shebang

* Tue Jun 26 2018 Eli Young <elyscape@gmail.com> - 2.4.4-1
- Update to 2.4.4 (#1594777)

* Tue Jun 19 2018 Eli Young <elyscape@gmail.com> - 2.4.3-1
- Update to 2.4.3 (#1592158)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Eli Young <elyscape@gmail.com> - 2.4.0-1
- Update to 2.4.0 (#1589596)

* Tue May 29 2018 Eli Young <elyscape@gmail.com> - 2.3.0-1
- Update to 2.3.0 (#1582799)

* Mon May 07 2018 Eli Young <elyscape@gmail.com> - 2.2.3-1
- Update to 2.2.3 (#1575598)

* Thu May 03 2018 Eli Young <elyscape@gmail.com> - 2.2.2-1
- Update to 2.2.2 (#1574265)

* Sat Mar 24 2018 Eli Young <elyscape@gmail.com> - 2.2.1-1
- Update to 2.2.1
- Use Python 3 by default when available

* Mon Feb 19 2018 Nick Bebout <nb@fedoraproject.org> - 2.1.19-1
- Initial package.

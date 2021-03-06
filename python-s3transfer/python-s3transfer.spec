
%global pypi_name s3transfer
%global py3_prefix python%{python3_pkgversion}

Name:           python-%{pypi_name}
Version:        0.1.10
Release:        2%{?dist}
Summary:        An Amazon S3 Transfer Manager

License:        ASL 2.0
URL:            https://github.com/boto/s3transfer
Source0:        %{pypi_source}
# required to fix a test failure in the functional tests, present in 0.1.11+
Patch1:         %{name}-callbackenablingbody.patch
BuildArch:      noarch

%description
S3transfer is a Python library for managing Amazon S3 transfers.

%package -n     python2-%{pypi_name}
Summary:        An Amazon S3 Transfer Manager
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  python-mock
BuildRequires:  python-wheel
BuildRequires:  python-futures
BuildRequires:  python2-botocore >= 1.3.0, python2-botocore < 2.0.0
BuildRequires:  python-coverage
Requires:       python-futures
Requires:       python2-botocore >= 1.3.0, python2-botocore < 2.0.0
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
S3transfer is a Python library for managing Amazon S3 transfers.

%package -n     python3-%{pypi_name}
Summary:        An Amazon S3 Transfer Manager
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_prefix}-nose
BuildRequires:  %{py3_prefix}-mock
BuildRequires:  python3-wheel
BuildRequires:  python3-botocore >= 1.3.0, python3-botocore < 2.0.0
BuildRequires:  %{py3_prefix}-coverage
Requires:       python3-botocore >= 1.3.0, python3-botocore < 2.0.0
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
S3transfer is a Python library for managing Amazon S3 transfers.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove online tests (see https://github.com/boto/s3transfer/issues/8)
rm -rf tests/integration

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
nosetests-%{python2_version} --with-coverage --cover-erase --cover-package s3transfer --with-xunit --cover-xml -v tests/unit/ tests/functional/
nosetests-%{python3_version} --with-coverage --cover-erase --cover-package s3transfer --with-xunit --cover-xml -v tests/unit/ tests/functional/

%files -n python2-%{pypi_name} 
%doc README.rst
%license LICENSE.txt
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name} 
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Oct 13 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 0.1.10-2
- add Python 3 subpackage

* Wed Dec 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 0.1.9-2
- Rebuild for Python 3.6

* Thu Oct 27 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9

* Mon Oct 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.7-1
- Uodate to 0.1.7

* Sun Oct 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Wed Sep 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Wed Sep 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3

* Thu Aug 04 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1

* Tue Aug 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.0-1
- Update to 0.1.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 24 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.0.1-3
- Cleanup the spec a little bit
- Remove patch

* Tue Feb 23 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.0.1-2
- Add patch to remove tests needing web connection

* Tue Feb 23 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.0.1-1
- Initial package.

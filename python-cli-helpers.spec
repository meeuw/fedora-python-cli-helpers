%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

# python2-backports-csv not in Fedora yet, disable Python 2 version 
%global with_python2 0

%global pypi_name cli_helpers

Summary:        Python helpers for common CLI tasks
Name:           python-cli-helpers
Version:        0.2.3
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/dbcli/cli_helpers
Source0:        https://files.pythonhosted.org/packages/source/c/cli_helpers/cli_helpers-%{version}.tar.gz
Patch01:        python-cli-helpers-0.2.3-setup.patch
BuildArch:      noarch
%if 0%{?with_python2}
BuildRequires:  python2-backports-csv
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-terminaltables
BuildRequires:  python2-pytest
%endif
%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-terminaltables
BuildRequires:  python3-pytest
%endif 
%description
CLI Helpers is a Python package that makes it easy to perform common
tasks when building command-line apps. Its a helper library for
command-line interfaces.

%if 0%{?with_python2}
%package -n     python2-cli-helpers
Summary:        %{summary}
%{?python_provide:%python_provide python2-cli-helpers}
%{?el6:Provides: python-cli-helpers}
Requires:       python2-pygments >= 1.6
Requires:       python2-terminaltables >= 3.0.0
%description -n python2-cli-helpers
%{desc}
%endif

%if %{with python3}
%package -n     python3-cli-helpers
Summary:        %{summary}
%{?python_provide:%python_provide python3-cli-helpers}
Requires:       python3-pygments >= 1.6
Requires:       python3-terminaltables >= 3.0.0
%description -n python3-cli-helpers
%{desc}
%endif

%prep
%setup -q -n %{pypi_name}-%{version}
%patch01 -p1
rm -rf %{pypi_name}.egg-info

%build
%if 0%{?with_python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python3}
%py3_install
%endif
%if 0%{?with_python2}
%py2_install
%endif

%check
%if 0%{?with_python2}
PYTHONPATH=build/lib/ py.test-2
%endif
%if %{with python3}
PYTHONPATH=build/lib/ py.test-3
%endif

%if 0%{?with_python2}
%files -n python2-cli-helpers
%license LICENSE
%doc AUTHORS CHANGELOG README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python3-cli-helpers
%license LICENSE
%doc AUTHORS CHANGELOG README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Wed Aug 16 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.2.3-1
- 0.2.3
- Rename
- Use summary and desc macros
- Drop Python 2 sub package for now, backports.csv not available
- Add patch to remove Python 2 specific reqs into Python 3 package

* Mon Jun 26 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.2.0-1
- 0.2.0
- Rename

* Mon May 15 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.1.0-2
- Minor tweaks

* Sat May 13 2017 Dick Marinus <dick@mrns.nl> - 0.1.0-1
- Initial package

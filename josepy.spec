#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4D17C995CD9775F2 (letsencrypt-client@eff.org)
#
Name     : josepy
Version  : 1.10.0
Release  : 35
URL      : https://files.pythonhosted.org/packages/27/21/e228c5931c18882419590d5cb5306f124f7eb653146c7918efe78c81b553/josepy-1.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/27/21/e228c5931c18882419590d5cb5306f124f7eb653146c7918efe78c81b553/josepy-1.10.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/27/21/e228c5931c18882419590d5cb5306f124f7eb653146c7918efe78c81b553/josepy-1.10.0.tar.gz.asc
Summary  : JOSE protocol implementation in Python
Group    : Development/Tools
License  : Apache-2.0
Requires: josepy-bin = %{version}-%{release}
Requires: josepy-license = %{version}-%{release}
Requires: josepy-python = %{version}-%{release}
Requires: josepy-python3 = %{version}-%{release}
Requires: cryptography
Requires: pyOpenSSL
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyOpenSSL
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
JOSE protocol implementation in Python using cryptography
.. image:: https://github.com/certbot/josepy/actions/workflows/check.yaml/badge.svg
:target: https://github.com/certbot/josepy/actions/workflows/check.yaml

%package bin
Summary: bin components for the josepy package.
Group: Binaries
Requires: josepy-license = %{version}-%{release}

%description bin
bin components for the josepy package.


%package license
Summary: license components for the josepy package.
Group: Default

%description license
license components for the josepy package.


%package python
Summary: python components for the josepy package.
Group: Default
Requires: josepy-python3 = %{version}-%{release}

%description python
python components for the josepy package.


%package python3
Summary: python3 components for the josepy package.
Group: Default
Requires: python3-core
Provides: pypi(josepy)
Requires: pypi(cryptography)
Requires: pypi(pyopenssl)
Requires: pypi(setuptools)

%description python3
python3 components for the josepy package.


%prep
%setup -q -n josepy-1.10.0
cd %{_builddir}/josepy-1.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635744364
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/josepy
cp %{_builddir}/josepy-1.10.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/josepy/d095fa0d394cc9417a65aecd0d28e7d10e762f98
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jws

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/josepy/d095fa0d394cc9417a65aecd0d28e7d10e762f98

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

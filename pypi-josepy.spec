#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-josepy
Version  : 1.13.0
Release  : 44
URL      : https://files.pythonhosted.org/packages/f4/be/5c1d9decbd5e9cf97dccd40d13c5657bef936d87da03c9d7aeb67c1b5126/josepy-1.13.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f4/be/5c1d9decbd5e9cf97dccd40d13c5657bef936d87da03c9d7aeb67c1b5126/josepy-1.13.0.tar.gz
Summary  : JOSE protocol implementation in Python
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-josepy-bin = %{version}-%{release}
Requires: pypi-josepy-license = %{version}-%{release}
Requires: pypi-josepy-python = %{version}-%{release}
Requires: pypi-josepy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cryptography)
BuildRequires : pypi(py)
BuildRequires : pypi(pyopenssl)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
JOSE protocol implementation in Python using cryptography
.. image:: https://github.com/certbot/josepy/actions/workflows/check.yaml/badge.svg
:target: https://github.com/certbot/josepy/actions/workflows/check.yaml

%package bin
Summary: bin components for the pypi-josepy package.
Group: Binaries
Requires: pypi-josepy-license = %{version}-%{release}

%description bin
bin components for the pypi-josepy package.


%package license
Summary: license components for the pypi-josepy package.
Group: Default

%description license
license components for the pypi-josepy package.


%package python
Summary: python components for the pypi-josepy package.
Group: Default
Requires: pypi-josepy-python3 = %{version}-%{release}

%description python
python components for the pypi-josepy package.


%package python3
Summary: python3 components for the pypi-josepy package.
Group: Default
Requires: python3-core
Provides: pypi(josepy)
Requires: pypi(cryptography)
Requires: pypi(pyopenssl)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-josepy package.


%prep
%setup -q -n josepy-1.13.0
cd %{_builddir}/josepy-1.13.0
pushd ..
cp -a josepy-1.13.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656397810
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-josepy
cp %{_builddir}/josepy-1.13.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-josepy/d095fa0d394cc9417a65aecd0d28e7d10e762f98
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jws

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-josepy/d095fa0d394cc9417a65aecd0d28e7d10e762f98

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

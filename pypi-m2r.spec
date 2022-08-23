#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-m2r
Version  : 0.2.1
Release  : 5
URL      : https://files.pythonhosted.org/packages/39/e7/9fae11a45f5e1a3a21d8a98d02948e597c4afd7848a0dbe1a1ebd235f13e/m2r-0.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/39/e7/9fae11a45f5e1a3a21d8a98d02948e597c4afd7848a0dbe1a1ebd235f13e/m2r-0.2.1.tar.gz
Summary  : Markdown and reStructuredText in a single file.
Group    : Development/Tools
License  : MIT
Requires: pypi-m2r-bin = %{version}-%{release}
Requires: pypi-m2r-license = %{version}-%{release}
Requires: pypi-m2r-python = %{version}-%{release}
Requires: pypi-m2r-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(docutils)
BuildRequires : pypi(mistune)
BuildRequires : pypi-pygments

%description
M2R
        ===

%package bin
Summary: bin components for the pypi-m2r package.
Group: Binaries
Requires: pypi-m2r-license = %{version}-%{release}

%description bin
bin components for the pypi-m2r package.


%package license
Summary: license components for the pypi-m2r package.
Group: Default

%description license
license components for the pypi-m2r package.


%package python
Summary: python components for the pypi-m2r package.
Group: Default
Requires: pypi-m2r-python3 = %{version}-%{release}

%description python
python components for the pypi-m2r package.


%package python3
Summary: python3 components for the pypi-m2r package.
Group: Default
Requires: python3-core
Provides: pypi(m2r)
Requires: pypi(docutils)
Requires: pypi(mistune)

%description python3
python3 components for the pypi-m2r package.


%prep
%setup -q -n m2r-0.2.1
cd %{_builddir}/m2r-0.2.1
pushd ..
cp -a m2r-0.2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653853549
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-m2r
cp %{_builddir}/m2r-0.2.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-m2r/b150fd223b02601866bd624f1c39a7ad2edeabef
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/m2r

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-m2r/b150fd223b02601866bd624f1c39a7ad2edeabef

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

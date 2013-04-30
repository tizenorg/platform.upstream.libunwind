%define keepstatic 1

Name:           libunwind
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
Url:            http://savannah.nongnu.org/projects/libunwind/
Summary:        Unwind Library
License:        MIT
Group:          System/Libraries
Version:        1.1
Release:        0
VCS:            profile/base/libunwind#upstream/1.1-0-g0349587-dirty
Source:         libunwind-%{version}.tar.gz
ExclusiveArch:  %ix86 x86_64 %arm 

%description
A portable and efficient C programming interface (API) to determine the
call chain of a program.

%package devel
Summary:        Unwind library
Group:          Development/Libraries
Requires:       libunwind = %{version}-%{release}
Provides:       libunwind:%{_libdir}/libunwind.so

%description devel
A portable and efficient C programming interface (API) to determine the
call-chain of a program.

%prep
%setup -q

%build
autoreconf -fi
export CFLAGS="%optflags -U_FORTIFY_SOURCE"
%configure
make %{?_smp_mflags}


%install
%make_install
mkdir -p $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_libdir}/libunwind.so.8 $RPM_BUILD_ROOT%{_libdir}/libunwind.so
# Check that ln did not create a dangling link
stat "%buildroot"/$(readlink -f "%buildroot/%_libdir/libunwind.so");

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%_libdir/lib*
%{_libdir}/lib*.so.*
%{_libdir}/libunwind.so

%files devel
%defattr(-, root, root)
%{_prefix}/include/*
%{_libdir}/lib*.a
%{_libdir}/libunwind-*.so
%{_libdir}/pkgconfig/libunwind-generic.pc
%{_libdir}/pkgconfig/libunwind-ptrace.pc
%{_libdir}/pkgconfig/libunwind-setjmp.pc
%{_libdir}/pkgconfig/libunwind.pc
%ifarch %arm %ix86 x86_64
%{_libdir}/pkgconfig/libunwind-coredump.pc
%endif
%doc %{_mandir}/man?/*

%changelog

Summary:	C++ wrappers for libglade (cross mingw32 version)
Summary(pl.UTF-8):	Interfejsy C++ dla libglade (wersja skrośna mingw32)
%define		realname   libglademm
Name:		crossmingw32-%{realname}
Version:	2.6.7
Release:	1
License:	LGPL v2+
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libglademm/2.6/%{realname}-%{version}.tar.bz2
# Source0-md5:	f9ca5b67f6c551ea98790ab5f21c19d0
URL:		http://www.gtkmm.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	crossmingw32-gcc-c++
BuildRequires:	crossmingw32-gtkmm >= 2.12.1
BuildRequires:	crossmingw32-libglade2 >= 2.6.2
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.15
Requires:	crossmingw32-gtkmm >= 2.12.1
Requires:	crossmingw32-libglade2 >= 2.6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_libdir			%{_prefix}/lib
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
%define		_dlldir			/usr/share/wine/windows/system
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%ifnarch %{ix86}
# arch-specific flags (like alpha's -mieee) are not valid for i386 gcc
%define		optflags	-O2
%endif
# -z options are invalid for mingw linker
%define		filterout_ld	-Wl,-z,.*

%description
C++ wrappers for libglade (cross mingw32 version).

%description -l pl.UTF-8
Interfejsy C++ dla libglade (wersja skrośna mingw32).

%package static
Summary:	Static libglademm library (cross mingw32 version)
Summary(pl.UTF-8):	Statyczna biblioteka libglademm (wersja skrośna mingw32)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static libglademm library (cross mingw32 version).

%description static -l pl.UTF-8
Statyczna biblioteka libglademm (wersja skrośna mingw32).

%package dll
Summary:	DLL libglademm library for Windows
Summary(pl.UTF-8):	Biblioteka DLL libglademm dla Windows
Group:		Applications/Emulators
Requires:	crossmingw32-gtkmm-dll >= 2.12.1
Requires:	crossmingw32-libglade2-dll >= 2.6.2
Requires:	wine

%description dll
DLL libglademm library for Windows.

%description dll -l pl.UTF-8
Biblioteka DLL libglademm dla Windows.

%prep
%setup -q -n %{realname}-%{version}

%build
export PKG_CONFIG_LIBDIR=%{_prefix}/lib/pkgconfig
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--target=%{target} \
	--host=%{target} \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_dlldir}
mv -f $RPM_BUILD_ROOT%{_prefix}/bin/*.dll $RPM_BUILD_ROOT%{_dlldir}

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

rm -rf $RPM_BUILD_ROOT%{_libdir}/libglademm-2.4/proc
rm -rf $RPM_BUILD_ROOT%{_datadir}/{devhelp,doc/gnomemm-2.6}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%{_libdir}/libglademm-2.4.la
%{_libdir}/libglademm-2.4.dll.a
%{_includedir}/libglademm-2.4
%{_libdir}/libglademm-2.4
%{_pkgconfigdir}/libglademm-2.4.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libglademm-2.4.a

%files dll
%defattr(644,root,root,755)
%{_dlldir}/libglademm*-2.4-*.dll

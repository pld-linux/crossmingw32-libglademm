Summary:	C++ wrappers for libglade
Summary(pl.UTF-8):Interfejsy C++ dla libglade
%define		_realname   libglademm
Name:		crossmingw32-%{_realname}
Version:	2.6.3
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libglademm/2.6/%{_realname}-%{version}.tar.bz2
# Source0-md5:	3dd3c3777c4407b8a330bd79089ddbfc
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	crossmingw32-gtkmm >= 2.10.0
BuildRequires:	crossmingw32-libglade2 >= 2.6.0
BuildRequires:	crossmingw32-pkgconfig
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}
%define		gccarch			%{_prefix}/lib/gcc-lib/%{target}
%define		gcclib			%{_prefix}/lib/gcc-lib/%{target}/%{version}

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%description
C++ wrappers for libglade.

%description -l pl.UTF-8
Interfejsy C++ dla libglade.

%prep
%setup -q -n %{_realname}-%{version}

%build
export PKG_CONFIG_PATH=%{_prefix}/lib/pkgconfig
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%{_libdir}/libglademm*.la
%{_libdir}/libglademm*.a
%{_bindir}/libglademm*.dll
%{_includedir}/%{_realname}-2.4
%{_libdir}/%{_realname}-2.4
%{_pkgconfigdir}/%{_realname}-2.4.pc

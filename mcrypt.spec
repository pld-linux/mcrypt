Summary:	Mcrypt - simple crypting program
Summary(pl):	Mcrypt - prosty program szyfruj�cy
Name:		mcrypt
Version:	2.6.4
Release:	1
Vendor:		Fazekas Mih�ly Gimn�zium, Budapest
License:	GPL
Group:		Development/Libraries
Source0:	ftp://mcrypt.hellug.gr/pub/mcrypt/%{name}-%{version}.tar.gz
# Source0-md5:	5a011846fd0f166428c8d97359aaa6b3
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-man_fix.patch
Patch2:		%{name}-pl.po-update.patch
URL:		http://mcrypt.hellug.gr/mcrypt/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libmcrypt-devel >= 2.5.0
BuildRequires:	libtool
BuildRequires:	mhash-devel >= 0.8.15
Requires:	libmcrypt >= 2.5.0
Requires:	mhash >= 0.8.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A replacement for the old unix crypt(1) command. Mcrypt uses the
following encryption (block) algorithms: BLOWFISH, DES, TripleDES,
3-WAY, SAFER-SK64, SAFER-SK128, CAST-128, RC2 TEA (extended), TWOFISH,
RC6, IDEA and GOST. The unix crypt algorithm is also included, to
allow compability with the crypt(1) command.

CBC, ECB, OFB and CFB modes of encryption are supported. A library
which allows access to the above algorithms and modes is included.

%description -l pl
Zamiennik dla starej uniksowej funkcji crypt(). Mcrypt u�ywa
nast�puj�cych algorytm�w: BLOWFISH, DES, TripleDES, 3-WAY, SAFER-SK64,
SAFER-SK128, CAST-128, RC2 TEA (rozszerzona), TWOFISH, RC6, IDEA i
GOST. Uniksowy algorytm crypt tak�e jest obs�ugiwany, aby zachowa�
kompatybilno�� z crypt(1).

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f doc/mcrypt.info missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO  doc/{FORMAT,magic,sample.mcryptrc}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

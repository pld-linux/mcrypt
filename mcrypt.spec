Summary:	Mini-crypt
Summary(pl):	Mini-crypt
Name:		mcrypt
Version:	2.5.5
Release:	1
Vendor:		Fazekas Mihály Gimnázium, Budapest
License:	GPL
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Source0:	http://hq.hellug.gr/~mcrypt/mcrypt/%{name}-%{version}.tar.gz
Patch0:		mcrypt-DESTDIR.patch
Patch1:		mcrypt-man_fix.patch
BuildRequires:	libmcrypt-devel >= 2.4.0
BuildRequires:	gettext-devel
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
Zamiennik dla starej unixowej funkcji crypt(). Mcrypt u¿ywa
nastêpuj±cych algorytmów: BLOWFISH, DES, TripleDES, 3-WAY, SAFER-SK64,
SAFER-SK128, CAST-128, RC2 TEA (rozszerzona), TWOFISH, RC6, IDEA i
GOST. Unixowy algorytm crypt tak¿e jest obs³ugiwany by zachowaæ
kompatybilno¶æ z crypt(1).

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
rm -f doc/mcrypt.info
gettextize --copy --force
automake
LDFLAGS="-s"; export LDFLAGS
%configure \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR="$RPM_BUILD_ROOT" install
gzip -9nf {LSM,AUTHORS,NEWS,README,THANKS,TODO} doc/{FORMAT,magic,sample.mcryptrc}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {{LSM,AUTHORS,NEWS,README,THANKS,TODO},doc/{FORMAT,magic,sample.mcryptrc}}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

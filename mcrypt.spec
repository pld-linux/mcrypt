Summary:	Mini-crypt
Summary(pl):	Mini-crypt
Name:		mcrypt
Version:	2.2.6
Release:	3
Vendor:		Fazekas Mihály Gimnázium, Budapest
License:	GPL
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Source0:	http://hq.hellug.gr/~mcrypt/mcrypt/%{name}-%{version}.tar.gz
Patch0:		mcrypt-DESTDIR.patch
Patch1:		mcrypt-info.patch
Patch2:		mcrypt-man_fix.patch
BuildRequires:	libmcrypt-devel >= 2.3.0
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
%patch2 -p1

%build
rm -f doc/mcrypt.info
gettextize --copy --force
automake
LDFLAGS="-s"; export LDFLAGS
%configure \
	--without-included-gettext
make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR="$RPM_BUILD_ROOT" install

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/mdecrypt.1
echo ".so mcrypt.1" > $RPM_BUILD_ROOT%{_mandir}/man1/mdecrypt.1

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/mcrypt.info \
	$RPM_BUILD_ROOT%{_mandir}/man1/* \
	LSM doc/{FORMAT,README*,THANKS,magic}

%find_lang %{name}

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {LSM,doc/{FORMAT,README*,THANKS,magic}}.gz
%doc doc/sample.mcryptrc
%attr(755,root,root) %{_bindir}/*
%{_infodir}/mcrypt.info*
%{_mandir}/man1/*

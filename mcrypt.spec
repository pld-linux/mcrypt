Summary:	Mini-crypt
Name:		mcrypt
Version:	2.1.18
Release:	1
Vendor:		Fazekas Mihály Gimnázium, Budapest
Copyright:	GPL/LGPL
Group:		Development/Libraries
Source:		ftp://argeas.cs-net.gr/pub/unix/mcrypt/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
A replacement for the old unix crypt(1) command. Mcrypt uses the following
encryption (block) algorithms: BLOWFISH, DES, TripleDES, 3-WAY, SAFER-SK64,
SAFER-SK128, CAST-128, RC2 TEA (extended), TWOFISH, RC6, IDEA and GOST. The
unix crypt algorithm is also included, to allow compability with the
crypt(1) command.

CBC, ECB, OFB and CFB modes of encryption are supported. A library which
allows access to the above algorithms and modes is included.

%description -l pl
Zamiennik dla starej unixowej funkcji crypt(). Mcrypt u¿ywa nastêpuj±cych
algorytmów: BLOWFISH, DES, TripleDES, 3-WAY, SAFER-SK64, SAFER-SK128, CAST-128,
RC2 TEA (rozszerzona), TWOFISH, RC6, IDEA i GOST. Unixowy algorytm crypt tak¿e
jest obs³ugiwany by zachowaæ kompatybilno¶æ z crypt(1).

%prep
%setup -q

%build
%configure

make
make test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

make install bin=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	datadir=$RPM_BUILD_ROOT%{_datadir}

make install.lib bin=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	datadir=$RPM_BUILD_ROOT%{_datadir}

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/mdecrypt.1
echo ".so mcrypt.1" > $RPM_BUILD_ROOT%{_mandir}/man1/mdecrypt.1

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/mcrypt.info \
	$RPM_BUILD_ROOT%{_mandir}/man1/* \
	CHANGES LSM doc/{FORMAT,README*,THANKS,magic}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,LSM,doc/{FORMAT,README*,THANKS,magic}}.gz
%doc doc/sample.mcryptrc
%attr(755,root,root) %{_bindir}/mcrypt
%{_includedir}/mcrypt.h
%{_infodir}/mcrypt.info*
%{_libdir}/libmcrypt.a
%{_mandir}/man1/*

Name:		mcrypt
Version:	2.1.18
Release:	1
Vendor:		Fazekas Mihály Gimnázium, Budapest
Copyright:	GPL/LGPL
Group:		Fazekas
Summary:	Mini-crypt
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

%prep
%setup -q

%build
%configure

make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/info
make prefix=$RPM_BUILD_ROOT%prefix exec_prefix=$RPM_BUILD_ROOT%prefix install
make prefix=$RPM_BUILD_ROOT%prefix exec_prefix=$RPM_BUILD_ROOT%prefix install.lib
gzip $RPM_BUILD_ROOT%prefix/man/man1/mcrypt.1
rm $RPM_BUILD_ROOT%prefix/man/man1/mdecrypt.1
ln -s mcrypt.1.gz $RPM_BUILD_ROOT%prefix/man/man1/mdecrypt.1.gz
gzip $RPM_BUILD_ROOT%prefix/info/mcrypt.info
chmod 644 $RPM_BUILD_ROOT%prefix/info/mcrypt.info.gz
chmod -R a+rX,go-w $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING LSM
%doc doc/FORMAT doc/README* doc/THANKS doc/sample.mcryptrc doc/magic
%{_bindir}/mcrypt
%{_include}/mcrypt.h
%{_infodir}/mcrypt.info*
%{_libdir}/libmcrypt.a
%prefix/man/man1/*

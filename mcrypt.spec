%define name mcrypt
%define ver 2.1.18
%define rel 1
%define prefix /usr/local

Name: %name
Version: %ver
Release: %rel
Vendor: Fazekas Mihály Gimnázium, Budapest
Distribution: SuSE Linux 6.0 (i386)
Copyright: GPL / LGPL
Group: Fazekas
#Provides:
#Requires:
#Conflicts:
Packager: Koblinger Egmont <egmont@fazekas.hu>
Summary: Mini-crypt
Source: %name-%ver.tar.gz
Url: ftp://argeas.cs-net.gr/pub/unix/mcrypt
BuildRoot: /tmp/%name-%ver
Prefix: %prefix
%description
A replacement for the old unix crypt(1) command. Mcrypt
uses the following encryption (block) algorithms: BLOWFISH,
DES, TripleDES, 3-WAY, SAFER-SK64, SAFER-SK128, CAST-128, RC2
TEA (extended), TWOFISH, RC6, IDEA and GOST. The unix crypt
algorithm is also included, to allow compability with the
crypt(1) command.
CBC, ECB, OFB and CFB modes of encryption are supported.
A library which allows access to the above algorithms and
modes is included.

Author: Nikos Mavroyanopoulos <nmav@i-net.paiko.gr>

%prep
%setup

%build
./configure --prefix=%prefix --disable-nls
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/info
make prefix=$RPM_BUILD_ROOT%prefix exec_prefix=$RPM_BUILD_ROOT%prefix install
make prefix=$RPM_BUILD_ROOT%prefix exec_prefix=$RPM_BUILD_ROOT%prefix install.lib
gzip $RPM_BUILD_ROOT%prefix/man/man1/mcrypt.1
rm $RPM_BUILD_ROOT%prefix/man/man1/mdecrypt.1
ln -s mcrypt.1.gz $RPM_BUILD_ROOT%prefix/man/man1/mdecrypt.1.gz
gzip $RPM_BUILD_ROOT%prefix/info/mcrypt.info
chmod 644 $RPM_BUILD_ROOT%prefix/info/mcrypt.info.gz
chmod -R a+rX,go-w $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%prefix/bin/mcrypt
%prefix/bin/mdecrypt
%prefix/include/mcrypt.h
%prefix/info/mcrypt.info.gz
%prefix/lib/libmcrypt.a
%prefix/man/man1/mcrypt.1.gz
%prefix/man/man1/mdecrypt.1.gz
%doc CHANGES COPYING LSM
%doc doc/FORMAT doc/README* doc/THANKS doc/sample.mcryptrc doc/magic

%clean
rm -rf $RPM_BUILD_ROOT

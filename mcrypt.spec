Summary:	Mcrypt - simple crypting program
Summary(pl.UTF-8):	Mcrypt - prosty program szyfrujący
Name:		mcrypt
Version:	2.6.8
Release:	1
License:	GPL v3+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/mcrypt/%{name}-%{version}.tar.gz
# Source0-md5:	97639f8821b10f80943fa17da302607e
Patch0:		%{name}-man_fix.patch
Patch1:		%{name}-pl.po-update.patch
URL:		http://mcrypt.sourceforge.net/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libmcrypt-devel >= 2.5.0
BuildRequires:	libtool
BuildRequires:	mhash-devel >= 0.8.15
BuildRequires:	zlib-devel
Requires:	libmcrypt >= 2.5.0
Requires:	mhash >= 0.8.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A replacement for the old Unix crypt(1) command. Mcrypt uses the
following encryption (block) algorithms: BLOWFISH, DES, TripleDES,
3-WAY, SAFER-SK64, SAFER-SK128, CAST-128, RC2 TEA (extended), TWOFISH,
RC6, IDEA and GOST. The Unix crypt algorithm is also included, to
allow compability with the crypt(1) command.

CBC, ECB, OFB and CFB modes of encryption are supported. A library
which allows access to the above algorithms and modes is included.

%description -l pl.UTF-8
Zamiennik dla starej uniksowej funkcji crypt(). Mcrypt używa
następujących algorytmów: BLOWFISH, DES, TripleDES, 3-WAY, SAFER-SK64,
SAFER-SK128, CAST-128, RC2 TEA (rozszerzona), TWOFISH, RC6, IDEA i
GOST. Uniksowy algorytm crypt także jest obsługiwany, aby zachować
kompatybilność z crypt(1).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# just invalid inclusions
%{__rm} acinclude.m4

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

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
%attr(755,root,root) %{_bindir}/mcrypt
%attr(755,root,root) %{_bindir}/mdecrypt
%{_mandir}/man1/mcrypt.1*
%{_mandir}/man1/mdecrypt.1*

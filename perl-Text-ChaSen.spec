#
# Conditional build:
# _without_tests	- do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	ChaSen
Summary:	Text::ChaSen - ChaSen library module for Perl
Summary(pl):	Text::ChaSen - modu³ biblioteki ChaSen dla Perla
Name:		perl-%{pdir}-%{pnam}
Version:	1.03
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.daionet.gr.jp/~knok/chasen/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1f5f8b1c79b815c1bc7d171971f1f4a4
#Patch0:		http://www.daionet.gr.jp/~knok/chasen/%%{pnam}.pm-1.03-pod-fix.diff
URL:		http://www.daionet.gr.jp/~knok/chasen/
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-106
BuildRequires:	chasen-devel
Requires:	chasen
Obsoletes:	chasen-perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::ChaSen - ChaSen library module for Perl.

%description -l pl
Text::ChaSen - modu³ biblioteki ChaSen dla Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitearch}/Text/ChaSen.pm
%dir %{perl_sitearch}/auto/Text/ChaSen
%{perl_sitearch}/auto/Text/ChaSen/ChaSen.bs
%attr(755,root,root) %{perl_sitearch}/auto/Text/ChaSen/ChaSen.so
%{_mandir}/man3/*

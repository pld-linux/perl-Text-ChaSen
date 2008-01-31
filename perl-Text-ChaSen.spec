#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	ChaSen
Summary:	Text::ChaSen - ChaSen library module for Perl
Summary(pl.UTF-8):	Text::ChaSen - moduł biblioteki ChaSen dla Perla
Name:		perl-Text-ChaSen
Version:	1.03
Release:	4
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.daionet.gr.jp/~knok/chasen/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1f5f8b1c79b815c1bc7d171971f1f4a4
#Patch0:		http://www.daionet.gr.jp/~knok/chasen/%%{pnam}.pm-1.03-pod-fix.diff
URL:		http://www.daionet.gr.jp/~knok/chasen/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	chasen-devel
Requires:	chasen
Obsoletes:	chasen-perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::ChaSen - ChaSen library module for Perl.

%description -l pl.UTF-8
Text::ChaSen - moduł biblioteki ChaSen dla Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/Text/ChaSen.pm
%dir %{perl_vendorarch}/auto/Text/ChaSen
%{perl_vendorarch}/auto/Text/ChaSen/ChaSen.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Text/ChaSen/ChaSen.so
%{_mandir}/man3/*

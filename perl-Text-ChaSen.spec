#
# Conditional build:
# _without_tests	- do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	ChaSen
Summary:	ChaSen Perl Module
Summary(pl):	Modu³ perla ChaSen
Name:		perl-%{pdir}-%{pnam}
Version:	1.03
Release:	1
License:	Distributable
Group:		Development/Languages/Perl
Source0:	http://www.daionet.gr.jp/~knok/chasen/%{pdir}-%{pnam}-%{version}.tar.gz
# Source-md5	1f5f8b1c79b815c1bc7d171971f1f4a4
#Patch0:		http://www.daionet.gr.jp/~knok/chasen/%%{pnam}.pm-1.03-pod-fix.diff
URL:		http://www.daionet.gr.jp/~knok/chasen/
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	chasen-devel
Requires:	chasen
Obsoletes:	chasen-perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
ChaSen Perl Module.

%description -l pl
Modu³ perla ChaSen.

%prep
%setup -q -n Text-ChaSen-%{version}
#%%patch0 -p1

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

# if module isn't noarch, use:
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
%{perl_vendorarch}/Text/ChaSen.pm
%{perl_vendorarch}/auto/Text/ChaSen
%{_mandir}/man3/*

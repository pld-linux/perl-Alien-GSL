#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Alien
%define		pnam	GSL
Summary:	Alien::GSL - Easy installation of the GSL library
Name:		perl-Alien-GSL
Version:	1.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a5dee649d2af80624c99cf3554230d6b
URL:		https://metacpan.org/pod/Alien::GSL
BuildRequires:	perl-Alien-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Alien-Base
BuildRequires:	perl-Test-Alien
BuildRequires:	perl-Test2-Suite
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alien::GSL - Easy installation of the GSL library.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorarch}/Alien/GSL
%{perl_vendorarch}/Alien/GSL.pm
%{perl_vendorarch}/auto/Alien/GSL/GSL.txt
%{perl_vendorarch}/auto/share/dist/Alien-GSL
%{_mandir}/man3/*

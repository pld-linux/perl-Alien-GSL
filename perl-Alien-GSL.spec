#
# TODO: fix perl-Alien-Build dirs, this package is noarch
#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Alien
%define		pnam	GSL
Summary:	Alien::GSL - Easy installation of the GSL library
Summary(pl.UTF-8):	Alien::GSL - łatwa instalacja biblioteki GSL
Name:		perl-Alien-GSL
Version:	1.07
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a5dee649d2af80624c99cf3554230d6b
URL:		https://metacpan.org/dist/Alien-GSL
BuildRequires:	perl-Alien-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Alien-Base
BuildRequires:	perl-Test-Alien
BuildRequires:	perl-Test2-Suite
%endif
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
Alien::GSL - Easy installation of the GSL library.

%description -l pl.UTF-8
Alien::GSL - łatwa instalacja biblioteki GSL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorarch}/Alien/GSL
%{perl_vendorarch}/Alien/GSL.pm
%dir %{perl_vendorarch}/auto/Alien
%dir %{perl_vendorarch}/auto/Alien/GSL
%{perl_vendorarch}/auto/Alien/GSL/GSL.txt
%{perl_vendorarch}/auto/share/dist/Alien-GSL
%{_mandir}/man3/Alien::GSL.3pm*

#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTTP
%define		pnam	Headers-ActionPack
Summary:	HTTP::Headers::ActionPack - HTTP Action, Adventure and Excitement
Name:		perl-HTTP-Headers-ActionPack
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d0d2cb37e259cc0449f7883202356654
URL:		https://metacpan.org/release/HTTP-Headers-ActionPack
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-HTTP-Date
BuildRequires:	perl-HTTP-Message
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Test-Fatal >= 0.0003
BuildRequires:	perl-Test-Warnings
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a module to handle the inflation and deflation of complex HTTP
header types. In many cases header values are simple strings, but in
some cases they are complex values with a lot of information encoded
in them. The goal of this module is to make the parsing and analysis
of these headers as easy as calling inflate on a compatible object
(see below for a list).

This top-level class is basically a Factory for creating instances of
the other classes in this module. It contains a number of convenience
methods to help make common cases easy to write.

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/HTTP/Headers/*.pm
%{perl_vendorlib}/HTTP/Headers/ActionPack
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

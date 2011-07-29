Name:           doublecmd
Version:        0.5.5
Release:        1%{?dist}
Summary:        Double Commander is a cross platform open source file manager with two panels side by side.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

License:        GPLv2
URL:            http://doublecmd.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
Patch1:		%{name}-compile-error-fix.patch

BuildRequires:  qt4pas lazarus fpc fpc-src
#Requires:       

%description
Double Commander is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas.

%prep
%setup -q
%patch1 -p1 -b .compile-error-fix

%build
./build.sh all qt

%install
install -D -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
#%doc 
%{_bindir}/%{name}



%changelog
* Wed Jul 30 2011 Alexei Panov <elemc AT atisserv DOT ru> - 0.5.5-1
- Initial build with active support of sergem from fedora@c.j.r

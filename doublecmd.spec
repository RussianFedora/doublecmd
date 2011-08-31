%define svn     3860
%define realver 0.5.0

Name:           doublecmd
Version:        %{realver}.svn%{svn}
Release:        2%{?dist}.R
Summary:        Double Commander is a cross platform open source file manager with two panels side by side.

License:        GPLv2
URL:            http://doublecmd.sourceforge.net/
Source0:        %{name}-%{version}.tar.xz
#Patch1:         %{name}-compile-error-fix.patch

BuildRequires:  qt4pas lazarus fpc fpc-src       

%description
Double Commander is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        qt
Summary:        Twin-panel (commander-style) file manager (QT)
Provides:       %{name}
Conflicts:      %{name}-gtk

%description    qt
Double Commander is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas. QT

%prep
%setup -q
#%patch1 -p1 -b .compile-error-fix

%build
./build.sh all qt

%install
install/linux/install.sh --install-prefix=%{buildroot}

%files qt
%defattr(-,root,root)
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%exclude %{_datadir}/%{name}/doc/
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Aug 30 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.0-svn3860.1.R
- Apdate to new revision

* Wed Aug 10 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.5-svn3796.1.R
- Removed .svn files
- Update svn to 3796

* Wed Jul 30 2011 Alexei Panov <elemc AT atisserv DOT ru> - 0.5.5-1
- Initial build with active support of sergem from fedora@c.j.r

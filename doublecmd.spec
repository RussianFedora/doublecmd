%global svn     3789

Name:           doublecmd
Version:        0.5.5
Release:        svn%{svn}.1%{?dist}.R
Summary:        Double Commander is a cross platform open source file manager with two panels side by side.

License:        GPLv2
URL:            http://doublecmd.sourceforge.net/
Source0:        %{name}-svn%{svn}.tar.xz
Patch1:         %{name}-compile-error-fix.patch

BuildRequires:  qt4pas lazarus fpc fpc-src       

%description
Double Commander is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        qt
Summary:        Twin-panel (commander-style) file manager (GTK2)
Provides:       %{name}
Conflicts:      %{name}-gtk

%description    qt
Double Commander is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas. QT

%prep
%setup -q -n %{name}
%patch1 -p1 -b .compile-error-fix

%build
./build.sh all qt

%install
install/linux/install.sh --install-prefix=%{buildroot}

%files qt
#%doc 
#%{_bindir}/%{name}
%defattr(-,root,root)
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/language/.svn
%exclude %{_datadir}/%{name}/language/lcl/.svn
%{_datadir}/pixmaps/%{name}.png
%exclude %{_datadir}/%{name}/pixmaps/.svn
%exclude %{_datadir}/%{name}/pixmaps/dctheme/.svn
%exclude %{_datadir}/%{name}/pixmaps/dctheme/*x*/.svn
%exclude %{_datadir}/%{name}/pixmaps/dctheme/*x*/*/.svn
%exclude %{_datadir}/%{name}/doc/
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Aug 10 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.5-svn3789.1.R
- Removed .svn files
- Update svn to 3789

* Wed Jul 30 2011 Alexei Panov <elemc AT atisserv DOT ru> - 0.5.5-1
- Initial build with active support of sergem from fedora@c.j.r

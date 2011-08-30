%define svn     3860
%define realver 0.5.0

Name:           doublecmd
Summary:        Twin-panel (commander-style) file manager
Version:        %{realver}.svn%{svn}
Release:        1%{?dist}.R
URL:            http://doublecmd.sourceforge.net
Source0:        %{name}-%{version}.tar.bz2
License:        GPL
Group:          Applications/File
BuildRequires:	fpc >= 2.4.0 fpc-src glib2-devel gtk2-devel lazarus >= 0.9.29
BuildRequires:  gdk-pixbuf-devel ncurses-devel dbus-devel bzip2-devel xorg-x11-proto-devel xorg-x11-xtrans-devel
BuildRequires:  util-linux

%description
Double Commander is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        gtk
Summary:        Twin-panel (commander-style) file manager (GTK2)
Provides:       %{name}
Conflicts:      %{name}-qt

%description    gtk
Double Commander is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas. GTK2

%package        doc
Summary:        Double Commander's help files

%description    doc
Double Commander's help files

%prep
%setup -q
chmod +x install/linux/install-help.sh

%build
./build.sh all gtk2

%install
install/linux/install.sh --install-prefix=%{buildroot}
install/linux/install-help.sh --install-prefix=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files gtk
%defattr(-,root,root)
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%exclude %{_datadir}/%{name}/doc/
%{_datadir}/applications/%{name}.desktop

%files doc
%defattr(-,root,root)
%{_datadir}/%{name}/doc

%changelog
* Tue Aug 30 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.0-svn3860.1.R
- Apdate to new revision

* Mon Aug 08 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.5-svn3789.2.R
- Added documentation package

* Mon Aug 08 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.5-svn3789.1.R
- Removed .svn files
- Update svn to 3789

* Thu Jul  28 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.5-svn3765.2.R
- Split packages
- Clean spec

* Thu Jul  28 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.5-svn3765.1.R
- Initial build for Fedora

* Fri Jun 11 2010 - Alexander Koblov <Alexx2000@mail.ru>
- Initial package, version 0.4.6

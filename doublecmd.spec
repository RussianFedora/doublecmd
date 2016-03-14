%global debug_package %{nil}
%global help_version 0.6.0

Name:           doublecmd
Version:        0.7.0
Release:        1%{?dist}
Summary:        Cross platform open source file manager with two panels (GTK2)

License:        GPLv2
URL:            http://doublecmd.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
Source1:        http://downloads.sourceforge.net/%{name}/%{name}-help-%{help_version}-src.tar.gz
Source2:        %{name}-qt.desktop

BuildRequires:  fpc >= 2.6.0
BuildRequires:  fpc-src
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  lazarus >= 1.0.0
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  ncurses-devel
BuildRequires:  dbus-devel
BuildRequires:  bzip2-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-xtrans-devel
BuildRequires:  util-linux
BuildRequires:  pango-devel
BuildRequires:  desktop-file-utils
BuildRequires:  qt4pas-devel

%description
Double Commander GTK2 is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        doc
Summary:        Double Commander's help files
BuildArch:      noarch

%description    doc
Double Commander's help files

%package        gtk
Summary:        Twin-panel (commander-style) file manager (GTK)
Group:          File tools
Requires:       %{name}-common%{?_isa} = %{version}-%{release}

%description    gtk
Double Commander GTK is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        qt
Summary:        Twin-panel (commander-style) file manager (Qt4)
Group:          File tools
Requires:       %{name}-common%{?_isa} = %{version}-%{release}

%description    qt
Double Commander QT4 is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        common
Summary:        Common files for Double Commander

%description    common
Common files for Double Commander GTK2 and Qt.

%prep
%setup -q
chmod +x install/linux/install-help.sh
tar -xvf %{SOURCE1}
mv %{name}-help-%{help_version}/* doc/

%build
./build.sh beta qt
mv ./%name ./%name-qt
mv ./%name.zdli ./%name-qt.zdli
./clean.sh
./build.sh beta gtk2

%install
install/linux/install.sh --install-prefix=%{buildroot}
install -pm 0755 ./%{name}-qt %{buildroot}%{_libdir}/%{name}/%{name}-qt
ln -s ../%{_lib}/%{name}/%{name}-qt %{buildroot}%{_bindir}/%{name}-qt
install -pm 0644 ./%{name}-qt.zdli %{buildroot}%{_libdir}/%{name}/%{name}-qt.zdli

install/linux/install-help.sh --install-prefix=%{buildroot}

desktop-file-install %{SOURCE2}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files gtk
%doc doc/changelog.txt  doc/README.RUS.txt  doc/README.txt
%license doc/COPYING.LGPL.txt  doc/COPYING.modifiedLGPL.txt  doc/COPYING.txt
%{_libdir}/%{name}/%{name}
%{_bindir}/%{name}
%_libdir/%name/%name.zdli
%{_datadir}/applications/%{name}.desktop


%files qt
%{_libdir}/%{name}/%{name}-qt
%{_bindir}/%{name}-qt
%{_libdir}/%{name}/%{name}-qt.zdli
%{_datadir}/applications/%{name}-qt.desktop

%files common
%exclude %{_libdir}/%{name}/%{name}
%exclude %{_libdir}/%{name}/%{name}-qt
%exclude %{_libdir}/%{name}/%{name}.zdli
%exclude %{_libdir}/%{name}/%{name}-qt.zdli
%exclude %{_bindir}/%{name}
%exclude %{_bindir}/%{name}-qt
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/pixmaps/%{name}.*

%files doc
%{_datadir}/%{name}/doc

%changelog
* Mon Mar 14 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.0-1
- Update to 0.7.0

* Thu Nov 19 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.6.6-1
- Update to 0.6.6
- One spec for GTK and Qt version

* Fri Oct 09 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.6.5-1
- Update to 0.6.5

* Tue Feb 10 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.6.0-1
- Update to 0.6.0

* Wed Oct 12 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.0-svn3993.1.R
- Update to new revision

* Tue Aug 30 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.0-svn3926.1.R
- Update to new revision

* Tue Aug 30 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.0-svn3860.1.R
- Update to new revision

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

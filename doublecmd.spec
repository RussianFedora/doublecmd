%global debug_package %{nil}
%global help_version 0.6.0

Name:           doublecmd
Version:        0.8.4
Release:        1%{?dist}
Summary:        Cross platform open source file manager with two panels

License:        GPLv2
URL:            http://doublecmd.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
Source1:        http://downloads.sourceforge.net/project/doublecmd/Double%20Commander%20Source/%{name}-help-%{help_version}-src.tar.gz
Source2:        %{name}-qt.desktop

BuildRequires:  fpc >= 2.6.0
BuildRequires:  fpc-src
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  lazarus >= 1.0.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(dbus-1)
%if 0%{?fedora} >= 23
BuildRequires:  pkgconfig(bzip2)
%else
BuildRequires:  bzip2-devel
%endif
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  util-linux
BuildRequires:  pkgconfig(pango)
BuildRequires:  desktop-file-utils
BuildRequires:  qt5pas-devel
BuildRequires:  qt5-qtbase-devel

Requires:       hicolor-icon-theme

ExclusiveArch:  %{fpc_arches}

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
%autosetup
chmod +x install/linux/install-help.sh
tar -xvf %{SOURCE1}
mv %{name}-help-%{help_version}/* doc/

%build
lcl=qt5 ./build.sh beta
mv ./%name ./%name-qt
mv ./%name.zdli ./%name-qt.zdli
./clean.sh
lcl=gtk2 ./build.sh beta

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
%doc doc/changelog.txt doc/README.txt
%license doc/COPYING.LGPL.txt doc/COPYING.modifiedLGPL.txt doc/COPYING.txt
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
%{_datadir}/icons/hicolor/scalable/apps/doublecmd.svg
%{_datadir}/polkit-1/actions/org.doublecmd.root.policy

%files doc
%{_datadir}/%{name}/doc

%changelog
* Wed Aug 29 2018 Vasiliy N. Glazov <vascom2@gmail.com> 0.8.4-1
- Update to 0.8.4

* Thu Dec 14 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.8.3-1
- Update to 0.8.3

* Thu Dec 14 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.8.2-1
- Update to 0.8.2

* Thu Dec 14 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.8.0-1
- Update to 0.8.0

* Mon Mar 06 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.8-1
- Update to 0.7.8

* Mon Dec 26 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.7-1
- Update to 0.7.7

* Fri Sep 16 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.5-1
- Update to 0.7.5

* Fri Jul 15 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.3-1
- Update to 0.7.3

* Fri Jun 03 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.2-1
- Update to 0.7.2

* Thu Apr 21 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.1-1
- Update to 0.7.1

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

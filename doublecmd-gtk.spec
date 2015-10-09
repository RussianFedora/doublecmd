%global debug_package %{nil}
%global realname doublecmd
%global help_version 0.6.0

Name:           doublecmd-gtk
Version:        0.6.5
Release:        1%{?dist}
Summary:        Cross platform open source file manager with two panels

License:        GPLv2
URL:            http://doublecmd.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{realname}/%{realname}-%{version}-src.tar.gz
Source1:        http://downloads.sourceforge.net/%{realname}/%{realname}-help-%{help_version}-src.tar.gz

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

Provides:       %{realname} = %{version}
Conflicts:      %{realname}-qt

%description
Double Commander is a cross platform open source file manager with two panels
side by side.
It is inspired by Total Commander and features some new ideas.
GTK2 version.

%package -n     %{realname}-doc
Summary:        Double Commander's help files
BuildArch:      noarch

%description -n %{realname}-doc
Double Commander's help files

%prep
%setup -q -n %{realname}-%{version}
chmod +x install/linux/install-help.sh
tar -xvf %{SOURCE1}
mv %{realname}-help-%{help_version}/* doc/

%build
./build.sh beta gtk2

%install
install/linux/install.sh --install-prefix=%{buildroot}
install/linux/install-help.sh --install-prefix=%{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{realname}.desktop


%files
%doc doc/changelog.txt  doc/README.RUS.txt  doc/README.txt
%license doc/COPYING.LGPL.txt  doc/COPYING.modifiedLGPL.txt  doc/COPYING.txt
%{_libdir}/%{realname}
%{_bindir}/%{realname}
%{_datadir}/%{realname}
%{_datadir}/pixmaps/%{realname}.*
%exclude %{_datadir}/%{realname}/doc/
%{_datadir}/applications/%{realname}.desktop
%{_mandir}/man1/%{realname}.1.gz

%files -n %{realname}-doc
%{_datadir}/%{realname}/doc

%changelog
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

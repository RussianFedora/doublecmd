%global svn     3789

Name:		doublecmd
Summary:	Twin-panel (commander-style) file manager
Version:	0.5.5
Release:	svn%{svn}.1%{?dist}.R
URL:		http://doublecmd.sourceforge.net
Source0:	doublecmd-svn%{svn}.tar.xz
License:	GPL
Group:		Applications/File
BuildRequires:	fpc >= 2.4.0 fpc-src glib2-devel gtk2-devel lazarus >= 0.9.29
BuildRequires:  gdk-pixbuf-devel ncurses-devel dbus-devel bzip2-devel xorg-x11-proto-devel xorg-x11-xtrans-devel
BuildRequires:  util-linux

%description
Double Commander is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        gtk
Summary:        Twin-panel (commander-style) file manager (GTK2)
Provides:  doublecmd
Obsoletes: doublecmd < 0.4.6 doublecmd-qt

%description    gtk
Double Commander is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas. GTK2

%prep
%setup -q -n doublecmd

%build
./build.sh all gtk2

%install
install/linux/install.sh --install-prefix=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files gtk
%defattr(-,root,root)
%{_libdir}/doublecmd
%{_bindir}/doublecmd
%{_datadir}/doublecmd
%exclude %{_datadir}/doublecmd/language/.svn
%exclude %{_datadir}/doublecmd/language/lcl/.svn
%{_datadir}/pixmaps/doublecmd.png
%exclude %{_datadir}/doublecmd/pixmaps/.svn
%exclude %{_datadir}/doublecmd/pixmaps/dctheme/.svn
%exclude %{_datadir}/doublecmd/pixmaps/dctheme/*x*/.svn
%exclude %{_datadir}/doublecmd/pixmaps/dctheme/*x*/actions/.svn
%exclude %{_datadir}/doublecmd/pixmaps/dctheme/*x*/apps/.svn
%exclude %{_datadir}/doublecmd/pixmaps/dctheme/*x*/devices/.svn
%exclude %{_datadir}/doublecmd/pixmaps/dctheme/*x*/emblems/.svn
%exclude %{_datadir}/doublecmd/pixmaps/dctheme/*x*/mimetypes/.svn
%exclude %{_datadir}/doublecmd/pixmaps/dctheme/*x*/places/.svn
%{_datadir}/applications/doublecmd.desktop

%changelog
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

%define debug_package %{nil}

Summary: StotinkaOS defaults configs
Name:    stotinkaos-defaults
Version: 0.4
Release: 4%{?dist}
Group:   System Environment/Base
License: GPLv3+
Url:     http://stotinkaos.net/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: google-noto-sans-fonts google-noto-serif-fonts google-droid-sans-mono-fonts
Requires: freetype-freeworld
Requires: faba-icon-theme faba-mono-icons moka-icon-theme
Requires: gnome-shell-extension-panel-favorites
Requires: gnome-shell-extension-panel-osd
Requires: gnome-shell-extension-nohotcorner
Requires: gnome-shell-impatience
Requires(post): glib2
Conflicts: stotinkaos-xfce-defaults
BuildArch: noarch

%description
%{summary}.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_sysconfdir}/skel
mkdir -p %{buildroot}%{_sysconfdir}/fonts
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas

install -m 0755 %{_builddir}/%{name}-%{version}/nanorc %{buildroot}%{_sysconfdir}/skel/.nanorc
cp -a %{_builddir}/%{name}-%{version}/Templates %{buildroot}%{_sysconfdir}/skel/
install -m 0755 %{_builddir}/%{name}-%{version}/kern_dir.sh %{buildroot}%{_sysconfdir}/profile.d/kern_dir.sh
install -m 0755 %{_builddir}/%{name}-%{version}/color_prompt.sh %{buildroot}%{_sysconfdir}/profile.d/color_prompt.sh
install -m 0755 %{_builddir}/%{name}-%{version}/local.conf %{buildroot}%{_sysconfdir}/fonts/local.conf
install -m 0644 %{_builddir}/%{name}-%{version}/org.stotinkaos.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/org.stotinkaos.gschema.override

%clean
rm -rf %{buildroot}

%pre

%post
# rebuild schema cache with any overrides we installed
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null

%postun
# rebuild schema cache with any overrides we installed
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null

%files
%defattr(-,root,root)
%{_sysconfdir}/skel/.nanorc
%{_sysconfdir}/skel/Templates/*
%{_sysconfdir}/profile.d/kern_dir.sh
%{_sysconfdir}/profile.d/color_prompt.sh
%{_sysconfdir}/fonts/local.conf
%{_datadir}/glib-2.0/schemas/org.stotinkaos.gschema.override

%changelog
* Sat Nov 25 2017 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.4-4
- Revert Yumex
* Thu Nov 23 2017 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.4-3
- Fix natural scroll
- Fix nautilus thumbnail size
- Add gnome-shell-extension-add-username-toppanel
* Sun Nov 05 2017 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.4-2
- Fix touchpad settings
* Tue Oct 17 2017 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.4-1
- Update to 7.4 release
* Sat Feb 18 2017 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.3-3
- Add Conflicts stotinkaos-xfce-defaults
* Tue Feb 14 2017 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.3-2
- Fix keyboard
* Mon Feb 13 2017 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.3-1
- Add Cinnamon settings
* Sun Dec 18 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.2-2
- Add missing Requires
* Wed Nov 30 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.2-1
- Update to 7.3 release
* Thu Feb 11 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.1-1
- initial "build"

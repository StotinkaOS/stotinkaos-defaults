%define debug_package %{nil}

Summary: StotinkaOS defaults configs
Name:    stotinkaos-defaults
Version: 0.1
Release: 1%{?dist}.sos
Group:   System Environment/Base
License: GPLv3+
Url:     http://stotinkaos.net/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: google-noto-sans-fonts google-noto-serif-fonts google-droid-sans-mono-fonts
Requires: freetype-freeworld
Requires: faba-icon-theme faba-mono-icons moka-icon-theme
Requires(post): glib2
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
* Thu Feb 11 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.1-1
- initial "build"

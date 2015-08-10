Summary: StotinkaOS defaults configs
Name:    stotinkaos-defaults
Version: 0.2
Release: 3%{?dist}.sos
Group:   System Environment/Base
License: GPLv3+
Url:     http://stotinkaos.net/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

Requires: GConf2 bluebird-metacity-theme paratype-pt-sans-fonts paratype-pt-mono-fonts

%description
%{summary}.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_sysconfdir}/skel

install -m 0755 %{_builddir}/%{name}-%{version}/nanorc %{buildroot}%{_sysconfdir}/skel/.nanorc
install -m 0755 %{_builddir}/%{name}-%{version}/kern_dir.sh %{buildroot}%{_sysconfdir}/profile.d/kern_dir.sh
install -m 0755 %{_builddir}/%{name}-%{version}/color_prompt.sh %{buildroot}%{_sysconfdir}/profile.d/color_prompt.sh

%clean
rm -rf %{buildroot}

%pre

%post

# GNOME Settings

# Enable PackageKit update checking by default
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults -s -t int /apps/gnome-packagekit/update-icon/frequency_get_updates 86400 2>/dev/null
# Add a Keyboard Applet to the top panel
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults --type string --set /apps/panel/applets/keyboard/bonobo_iid OAFIID:GNOME_KeyboardApplet
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults --type string --set /apps/panel/applets/keyboard/object_type bonobo-applet
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults --type bool --set /apps/panel/applets/keyboard/panel_right_stick false
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults --type int --set /apps/panel/applets/keyboard/position 1098
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults --type string --set /apps/panel/applets/keyboard/toplevel_id top_panel
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults --type list --list-type string --set /apps/panel/general/applet_id_list "[clock,systray,show_desktop_button,window_list,workspace_switcher,keyboard,trash_applet]"
# Toggle keyboard layouts
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults --type list --list-type string --set /desktop/gnome/peripherals/keyboard/kbd/layouts "[us,bg]"
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.defaults --type list --list-type string --set /desktop/gnome/peripherals/keyboard/kbd/options "[grp	grp:alt_shift_toggle]"
# Switching to Thunderbird as the default MUA
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --type string --set /desktop/gnome/url-handlers/mailto/command "thunderbird %" 2>/dev/null
# Touchpad
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type int /desktop/gnome/peripherals/touchpad/scroll_method 2 2>/dev/null
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type bool /desktop/gnome/peripherals/touchpad/disable_while_typing true 2>/dev/null
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type bool /desktop/gnome/peripherals/touchpad/tap_to_click true 2>/dev/null
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type bool /desktop/gnome/peripherals/touchpad/horiz_scroll_enabled true 2>/dev/null
# disable nautilus to open folder in the same window
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type bool /apps/nautilus/preferences/always_use_browser true 2>/dev/null
# metacity set default theme
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /apps/metacity/general/theme Bluebird 2>/dev/null
# Font settings
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /desktop/gnome/font_rendering/antialiasing "rgba" 2>/dev/null 
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /desktop/gnome/font_rendering/hinting "slight" 2>/dev/null 
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /desktop/gnome/font_rendering/rgba_order "rgb" 2>/dev/null 
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --type string --set /apps/nautilus/preferences/desktop_font "PT Sans 11" 2>/dev/null
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --type string --set /apps/metacity/general/titlebar_font "PT Sans Bold 11" 2>/dev/null
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --type string --set /desktop/gnome/interface/document_font_name "PT Sans 11" 2>/dev/null
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --type string --set /desktop/gnome/interface/monospace_font_name "PT Mono 11" 2>/dev/null
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --type string --set /desktop/gnome/interface/font_name "PT Sans 11" 2>/dev/null
# Open terminal with Ctrl+Alt t
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /apps/metacity/global_keybindings/run_command_terminal "<Control><Alt>t" 2>/dev/null
# Change gnome's terminal font
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /apps/gnome-terminal/profiles/Default/font "PT Mono 11" 2>/dev/null
# Disable Emacs keybindings in Gnome
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set --type string /desktop/gnome/interface/gtk_key_theme "Default" 2>/dev/null
# Enable menu and buttons icons
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set /desktop/gnome/interface/buttons_have_icons --type bool "true" 2>/dev/null
gconftool-2 --direct --config-source=xml:readwrite:/etc/gconf/gconf.xml.defaults --set /desktop/gnome/interface/menus_have_icons --type bool "true" 2>/dev/null

%postun

%files
%defattr(-,root,root)
%{_sysconfdir}/skel/.nanorc
%{_sysconfdir}/profile.d/kern_dir.sh
%{_sysconfdir}/profile.d/color_prompt.sh

%changelog
* Mon Aug 10 2015 Ivaylo Kuzev <ivo@stotinkaos.net> - 0.2-3 
- Fix keyboard applet
 
* Sat Jul 04 2015 Ivaylo Kuzev <ivo@stotinkaos.net> - 0.2-2
- Revert to Bulgarian BDS keyboard layout
- Remove fortune/cowsay

* Mon Jun 29 2015 Ivaylo Kuzev <ivo@stotinkaos.net> - 0.2
- Fix Bug - with missing key touchpad and disable_while_typing option
- Enable menu and buttons icons
- Disable Emacs keybindings by default
- Set gnome's terminal font to use PT Mono
- Change bulgarian kbd layout to use bas_phonetic
- Add various files required for StotinkaOS

* Sat Jan 31 2015 Ivaylo Kuzev <ivo@stotinkaos.net> - 0.1
- initial "build"

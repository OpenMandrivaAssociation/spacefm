Summary:	A multi-panel tabbed file manager
Name:		spacefm
Version:	1.0.6
Release:	1
License:	GPLv3+
Group:		File tools
Url:		http://ignorantguru.github.com/spacefm/
Source0:	http://download.sourceforge.net/spacefm/%{name}-%{version}.tar.gz
Patch0:   spacefm-sysmacros.patch
BuildRequires:	intltool
# It's possible to build with GTK2 as well
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libudev)
BuildRequires:  pkgconfig(libffmpegthumbnailer)

# To perform 'run as root' functions
Requires:	gksu
# Eject media
Requires:	util-linux
# For device processes
Requires:	lsof
# Mount as non-root user
Requires:	udisks2
# For plugin download
Requires:	wget

%description
SpaceFM is a multi-panel tabbed file manager with built-in VFS, udev-based
device manager, customizable menu system, and bash integration.

%prep
%setup -q
%autopatch -p0

%build
autoreconf -vfi
%configure2_5x --with-gtk3
%make_build

%install
%make_install

# for configs
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/

# handle docs in files section
rm -rf %{buildroot}%{_defaultdocdir}

%find_lang %{name}

%files -f %{name}.lang
%doc data/spacefm-manual-en.html
%{_bindir}/%{name}*
%dir %{_sysconfdir}/%{name}/
%{_sysconfdir}/spacefm/spacefm.conf
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/spacefm-mime.xml
%{_iconsdir}/hicolor/*/apps/%{name}*.png
%{_iconsdir}/Faenza/apps/*/spacefm*.png

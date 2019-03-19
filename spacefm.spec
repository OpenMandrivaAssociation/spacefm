Summary:	A multi-panel tabbed file manager
Name:		spacefm
Version:	1.0.6
Release:	1
License:	GPLv3+
Group:		File tools
Url:		http://ignorantguru.github.com/spacefm/
Source0:	http://download.sourceforge.net/spacefm/%{name}-%{version}.tar.gz
BuildRequires:	intltool
# It's possible to build with GTK3 as well
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libudev)
BuildRequires:  libffmpegthumbnailer-devel

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

%build
%configure2_5x
%make

%install
%makeinstall_std

# for configs
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/

# handle docs in files section
rm -rf %{buildroot}%{_defaultdocdir}

%find_lang %{name}

%files -f %{name}.lang
%doc data/spacefm-manual-en.html
%{_bindir}/%{name}*
%dir %{_sysconfdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/spacefm-mime.xml
%{_iconsdir}/hicolor/*/apps/%{name}*.png
%{_iconsdir}/Faenza/apps/*/spacefm*.png

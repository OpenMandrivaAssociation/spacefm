Summary:	A multi-panel tabbed file manager
Name:		spacefm
Version:	1.0.6
Release:	2
License:	GPLv3+
Group:		File tools
Url:		https://ignorantguru.github.io/spacefm/
Source0:	https://github.com/IgnorantGuru/spacefm/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		spacefm-sysmacros.patch
# (upstream) https://github.com/IgnorantGuru/spacefm/pull/772
Patch1:		spacefm-1.0.6-fix_link.patch
#Patch1:		https://github.com/IgnorantGuru/spacefm/pull/772/commits/581d54035d3b1f35a77afdd1c3be92a7acfc6b90.patch
#Patch2:		https://github.com/IgnorantGuru/spacefm/commit/169338091100045316f5cb5ad22c4af748efdd2f.patch
# (fedora)
Patch4:		spacefm-1.0.5-force-x11-backend.patch

BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libffmpegthumbnailer)
BuildRequires:	pkgconfig(x11)

# To perform 'run as root' functions
#Requires:	gksu
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

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
#autoreconf -fiv
%configure --with-gtk3
%make_build

%install
%make_install

# for configs
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/

# handle docs in files section
rm -rf %{buildroot}%{_defaultdocdir}

%find_lang %{name}


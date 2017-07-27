Name:           ros-kinetic-nav-pcontroller
Version:        0.1.4
Release:        0%{?dist}
Summary:        ROS nav_pcontroller package

Group:          Development/Libraries
License:        BSD
URL:            https://www.github.com/code-iai/nav_pcontroller
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-move-base-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-visualization-msgs
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-move-base-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslib
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-visualization-msgs

%description
Simple P-Controller for a holonomic robot base

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Jul 27 2017 Alexis Maldonado <amaldo@cs.uni-bremen.de> - 0.1.4-0
- Autogenerated by Bloom

* Mon Jul 18 2016 Jan Winkler <winkler@cs.uni-bremen.de> - 0.1.2-0
- Autogenerated by Bloom


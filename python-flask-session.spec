# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-flask-session
Epoch: 100
Version: 0.8.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Server-side session support for Flask
License: BSD-3-Clause
URL: https://github.com/pallets-eco/flask-session/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
Flask-Session is an extension for Flask that adds support for
server-side sessions to your application.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} >= 1500
%package -n python%{python3_version_nodots}-Flask-Session
Summary: Server-side session support for Flask
Requires: python3
Requires: python3-cachelib
Requires: python3-Flask >= 2.2
Requires: python3-msgspec >= 0.18.6
Provides: python3-Flask-Session = %{epoch}:%{version}-%{release}
Provides: python3dist(Flask-Session) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-Flask-Session = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(Flask-Session) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-Flask-Session = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(Flask-Session) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-Flask-Session
Flask-Session is an extension for Flask that adds support for
server-side sessions to your application.

%files -n python%{python3_version_nodots}-Flask-Session
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} >= 1500)
%package -n python3-flask-session
Summary: Server-side session support for Flask
Requires: python3
Requires: python3-cachelib
Requires: python3-flask >= 2.2
Requires: python3-msgspec >= 0.18.6
Provides: python3-flask-session = %{epoch}:%{version}-%{release}
Provides: python3dist(flask-session) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-flask-session = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(flask-session) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-flask-session = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(flask-session) = %{epoch}:%{version}-%{release}

%description -n python3-flask-session
Flask-Session is an extension for Flask that adds support for
server-side sessions to your application.

%files -n python3-flask-session
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%changelog

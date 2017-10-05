[project]
name = golang
version = 1.9.1
vendor = golang.org
homepage = https://golang.org/
groups = dev/sys-runtime
description = open source programming language that makes it easy to build simple, reliable, and efficient software.

%build
PREFIX="{{.project__prefix}}"

cd {{.inpack__pack_dir}}/deps

if [ ! -f "go{{.project__version}}.linux-amd64.tar.gz" ]; then
    wget https://storage.googleapis.com/golang/go{{.project__version}}.linux-amd64.tar.gz
fi
if [ ! -d "go" ]; then
    tar -zxf go{{.project__version}}.linux-amd64.tar.gz
fi

cd go

cp -rp bin  {{.buildroot}}/
cp -rp lib  {{.buildroot}}/
cp -rp pkg  {{.buildroot}}/
cp -rp src  {{.buildroot}}/
cp -rp LICENSE   {{.buildroot}}/
cp -rp VERSION   {{.buildroot}}/
if [ -f "README.md" ]; then
    cp -rp README.md {{.buildroot}}/
fi
if [ -f "README" ]; then
    cp -rp README {{.buildroot}}/
fi

cd {{.inpack__pack_dir}}/deps
rm -rf go

%files

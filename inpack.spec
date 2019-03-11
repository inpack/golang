[project]
name = golang
version = 1.11
vendor = golang.org
homepage = https://golang.org/
groups = dev/sys-runtime
description = open source programming language that makes it easy to build simple, reliable, and efficient software.

%build

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

files=`find {{.buildroot}}/bin/ -executable -type f |xargs`
for file in $files; do
    strip -s ${file}
done
files=`find {{.buildroot}}/pkg/tool/linux_amd64/ -executable -type f |xargs`
for file in $files; do
    strip -s ${file}
done

cd {{.inpack__pack_dir}}
mkdir -p {{.buildroot}}/misc
install misc/inner-init.sh {{.buildroot}}/inner-init.sh
install misc/profile.d_golang.sh {{.buildroot}}/misc/profile.d_golang.sh

cd {{.inpack__pack_dir}}/deps
rm -rf go

%files

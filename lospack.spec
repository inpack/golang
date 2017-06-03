project.name = golang
project.version = 1.8.3
project.vendor = golang.org
project.homepage = https://golang.org/
project.groups = dev/sys-runtime
project.description = open source programming language that makes it easy to build simple, reliable, and efficient software.

%build
PREFIX="{{.project__prefix}}"

cd {{.lospack__pack_dir}}/deps

if [ ! -f "go1.8.3.linux-amd64.tar.gz" ]; then
    wget https://storage.googleapis.com/golang/go1.8.3.linux-amd64.tar.gz
fi
if [ ! -d "go" ]; then
    tar -zxf go1.8.3.linux-amd64.tar.gz
fi

cd go

cp -rp bin  {{.buildroot}}/
cp -rp lib  {{.buildroot}}/
cp -rp pkg  {{.buildroot}}/
cp -rp src  {{.buildroot}}/
cp -rp LICENSE   {{.buildroot}}/
cp -rp README.md {{.buildroot}}/
cp -rp VERSION   {{.buildroot}}/


%files

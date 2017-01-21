
startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/maven/maven.spec $RPM_DIR/SPECS/maven.spec

cp ../zips/maven/apache-maven-3.3.9-bin.tar.gz $RPM_DIR/SOURCES/apache-maven-3.3.9-bin.tar.gz


cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/maven.spec

. ${startDir}/copyAndRepo.sh



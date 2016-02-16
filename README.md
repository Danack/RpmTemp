# BastionRPM


An environment for building and deploying RPMS 


## How to use


* `vagrant up` in ./vagrant. Ignore the error message about my private key not being available.

* Download the source files of the things you want to build into the zips directory. e.g. for nginx

./zips/nginx/nginx-1.7.4.tar.gz from http://nginx.org/en/download.html
./zips/nginx/nginx-upstream-fair-master.tgz from https://github.com/gnosek/nginx-upstream-fair/archive/master.tar.gz

Or other modules from http://wiki.nginx.org/3rdPartyModules

* Go into the scripts directory and run `sh nginx.sh`.

* Go into the src directory and run `sh sync.sh` - this
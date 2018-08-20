if [ "$#" -ne 1 ] || ! [ -d "$1" ]; then
  echo "Usage: $0 VIRTUAL_ENV_DIRECTORY" >&2
  exit 1
fi
rm -rf lunchtagbot
mkdir -p lunchtagbot
mkdir -p
rsync -avzh ./ lunchtagbot --exclude '***.pyc' --exclude 'lunchtagbot'
rm lunchtagbot/requirements.txt
rm lunchtagbot/build.sh
rsync -avzh $1/lib/python2.7/site-packages/ lunchtagbot
zip -r build.zip lunchtagbot/
rm -rf lunchtagbot

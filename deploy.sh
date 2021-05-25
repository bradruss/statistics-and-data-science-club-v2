rsync -av --rsh=ssh --exclude '.git*' --exclude 'deploy.sh' --exclude 'venv' --exclude 'db.sqlite3' --exclude '.htaccess' \
	  . statclub:django-root/
rsync .htaccess --rsh=ssh statclub:www-root/
rsync -av --rsh=ssh  ../www-root/static statclub:www-root/

Apache Virtual Host/Reverse Proxy
=================================

Since Zope 2.4, VirtualHostMonster is recommended over SiteRoot to put
Zope behind Apache and have all requests be redirected correctly.  In
this case, this will be the URI to use::

    http://localhost:12080/VirtualHostBase/http/www.cmiss.org:80/cmiss/VirtualHostRoot/

For https, this will be the URI::

    http://localhost:12080/VirtualHostBase/https/www.cmiss.org:443/cmiss/VirtualHostRoot/

The full configuration file should be something like::

    <VirtualHost *:80>
        ServerAdmin webmaster@example.org
        ServerName www.cmiss.org
        DocumentRoot /home/zope/cmiss.site/var/www

        # CustomLog /var/log/httpd/cmiss.access.log combined
        # ErrorLog /var/log/httpd/cmiss.error.log

        <Directory />
            AllowOverride None
            Options +FollowSymLinks
            Order allow,deny
            allow from all
        </Directory>

        ProxyPass / http://localhost:8380/VirtualHostBase/http/www.cmiss.org:80/pmr/VirtualHostRoot/
        ProxyPassReverse / http://localhost:8380/VirtualHostBase/http/www.cmiss.org:80/pmr/VirtualHostRoot/
    </VirtualHost>



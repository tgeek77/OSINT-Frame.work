## How to clean up arf.json

### Grep out all of the urls into it's own file. I like copying it to a temp directory first.

```bash
git clone https://github.com/tgeek77/OSINT-Frame.work.git
mkdir ~/temp
cp OSINT-Frame.work/html/arf.json ~/temp

grep http arf.json | sed 's/^[[:space:]]*"url": "//g; s/"$//g' | sort | uniq > urllist.txt
```

You will now have a new file called urllist.txt that contains all of urls in the OSINT Frame.work

### Check them all with grep.

This is going to take some time, so after you start this command, go get some coffee and a good book or two.

```bash
for i in `cat urllist.txt`; do
  code=$(curl -o /dev/null -s -w "%{http_code}" "$i")
  echo "$code $i"
done > url_codes.txt
```

You're now going to have a new text file called `url_codes.txt`.

This file will look like this:

```
404 https://whatbrowser.org/
301 http://browserspy.dk/browser.php
503 http://www.browserscope.org/
000 https://proxycheck.haschek.at/
200 https://www.ip2proxy.com/
200 https://noscript.net/
200 https://github.com/amq/firefox-debloat
200 https://browserleaks.com/
404 https://addons.mozilla.org/en-US/firefox/addon/self-destructing-cookies/
```

Here are some of the most standard http status codes:

- 200 OK - The most common success response, indicating the request was successful.
- 404 Not Found - Extremely common when a URL is mistyped or a resource has been moved/removed.
- 301 Moved Permanently - Frequently used for URL redirection, especially when websites change their structure.
- 302 Found (or 307 Temporary Redirect) - Common for temporary redirects, often used after form submissions or during maintenance.
- 500 Internal Server Error - The generic "something went wrong" error that occurs when an unexpected condition was encountered.
- 403 Forbidden - Used when the server understands the request but refuses to authorize it.
- 400 Bad Request - Common when the client sends a malformed request syntax or invalid request message framing.
- 401 Unauthorized - Frequently seen when authentication is required but has failed or not been provided.
- 503 Service Unavailable - Often appears during server maintenance or when a server is overloaded.
- 204 No Content - Common in APIs when a request was successful but there's no content to return.

One more specifically for curl:

- 000 - This means that there is no response at all. There is no server at this url

### Cleaning up

* If you see a url with **000** or **404**, then this should probably be removed unless you know they have changed addresses. If the website is just informational and not a search or other similar tool, then there's no harm in updating the url with an archive and marking the link as (a).

* **401** means that the page is no longer available to the internet without credentials. These may need to be removed because if you can't use them, then why link to them.

* An error **500** typically means that the website is having problems. It could be temporary or if it is happening for a long time, it could mean that the project is abandoned. 

* **200** is typically what you want to see. **301** is pretty normal and the link should probably still work fine.


# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(True)

# List of URLs to host blocklists for the host blocker.  Only used when
# the simple host-blocker is used (see `content.blocking.method`).  The
# file can be in one of the following formats:  - An `/etc/hosts`-like
# file - One host per line - A zip-file of any of the above, with either
# only one file, or a file   named `hosts` (with any extension).  It's
# also possible to add a local file or directory via a `file://` URL. In
# case of a directory, all files in the directory are read as adblock
# lists.  The file `~/.config/qutebrowser/blocked-hosts` is always read
# if it exists.
# Type: List of Url
c.content.blocking.hosts.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']

# List of URLs to ABP-style adblocking rulesets.  Only used when Brave's
# ABP-style adblocker is used (see `content.blocking.method`).  You can
# find an overview of available lists here:
# https://adblockplus.org/en/subscriptions - note that the special
# `subscribe.adblockplus.org` links aren't handled by qutebrowser, you
# will instead need to find the link to the raw `.txt` file (e.g. by
# extracting it from the `location` parameter of the subscribe URL and
# URL-decoding it).
# Type: List of Url
c.content.blocking.adblock.lists = [ \
        "https://easylist.to/easylist/easylist.txt", \
        "https://easylist.to/easylist/easyprivacy.txt", \
        "https://easylist-downloads.adblockplus.org/antiadblockfilters.txt", \
        "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt", \
        "https://secure.fanboy.co.nz/fanboy-annoyance.txt", \
        "https://secure.fanboy.co.nz/r/fanboy-ultimate.txt", \
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt", \
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt", \
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt", \
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt", \
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt", \
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt" \
        ]

config.bind(',m', 'spawn ~/.local/bin/umpv {url}')
config.bind(',M', 'hint links spawn ~/.local/bin/umpv {hint-url}')
config.bind(';M', 'hint --rapid links spawn ~/.local/bin/umpv {hint-url}')

config.set('hints.mode', 'word')
config.set('hints.auto_follow_timeout', 200)

config.set('colors.webpage.preferred_color_scheme', 'dark')
config.set('colors.webpage.bg', 'black')

c.aliases['proxy-mitm'] = 'set content.proxy http://127.0.0.1:8080/'
c.aliases['noproxy'] = 'set content.proxy none'

mycursor = None
mydb = None
recipient_minimum = None
tip_bot_username = None
excluded_redditors = None
program_minimum = None
reddit = None
donate_commands = None

comment_footer = """\n\n
***\n\n
[*^(Nano)*](https://nano.org)*^( | )*
[*^(Nano Tipper)*](https://github.com/danhitchcock/nano_tipper_z)*^( | )*
[*^(Free Nano!)*](https://nanolinks.info/#faucets-free-nano)*^( | )*
[*^(Spend Nano)*](https://usenano.org/)*^( | )*
[*^(Nano Links)*](https://nanolinks.info/)"""

help_text = """
Help from Nano Tipper! This bot was handles tips via the Nano cryptocurrency.
[Visit us on GitHub](https://github.com/danhitchcock/nano_tipper_z), the [Wiki](http://reddit.com/r/nano_tipper/wiki/) 
or /r/nano_tipper for more information on its use and its status. Be sure to read the 
[Terms of Service](https://github.com/danhitchcock/nano_tipper_z#terms-of-service)\n\n

Nano Tipper works in two ways -- either publicly tip a user on a subreddit, or send a PM to /u/nano_tipper with a PM command below.\n\n
To tip 0.1 Nano on a comment or post on a [tracked subreddit](https://www.reddit.com/r/nano_tipper/comments/astwp6/nano_tipper_status/), make a comment starting with:\n
    !nano_tip 0.1
    -or-
    !ntip 0.1\n
To tip anywhere on reddit, tag the bot as such (it won't post on the all subreddits, but it will PM the users):\n
    /u/nano_tipper 0.1
You can tip any amount above the program minimum of 0.0001 Nano.\n\n

For PM commands, create a new message with any of the following commands (be sure to remove the quotes, '<'s and '>'s):\n
    'create' - Create a new account if one does not exist
    'send <amount or all> <user/address>' - Send Nano to a reddit user or an address
    'balance' or 'address' - Retrieve your account balance. Includes both pocketed and unpocketed transactions
    'minimum <amount>' - (default 0.0001) Sets a minimum amount for receiving tips
    'silence <yes/no>' - (default 'no') Prevents the bot from sending you tip notifications or tagging in posts 
    'history <optional: number of records>' - Retrieves tipbot commands. Default 10, maximum is 50.
    'percentage <percent>' - (default 10 percent) Sets a percentage of returned tips to donate to TipBot development
    'help' - Get this help message\n
If you wanted to send 0.01 Nano to zily88, reply:\n
    send 0.01 zily88\n
If you have any questions or bug fixes, please contact /u/zily88."""

welcome_create = """
Welcome to Nano Tipper, a reddit tip bot which allows you to tip and send the Nano Currency to your favorite redditors! 
Your account is **active** and your Nano address is %s. By using this service, you agree 
to the [Terms of Service](https://github.com/danhitchcock/nano_tipper_z#terms-of-service).\n\n

You will be receiving a tip of 0.001 Nano as a welcome gift! To load more Nano, try any of the the free 
[Nano Faucets](https://nanolinks.info/#faucets-free-nano), or deposit some (click on the Nanode link for a QR code), 
or receive a tip from a fellow redditor!\n\n
***\n\n
Nano Tipper can be used in two ways. The most common is to tip other redditors publicly by replying to a comment on a 
[tracked subreddit](https://www.reddit.com/r/nano_tipper/comments/astwp6/nano_tipper_status/). 
To tip someone 0.01 Nano, reply to their message with:\n\n
```!ntip 0.01```\n\n
To tip a redditor on any subreddit, tag the bot instead of issuing a command:\n\n
```/u/nano_tipper 0.01```\n\n
In unfamiliar subreddits, the minimum tip is 1 Nano.\n\n
***\n\n
There are also PM commands by [messaging](https://reddit.com/message/compose/?to=nano_tipper&subject=command&message=type_command_here) /u/nano_tipper. Remove any quotes, <'s and >'s.\n\n
```send <amount> <valid_nano_address>``` Withdraw your Nano to your own wallet.\n\n
```send <amount> <redditor username>``` Send to another redditor.\n\n
```minimum <amount>``` Prevent annoying spam by setting a receiving tip minimum.\n\n
```balance``` Check your account balance.\n\n
```help``` Receive an in-depth help message.\n\n

View your account on (the block explorer)[https://nanocrawler.cc/explorer/account/%s].\n\n
If you have any questions, please post at /r/nano_tipper
"""

welcome_tipped = """
Welcome to Nano Tipper, a reddit tip bot which allows you to tip and send the Nano Currency to your favorite redditors! 
You have just received a Nano tip in the amount of ```%s Nano``` at your address %s.\n\n
By using this service, you agree to the [Terms of Service](https://github.com/danhitchcock/nano_tipper_z#terms-of-service). Please activate your account by 
replying to this message or any tips which are 30 days old will be returned to the sender.\n\n
To load more Nano, try any of the the free 
[Nano Faucets](https://nanolinks.info/#faucets-free-nano), or deposit some (click on the Nano Crawler link for a QR code).\n\n
***\n\n
Nano Tipper can be used in two ways. The most common is to tip other redditors publicly by replying to a comment on a 
[tracked subreddit](https://www.reddit.com/r/nano_tipper/comments/astwp6/nano_tipper_status/). 
To tip someone 0.01 Nano, reply to their message with:\n\n
```!ntip 0.01```\n\n
To tip a redditor on any subreddit, tag the bot instead of issuing a command:\n\n
```/u/nano_tipper 0.01```\n\n
In unfamiliar subreddits, the minimum tip is 1 Nano.\n\n
***\n\n
There are also PM commands by [messaging](https://reddit.com/message/compose/?to=nano_tipper&subject=command&message=type_command_here) /u/nano_tipper. Remove any quotes, <'s and >'s.\n\n
```send <amount> <valid_nano_address>``` Withdraw your Nano to your own wallet.\n\n
```send <amount> <redditor username>``` Send to another redditor.\n\n
```minimum <amount>``` Prevent annoying spam by setting a receiving tip minimum.\n\n
```balance``` Check your account balance.\n\n
```help``` Receive an in-depth help message.\n\n

View your account on Nano Crawler: https://nanocrawler.cc/explorer/account/%s\n\n
If you have any questions, please post at /r/nano_tipper
"""

new_tip = """
Somebody just tipped you %s Nano at your address %s. Your new account balance is:\n\n
Available: %s Nano\n\n
Unpocketed: %s Nano\n\n  
Unpocketed Nanos will be pocketed automatically. [Transaction on Nano Crawler](https://nanocrawler.cc/explorer/block/%s)\n\n
To turn off these notifications, reply with "silence yes".
"""
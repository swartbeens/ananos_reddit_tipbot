import shared
from shared import from_raw, NumberUtil

COMMENT_FOOTER = """\n\n
***\n\n
[*^(Ananos)*](https://ananos.express)*^( | )*
[*^(Ananos Tipper)*](https://github.com/swartbeens/ananos_reddit_tipbot)*^( | )*
[*^(Opt Out)*](https://reddit.com/message/compose/?to=ana_tipbot&subject=command&message=opt-out)
"""

HELP = """
Help from Ananos Tipper! This bot handles tips via the [Ananos](https://ananos.express) currency.
[Visit us on GitHub](https://github.com/swartbeens/ananos_reddit_tipbot) or /r/ana_tipbot for more information on its use and its status. Be sure to read the 
[Terms of Service](https://github.com/swartbeens/ananos_reddit_tipbot#terms-of-service)\n\n

If you do not accept the Terms of Service, or do not wish to participate, please respond with the text `opt-out`.\n\n

Ananos Tipper works in two ways -- either publicly tip a user on a subreddit, or send a PM to /u/ana_tipbot with a PM command below.\n\n
To tip 1.2 Ananos on a comment or post on a [tracked subreddit](https://www.reddit.com/r/ana_tipbot/comments/astwp6/ana_tipbot_status/), make a comment starting with:\n
    !ana 1.2
To tip anywhere on reddit, tag the bot as such (it won't post on the all subreddits, but it will PM the users):\n
    /u/ana_tipbot 0.1
You can tip any amount above the program minimum of 1 Ananos.\n\n

For PM commands, create a new message with any of the following commands (be sure to remove the quotes, '<'s and '>'s):\n
    'create' - Create a new account if one does not exist
    'send <amount or all> <user/address>' - Send Ananos to a reddit user or an address
    'balance' or 'address' - Retrieve your account balance.
    'silence <yes/no>' - (default 'no') Prevents the bot from sending you tip notifications or tagging in posts 
    'history <optional: number of records>' - Retrieves tipbot commands. Default 10, maximum is 50.
    'opt-out' - Disables your account. 
    'opt-in' - Re-enables your account. 
    'help' - Get this help message\n
If you wanted to send 1.2 Ananos to rambamtyfus, reply:\n
    send 1.1 rambamtyfus\n
If you have any questions or bug fixes, please reach out on the [Ananos subreddit](https://reddit.com/r/Ananos)."""

WELCOME_CREATE = """
Welcome to Ananos Tipper, a reddit tip bot which allows you to tip and send the [Ananos](https://Ananos.cc) Currency to your favorite redditors! 
Your account is **active** and your Ananos address is `%s`. By using this service, you agree 
to the [Terms of Service](https://github.com/swartbeens/ananos_reddit_tipbot#terms-of-service).\n\n

If you do not accept the Terms of Service, or do not with to participate, please respond with the text `opt-out`.\n\n

***\n\n
Ananos Tipper can be used in two ways. The most common is to tip other redditors publicly by replying to a comment on a 
[tracked subreddit](https://www.reddit.com/r/ana_tipbot/comments/astwp6/ana_tipbot_status/). 
To tip someone 1 Ananos, reply to their message with:\n\n
```!ana 1```\n\n
To tip a redditor on any subreddit, tag the bot instead of issuing a command:\n\n
```/u/ana_tipbot 1```\n\n
In unfamiliar subreddits, the minimum tip is 1 Ananos.\n\n
***\n\n
There are also PM commands by [messaging](https://reddit.com/message/compose/?to=ana_tipbot&subject=command&message=type_command_here) /u/ana_tipbot. Remove any quotes, <'s and >'s.\n\n
```send <amount> <valid_bannano_address>``` Withdraw your Ananos to your own wallet.\n\n
```send <amount> <redditor username>``` Send to another redditor.\n\n
```balance``` Check your account balance.\n\n
```help``` Receive an in-depth help message.\n\n

View your account on [the block explorer](https://creeper.Ananos.cc/explorer/account/%s).\n\n
If you have any questions, please post at /r/ana_tipbot
"""

WELCOME_TIP = """
Welcome to Ananos Tipper, a reddit tip bot which allows you to tip and send the [Ananos](https://Ananos.cc) Currency to your favorite redditors! 
You have just received a Ananos tip in the amount of ```%s BAN``` at your address `%s`.\n\n
By using this service, you agree to the [Terms of Service](https://github.com/swartbeens/ananos_reddit_tipbot#terms-of-service).\n\n

If you do not accept the Terms of Service, or do not with to participate, please respond with the text `opt-out`.\n\n
***\n\n
Ananos Tipper can be used in two ways. The most common is to tip other redditors publicly by replying to a comment on a 
[tracked subreddit](https://www.reddit.com/r/ana_tipbot/comments/astwp6/ana_tipbot_status/). 
To tip someone 1 Ananos, reply to their message with:\n\n
```!ana 1```\n\n
To tip a redditor on any subreddit, tag the bot instead of issuing a command:\n\n
```/u/ana_tipbot 1```\n\n
In unfamiliar subreddits, the minimum tip is 1 Ananos.\n\n
***\n\n
There are also PM commands by [messaging](https://reddit.com/message/compose/?to=ana_tipbot&subject=command&message=type_command_here) /u/ana_tipbot. Remove any quotes, <'s and >'s.\n\n
```send <amount> <valid_Ananos_address>``` Withdraw your Ananos to your own wallet.\n\n
```send <amount> <redditor username>``` Send to another redditor.\n\n
```balance``` Check your account balance.\n\n
```help``` Receive an in-depth help message.\n\n

View your account on the block explorer: https://creeper.Ananos.cc/explorer/account/%s\n\n
If you have any questions, please post at /r/ana_tipbot
"""

NEW_TIP = """
Somebody just tipped you %s BAN at your address `%s`. Your new juicy account balance is:\n\n
**%s Ananos**\n\n
[View this transaction on Creeper](https://creeper.Ananos.cc/explorer/block/%s)\n\n
To turn off these notifications, reply with "silence yes".
"""

SUBJECTS = {
    "first_tip": "Ananos Tipper - Congrats on receiving your first Ananos Tip!",
    "new_tip": "Ananos Tipper - You just received a new Ananos tip!",
    "help": "Ananos Tipper - Help",
    "balance": "Ananos Tipper - Account Balance",
    "minimum": "Ananos Tipper - Tip Minimum",
    "create": "Ananos Tipper - Create",
    "send": "Ananos Tipper - Send",
    "history": "Ananos Tipper - History",
    "silence": "Ananos Tipper - Silence",
    "subreddit": "Ananos Tipper - Subreddit",
    "opt-out": "Ananos Tipper - Opt Out",
    "opt-in": "Ananos Tipper - Opt In",
    "success": "Ananos Tipper - Your Tip Was Successful",
    "failure": "Ananos Tipper - You Tip Did Not Go Through",
    "convert": "Ananos Tipper - Your Currency Conversion",
}

MINIMUM = {
    "set_min": "Updating tip minimum to %s",
    "below_program": "Did not update. The amount you specified is below the program minimum "
    "of %s Ananos.",
    "parse_error": "I couldn't parse your command. I was expecting 'minimum "
    "<amount>'. Be sure to check your spacing.",
}

NAN = "'%s' didn't look like a number to me. If it is blank, there might be extra spaces in the command."

ACCOUNT_MAKE_ERROR_ERROR = "I've experienced an error creating your account, please check with my owner or try again later."
TIP_CREATE_ACCT_ERROR = "I failed to create an account for your intended recipient, please check with my owner or try again later."

# full responses
SEND_TEXT = {
    10: (
        "Sent ```%s BAN``` to /u/%s\n\n[View this transaction on Creeper](https://creep"
        "er.Ananos.cc/explorer/block/%s)"
    ),
    11: (
        "Sent ```%s BAN``` to %s\n\n[View this transaction on Creeper](https://creep"
        "er.Ananos.cc/explorer/block/%s)"
    ),
    20: (
        "Creating a new account for /u/%s and "
        "sending ```%s BAN```.\n\n[View this transaction on Creeper](https://creeper.Ananos.cc"
        "/explorer/block/%s)"
    ),
    30: "Sent ```%s BAN``` to address `%s`\n\n[View this transaction on Creeper](https://creep"
    "er.Ananos.cc/explorer/block/%s)",
    100: (
        "You don't have an account yet. Please PM me with `create` in the body to "
        "make an account."
    ),
    110: "You must specify an amount and a user, e.g. `send 1 ana_tipbot`.",
    111: "Too many arguments specified.",
    120: "I could not read the amount. Is '%s' a number?",
    130: "Program minimum is %s Ananos.",
    150: "Your tip is below the minimum for an unfamiliar sub.",
    160: "You have insufficient funds. Please check your balance.",
    170: "'%s' is neither a redditor nor a valid address.",
    180: (
        "Sorry, the user has set a tip minimum of %s. "
        "Your tip of %s is below this amount."
    ),
    190: "Sorry, the user has opted-out of using Ananos Tipper.",
    200: "You cannot send to yourself."
}

# for subreddits who like minimal response, or 2nd level responses
SEND_TEXT_MIN = {
    10: (
        "^[Sent](https://creeper.Ananos.cc/explorer/block/%s) ^%s ^BAN ^to ^(/u/%s) ^- "
        "[^(Ananos Tipper)](https://github.com/swartbeens/ananos_reddit_tipbot)"
    ),
    11: (
        "^[Sent](https://creeper.Ananos.cc/explorer/block/%s) ^%s ^BAN ^to ^%s ^- [^(Bana"
        "no Tipper)](https://github.com/swartbeens/ananos_reddit_tipbot)"
    ),
    20: (
        "^(Made a new account and )^[sent](https://creeper.Ananos.cc/explorer/block/%s) ^%s ^BAN ^to ^(/u/%s) ^- [^(Bana"
        "no Tipper)](https://github.com/swartbeens/ananos_reddit_tipbot)"
    ),
    100: (
        "^(Tip not sent. Error code )^[%s](https://github.com/swartbeens/ananos_reddit_tipbot"
        "#error-codes) ^- [^(Ananos Tipper)](https://github.com/swartbeens/ananos_reddit_tipbot)"
    ),
}

OPT_IN = """
Welcome back! You have opted back in. Your account will be restored with the same address."""

OPT_OUT = """
You have opted-out and I promise not to bother you anymore.\n\n
If this was in error, please respond with the text `opt-in`.
"""

SUBREDDIT = {
    "missing": "Your command seems to be missing something. Make sure it follow the format `subreddit <subreddit> "
    "<command> <option>.`",
    "not_mod": "You are not a moderator of /r/%s.",
    "minimum": "Sucessfully set your /r/%s minimum to %s, active immediately.",
    "deactivate": "Within 5 minutes, tipping will be deactivated in your subreddit %s.",
    "activate": "Within 5 minutes, the Ananos Tipper response in your Subreddit will be set to %s.",
    "error": "There was something wrong with your activate or minimum command.",
    "all": "Here is a list of every subreddit and its status:\n\nName, Status, Minimum\n\n",
    "one": "Here are the settings for subreddit /r/%s:\n\nName, Status, Minimum\n\n",
}

SILENCE = {
    "yes_no": "I did not see 'no' or 'yes' after 'silence'. If you did type "
    "that, check your spacing.",
    "no": "Silence set to 'no'. You will receive tip notifications and be "
    "tagged by the bot in replies.",
    "yes": "Silence set to 'yes'. You will no longer receive tip "
    "notifications or be tagged by the bot.",
    "parse_error": "I couldn't parse your command. I was expecting 'silence "
    "<yes/no>'. Be sure to check your spacing.",
}

NOT_OPEN = (
    "You do not currently have an account open. To create one, "
    "respond with the text 'create' in the message body."
)

ALREADY_EXISTS = (
    "It looks like you already have an account. In any case it is now "
    "**active**. Your Ananos address is `%s`."
    "\n\nhttps://creeper.Ananos.cc/explorer/account/%s"
)

BALANCE = (
    "Your balance at address `%s` is:\n\n"
    "**%s Ananos**"
    "\n\nhttps://creeper.Ananos.cc/explorer/account/%s"
)


def make_response_text(message, response):

    # make a minimal response if (subreddit is tracked) AND (level 2+ or minimal)
    if ("subreddit_status" in response.keys()) and (
        response["subreddit_status"] == "minimal"
        or (str(message.parent_id)[:3] != "t3_")
    ):
        if response["status"] < 100:
            return SEND_TEXT_MIN[response["status"]] % (
                response["hash"],
                NumberUtil.format_float(from_raw(response["amount"])),
                response["recipient"],
            )
        else:
            return SEND_TEXT_MIN[100] % response["status"]

    # otherwise, it will be a full response. Even if hostile/silent (we'll send PMs)
    if response["status"] == 20:
        return SEND_TEXT[response["status"]] % (
            response["recipient"],
            NumberUtil.format_float(from_raw(response["amount"])),
            response["hash"],
        )
    if response["status"] < 100:
        return SEND_TEXT[response["status"]] % (
            NumberUtil.format_float(from_raw(response["amount"])),
            response["recipient"],
            response["hash"],
        )
    if response["status"] in [100, 110, 111, 150, 160, 190, 200]:
        return SEND_TEXT[response["status"]]
    if response["status"] == 120:
        return SEND_TEXT[response["status"]] % response["amount"]
    if response["status"] == 130:
        return SEND_TEXT[response["status"]] % shared.PROGRAM_MINIMUM
    if response["status"] in [170, 210]:
        return SEND_TEXT[response["status"]] % response["recipient"]
    if response["status"] == 180:
        return SEND_TEXT[response["status"]] % (
            NumberUtil.format_float(from_raw(response["minimum"])),
            NumberUtil.format_float(from_raw(response["amount"])),
        )
    if response["status"] == 200:
        return SEND_TEXT[response["status"]]
    return None

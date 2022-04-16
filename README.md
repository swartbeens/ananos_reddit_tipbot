# Ananos Reddit Tipbot
 is a reddit tipping service to easily give Ananos to your favorite redditors! [Ananos](https://Ananos.express) is a feeless, instant, rich in potassium cryptocurrency. Before using Ananos Tipper, please take a look at the [Terms of Service](https://github.com/swartbeens/ananos_reddit_tipbot#terms-of-service)

It is a fork and modification of the [Banano](https://banano.cc/) reddit tipbot created by /u/bbedward - which is available on [GitHub](https://github.com/BananoCoin/banano_reddit_tipbot)

### To get started with Ananos Tipper, either:
A) **Create an account** by [sending a message](https://reddit.com/message/compose/?to=ana_tipbot&subject=command&message=create) to /u/ana_tipbot with 'create' or 'register' in the message body. You will receive a Ananos address, to which you can add Ananos\*.
\-or-
B) **Receive a Ananos tip** from a fellow redditor, and you will automatically have an account made! be sure to activate it afterwards by [sending a message](https://reddit.com/message/compose/?to=ana_tipbot&subject=command&message=create) to /u/ana_tipbot.
Once you have funds in your account, you can tip other redditors, or send to any Ananos address via PM to /u/ana_tipbot.
# Comment Replies:
Ananos Tipper is intended for tipping on reddit posts and replies.

On supported subreddits, you can send a tip like this:

    !ana 1 This is great!

This will tip a redditor 1 Ananos. !bam <amount> must be the first thing in your message OR the last thing. Such, this is also a valid tip:

    This is great! !ana 1

Or from anywhere on reddit, you can tip a commenter by:

    /u/ana_tipbot 1 This is great!
   
or

    This is great! /u/ana_tipbot 1

If the subreddit is a friendly subreddi, the bot will repsond with a message. If the subreddit is not friendly, a PM will be sent to both the sender and the recipient.
    
# Private Messages

Ananos Tipper also works by PM. [Send a message](https://reddit.com/message/compose/?to=ana_tipbot&subject=command&message=type_command_here) to /u/ana_tipbot for a variety of actions.

To send 1 Ananos to bbedward, include this text in the message body:

    send 1 /u/bbedward
-or-

    send 1 bbedward

To send 1 Ananos to ana_36um149df9qi33eogxdecp9g5sw8mebgpg73ibsstbe363c7j95ghso8igrh, include this text in the message body:

    send 1 ana_36um149df9qi33eogxdecp9g5sw8mebgpg73ibsstbe363c7j95ghso8igrh

or send all your balance:

    send all ana_36um149df9qi33eogxdecp9g5sw8mebgpg73ibsstbe363c7j95ghso8igrh

There are many other commands.

```
'balance' or 'address' - Retrieve your account balance.
'create' - Create a new account if one does not exist
'help' - Get this help message
'history <optional: number of records>' - Retrieves tipbot commands. Default 10, maximum is 50.
'send <amount or all, optional: Currency> <user/address>' - Send Ananos to a reddit user or an address
'silence <yes/no>' - (default 'no') Prevents the bot from sending you tip notifications or tagging in posts
'subreddit <subreddit> <'activate'/'deactivate'> <option>' - Subreddit Moderator Controls - Enabled Tipping on Your Sub (`silent`, `minimal`, `full`)
'withdraw <amount or all> <user/address>' - Same as send
'opt-out' - Disables your account.
'opt-in' - Re-enables your account.
```
### Control TipBot Behavior On Your Subreddit
If you are a moderator of a subreddit, and would like to tipping to your sub, use the `subreddit` command. For example, for me to activate tipping on my /r/ana_tipbot subreddit, I send a PM to the bot saying:

`subreddit ana_tipbot activate`

This will allow the bot to look for !ana commands and respond to posts. 
-or- If I don't want the bot to respond, but still want tips:

`subreddit ana_tipbot activate silent`

-or- for a cleaner tipbot response:

`subreddit ana_tipbot activate minimal`

To deactivate, simply PM

`subreddit ana_tipbot deactivate`

### Here's a few other great links:
[Ananos Subreddit](https://reddit.com/r/Ananos) -- Post any questions about Ananos Tipper
[Ananos](https://Ananos.express) -- The Ananos website
[Kalium](https://ananault.lightcord.org/ -- The Ananos wallet

# Terms of Service
* Do not keep a lot of Ananos in your tip bot account! The tip bot is for tipping small amounts ONLY.

  

* You accept the risks of using this tip bot -- We won't steal your Ananos, but they might be lost at any point, and we are at no obligation to replace them. Don't put in more than you're willing to lose.

  

* We are under no obligation to provide support. The tip bot is not a custodial service.

  

* Any consequences of tipping are the responsibility of the users using this service.

 
 
* This software is provided "as is" and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. In no event shall the copyright holder or contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.

# FAQ
## Why does the message have to start or end with !ana <amount>?
This is to prevent unintentional tips! If the program simply scanned the entire comment, a user might accidentally quote someone else's tip command in a response. In the future I might change this, but for now it's the best way to ensure the program behaves as expected.

## Are my funds safe?
**NO! Unless you and you alone control your private keys, your funds are never safe!** Please don't keep more than a small dose of potassium on the tipbot at any time! While I'm not going to steal your Ananoss, this program is in early beta testing and weird things could happen, including lost Ananoss! **Use at your own risk!** (sorry for all the exclamation marks)

## I sent a tip to the wrong address. Can I get it back?
If the address isn't affiliated with a Redditor, **No.** We only have private keys for redditors, not for external addresses.

## I sent a tip to the wrong redditor. Can I get it back?
Your best bet is to try to reach out to the redditor and ask for it back. Do not harass other redditors or do anything that would violate Reddit's Terms of Service.

## Have you implemented any spam prevention for your bot?
Users are allowed 5 requests every 30 seconds. If you do more than that, the bot ignores you until 30 seconds have passed.

## I tried to send a tip, but received no response. Did it go through?
Probably not. It's most likely the bot was temporarily disconnected. If a command is issued while the bot is offline, the command will not be seen. If no response is received from the bot after a few minutes, send a message to the bot with the text 'history'. If you get a response and the tip isn't in your history, that means it wasn't seen. If you don't get a response, the bot is probably still offline. Try again in a few minutes.

## I found a bug or I have a concern. Question Mark?
Post on the [Ananos subreddit](https://reddit.com/r/Ananos) or reach on on the [Discord](https://chat.Ananos.cc)

# Error Codes
If a reddit tip is a reply to a reply, it's better to keep a short message with an error code.
* 100 - You do not have an account -- Create an account by typing 'create' or by receiving a tip from another redditor.
* 110 - You must specify an amount and a user, e.g. `send 1 ana_tipbot`.
* 120 - Could not read the tip amount -- use either a number or the word 'all'.
* 130 - Tip amount is below program minimum -- This is to prevent spamming other redditors.
* 150 - This subreddit does not accept tips this small, increase your tip or send the bot `subreddit subreddit_name` to see what the minimum is.
* 160 - You have insufficient funds.
* 190 - The recipient has disabled tipping for their account.
* 200 - You have tried to tip your own comment or withdraw to your own account, which is not allowed.
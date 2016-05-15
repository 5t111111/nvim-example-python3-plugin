import neovim
from slackclient import SlackClient

@neovim.plugin
class Main(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command("PostToSlack", range='')
    def post_to_slack(self, range):
        b = self.nvim.current.buffer
        lines = b[(range[0]-1):range[1]]

        text = "\n".join(lines)

        self.nvim.command('echo "Sending it to Slack"')

        token = self.nvim.eval('g:slack_api_token')
        channel = self.nvim.eval('g:slack_post_channel')
        self.nvim.command('echo "%s"' % token)
        sc = SlackClient(token)
        sc.api_call(
            'chat.postMessage',
            channel=channel,
            text=text,
            username='vimbot',
            icon_emoji=':vim:'
        )

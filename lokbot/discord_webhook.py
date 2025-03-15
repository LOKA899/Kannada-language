import json
import httpx
from loguru import logger


class DiscordWebhook:

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.client = httpx.Client()

    def send_message(self, content, embed=None):
        """
        Send a message to Discord webhook
        """
        payload = {"content": content}

        if embed:
            payload["embeds"] = [embed]

        response = self.client.post(self.webhook_url, json=payload)

        if response.status_code != 204:
            logger.error(
                f"Failed to send Discord webhook: {response.status_code} {response.text}"
            )
            return False

        return True

    def send_object_log(self,
                        obj_type,
                        code,
                        level,
                        location,
                        status,
                        occupied_info=""):
        """
        Send formatted object log to Discord
        """
        # Custom server emojis
        CRYSTAL_EMOJI = "<:crystal_mine:>"  # Crystal Mine custom emoji
        DRAGON_EMOJI = "<:dragon_soul:>"   # Dragon Soul custom emoji
        DEFAULT_EMOJI = "🎯"  # Default resource emoji

        # Set color based on resource type
        if "Crystal Mine" in obj_type:
            color = 0xFF0000  # Crystal Red color
            title = f"{CRYSTAL_EMOJI} **Crystal Mine Found!**"
        elif "Dragon Soul Cavern" in obj_type:
            color = 0xFFD700  # Gold color
            title = f"{DRAGON_EMOJI} **Dragon Soul Cavern Found!**"
        else:
            color = 0x3498DB  # Default blue color
            title = f"{DEFAULT_EMOJI} Resource Found"

        embed = {
            "title": title,
            "description": f"**Type:** {obj_type}",
            "color":
            color,
            "fields": [{
                "name": "Code",
                "value": str(code),
                "inline": True
            }, {
                "name": "Level",
                "value": str(level),
                "inline": True
            }, {
                "name": "Location",
                "value": str(location),
                "inline": True
            }, {
                "name": "Status",
                "value": status,
                "inline": True
            }]
        }

        if occupied_info:
            embed[
                "description"] = f"**Occupied Information:**\n{occupied_info}"

        return self.send_message("", embed)

    def send_all_resources(self,
                           obj_type,
                           code,
                           level,
                           location,
                           status,
                           occupied_info=""):
        """
        Send all resources to a separate webhook regardless of type or level
        """
        # Custom server emojis
        CRYSTAL_EMOJI = "<:crystal_mine:>"  # Crystal Mine custom emoji
        DRAGON_EMOJI = "<:dragon_soul:>"   # Dragon Soul custom emoji
        DEFAULT_EMOJI = "🎯"  # Default resource emoji

        # Set color based on resource type
        if "Crystal Mine" in obj_type:
            color = 0xFF0000  # Crystal Red color
            title = f"{CRYSTAL_EMOJI} **Crystal Mine Found!**"
        elif "Dragon Soul Cavern" in obj_type:
            color = 0xFFD700  # Gold color
            title = f"{DRAGON_EMOJI} **Dragon Soul Cavern Found!**"
        else:
            color = 0x3498DB  # Default blue color
            title = f"{DEFAULT_EMOJI} Resource Found"

        embed = {
            "title": title,
            "description": f"**Type:** {obj_type}",
            "color":
            color,
            "fields": [{
                "name": "Code",
                "value": str(code),
                "inline": True
            }, {
                "name": "Level",
                "value": str(level),
                "inline": True
            }, {
                "name": "Location",
                "value": str(location),
                "inline": True
            }, {
                "name": "Status",
                "value": status,
                "inline": True
            }]
        }

        if occupied_info:
            embed[
                "description"] = f"**Occupied Information:**\n{occupied_info}"

        return self.send_message("", embed)
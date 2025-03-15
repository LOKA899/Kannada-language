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
        # Set color based on status
        if "Available" in status:
            color = 0x00FF00  # Green color
        else:
            color = 0xFF0000  # Red color for occupied

        # Set title and thumbnail based on type
        if "Crystal Mine" in obj_type:
            title = "**Crystal Mine Found!**"
            thumbnail_url = "https://media.discordapp.net/attachments/1349663748339531837/1350496588614602752/crystal_mine.png"
        elif "Dragon Soul Cavern" in obj_type:
            title = "**Dragon Soul Cavern Found!**"
            thumbnail_url = "https://media.discordapp.net/attachments/1349663748339531837/1350496589139148810/dragon_soul.png"
        else:
            title = "Resource Found"

        embed = {
            "title": title,
            "description": f"**Type:** {obj_type}",
            "color":
            color,
            "thumbnail": {
                "url": thumbnail_url
            },
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
        # Set color based on status
        if "Available" in status:
            color = 0x00FF00  # Green color
        else:
            color = 0xFF0000  # Red color for occupied

        # Set title and thumbnail based on type
        if "Crystal Mine" in obj_type:
            title = "**Crystal Mine Found!**"
            thumbnail_url = "https://media.discordapp.net/attachments/1349663748339531837/1350496588614602752/crystal_mine.png"
        elif "Dragon Soul Cavern" in obj_type:
            title = "**Dragon Soul Cavern Found!**"
            thumbnail_url = "https://media.discordapp.net/attachments/1349663748339531837/1350496589139148810/dragon_soul.png"
        else:
            title = "Resource Found"

        embed = {
            "title": title,
            "description": f"**Type:** {obj_type}",
            "color":
            color,
            "thumbnail": {
                "url": thumbnail_url
            },
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
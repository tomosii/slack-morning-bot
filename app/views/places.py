from app.models.place import Place


def text():
    return f"朝活のチェックイン場所一覧です！"


def blocks(places: list[Place]) -> list[dict]:
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "チェックイン対応エリア一覧です！",
            },
        },
       {
			"type": "context",
			"elements": [
				{
					"type": "mrkdwn",
					"text": f":round_pushpin:  *{place.name}*",
				}
			]
		}
        for place in places if place.enabled
    ]

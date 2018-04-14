#!/usr/bin/env python3
""" this script will take any playlist that uploaded videos using the uploader and link the matches to TBA"""

import simplejson as json
import youtubeup
from youtubeAuthenticate import *
from youtubeup import post_video, quarters_match_code, semis_match_code, finals_match_code, tiebreak_mnum

PID = input("Playlist ID: ")
TBAID = input("TBA ID: ")
TBASECRET = input("TBA Secret: ")


if (TBAID == "" or TBASECRET == ""):
	print("Can't add to TBA without ID and Secret")
	sys.exit(0)

youtube = get_youtube_service()

playlistitems_list = youtube.playlistItems().list(
    playlistId=PID,
    part="snippet",
    maxResults=50
).execute()

print("got list")
nextPageToken = playlistitems_list["nextPageToken"]
while ('nextPageToken' in playlistitems_list):
    print("getting next page")
    nextPageList = youtube.playlistItems().list(
        playlistId=PID,
        part="snippet",
        maxResults=50,
        pageToken=nextPageToken).execute()
    print("got next page")
    playlistitems_list["items"] = playlistitems_list["items"] + \
        nextPageList["items"]
    if "nextPageToken" not in nextPageList:
        playlistitems_list.pop('nextPageToken', None)
        print("no more pages")
    else:
        nextPageToken = nextPageList['nextPageToken']
        print("got next page token")
        # Print information about each video.

for playlist_item in playlistitems_list["items"]:
    title = str(playlist_item["snippet"]["title"])
    video_id = str(playlist_item["snippet"]["resourceId"]["videoId"])
    if "Qual" in title:
        mnum = "qm{}".format(title[-3:].split(" ")[1])
        body = json.dumps({mnum: video_id})
        post_video(TBAID, TBASECRET, body, ecode, "match_videos")
    elif "Quarterfinal" in title:
        num = int(title[-3:].split(" ")[1])
        if "Tiebreak" in title:
            num = tiebreak_mnum(num, "qf")
        mnum = quarters_match_code("qf", num)
        body = json.dumps({mnum: video_id})
        post_video(TBAID, TBASECRET, body, ecode, "match_videos")
    elif "Semifinal" in title:
        num = int(title[-3:].split(" ")[1])
        if "Tiebreak" in title:
            num = tiebreak_mnum(num, "sf")
        mnum = semis_match_code("sf", num)
        body = json.dumps({mnum: video_id})
        post_video(TBAID, TBASECRET, body, ecode, "match_videos")
    elif "Final" in title:
        num = int(title[-3:].split(" ")[1])
        if "Tiebreak" in title:
            num = tiebreak_mnum(num, "f1m")
        mnum = finals_match_code("f1m", num)
        body = json.dumps({mnum: video_id})
        post_video(TBAID, TBASECRET, body, ecode, "match_videos")
    else:
        print("I don't know what this is")
        print(title)
        print(video_id)
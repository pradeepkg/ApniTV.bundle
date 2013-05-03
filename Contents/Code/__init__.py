####################################################################################################
# Autor:    Pradeep Kadambar <a href="mailto:pradeep.kadambar@rsa.com">Pradeep Kadambar</a>
# Date:     4/23/2013
# About:    This plugin allows live stream contents from ndtv.com to be viewed over Plex clients.
#
# Version:  0.12
#
# This is free and unencumbered software released into the public domain.
# 
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
# 
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
# 
# For more information, please refer to <http://unlicense.org/>
#
####################################################################################################

NAME = "NDTV"
ICON = "icon-default.gif"
ART = "art-default.gif"

LIVE_URL = "http://www.ndtv.com/video/list/channel"

CHANNELS = {
  "OTHER": 
        {
            "NDTV HINDU":   {
                                "channelUrl": "http://bglive-a.bitgravity.com/ndtv/indhi/live/native",
                                "channelLogo": "http://www.lyngsat-logo.com/logo/tv/nn/ndtv_hindu.jpg"
                            },
            "NDTV GOOD TIMES": {
                                "channelUrl": "http://bglive-a.bitgravity.com/ndtv/prohi/live/native",
                                "channelLogo": "http://www.lyngsat-logo.com/logo/tv/nn/ndtv_good_times.jpg"
                            }
         },
  "MUSIC": 
        {
            "ZOOM TV":      {
                                "channelUrl": "rtmp://cdn.rtmp1.yupptv.tv/nwk app=nwk playpath=zoomtv swfUrl=http://www.yupptv.com/yupptvhdflvplayer/hdplayer.swf swfVfy=true live=true pageUrl=http://www.yupptv.com/account/FlashPlayerFrame.aspx?ChanId=15",
                                "channelLogo": "http://www.lyngsat-logo.com/logo/tv/zz/zoom_tv.jpg"
                            },
            "9XM":          {
                                "channelUrl": "rtmp://210.210.27.37:1935/live/livestream3 swfUrl=http://www.9xm.in/livetv/liveStreamPlayer.swf swfVfy=true live=true",
                                "channelLogo": "http://www.lyngsat-logo.com/logo/tv/num/9xm_in.jpg"
                            }
        },
  "NEWS": 
        {
            "NDTV 24x7":    {
                                "channelUrl": "http://bglive-a.bitgravity.com/ndtv/247lo/live/native",
                                "channelLogo": "http://www.lyngsat-logo.com/logo/tv/nn/ndtv_24x7.jpg"
                            },
            "NDTV PROFIT":  {
                                "channelUrl": "http://bglive-a.bitgravity.com/ndtv/prolo/live/native",
                                "channelLogo": "http://www.lyngsat-logo.com/logo/tv/nn/ndtv_profit.jpg"
                            },
            "NDTV INDIA":   {
                                "channelUrl": "http://bglive-a.bitgravity.com/ndtv/indlo/live/native",
                                "channelLogo": "http://www.lyngsat-logo.com/logo/tv/nn/ndtv_india.jpg"
                            },
            "TIMES NOW":    {
                                "channelUrl": "rtmp://cdn.rtmp1.yupptv.tv/nwk app=nwk playpath=timesnow swfUrl=http://www.yupptv.com/yupptvhdflvplayer/hdplayer.swf swfVfy=true live=true pageUrl=http://www.yupptv.com/account/FlashPlayerFrame.aspx?ChanId=118",
                                "channelLogo": "http://www.lyngsat-logo.com/logo/tv/tt/times_now.jpg"
                            },
            "Al JAZEERA":   {
                                "channelUrl": "rtmp://media2.lsops.net/live/ playpath=aljazeer_en_high.sdp swfUrl=http://www.livestation.com/flash/player/5.4/player.swf pageUrl=http://www.livestation.com/channels/3-al-jazeera-english-english swfVfy=true live=true",
                                "channelLogo": "http://www.lyngsat-logo.com/logo/tv/aa/al_jazeera.jpg"
                            },
            "CNN":          {
                                "channelUrl": "rtmp://media2.lsops.net/live/ playpath=cnn_en_high.sdp swfUrl=http://www.livestation.com/flash/player/5.4/player.swf pageUrl=http://www.livestation.com/channels/66-cnn-international swfVfy=true live=true",
                                "channelLogo": "http://www.lyngsat-logo.com/logo/tv/cc/cnn_usa.jpg"
                            },
            "BBC NEWS":     {
                                "channelUrl": "rtmp://media2.lsops.net/live/ playpath=bbcworld1_en_high.sdp swfUrl=http://www.livestation.com/flash/player/5.4/player.swf pageUrl=http://www.livestation.com/channels/10-bbc-world-news-english swfVfy=true live=true",
                                "channelLogo": "http://www.lyngsat-logo.com/logo/tv/bb/bbc_news.jpg"
                            }
         }
}

# vid == 'LIVE_BG24x7' || vid == 'LIVE_BGINDIA' || vid == 'LIVE_BGGT' || vid == 'LIVE_BGPROFIT' || vid == 'LIVE_BGHINDU' || vid == 'LIVE_SPECIAL' || vid == 'LIVE-SPECIAL') 
LIVE_URLS = {
'BitGravity 400 Kbps': 'http://twit.live-s.cdn.bitgravity.com/cdn-live-s1/_definst_/twit/live/low/playlist.m3u8',
'BitGravity 1 Mbps': 'http://twit.live-s.cdn.bitgravity.com/cdn-live-s1/_definst_/twit/live/high/playlist.m3u8',
'Ustream': 'http://iphone-streaming.ustream.tv/ustreamVideo/1524/streams/live/playlist.m3u8',
'Justin.tv': 'http://usher.justin.tv/stream/multi_playlist/twit.m3u8',
'Flosoft.biz': 'http://hls.twit.tv:1935/flosoft/smil:twitStream.smil/playlist.m3u8'
}
####################################################################################################
def Start():

    # Initialize the plugin
    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")    
    
    # Setup the artwork associated with the plugin
    ObjectContainer.title1 = NAME
    ObjectContainer.art = R(ART)
    ObjectContainer.view_group = 'InfoList'

    DirectoryObject.thumb = R(ICON)
    DirectoryObject.art = R(ART)
    MovieObject.thumb = R(ICON)
    MovieObject.art = R(ART)
    SeasonObject.thumb = R(ICON)
    SeasonObject.art = R(ART)
    NextPageObject.thumb = R(ICON)
    NextPageObject.art = R(ART)    
  
@handler("/video/ndtv", NAME, thumb=ICON, art=ART)
def MainMenu():   

    oc = ObjectContainer(no_cache=True)
    
    for name in LIVE_URLS.keys():
        oc.add(LiveStream(name))    
#     oc = ObjectContainer(title1 = "TEST VIDEOS")        
#     oc.add(
#         EpisodeObject(
#             url = 'http://apni.tv/news/ndtv',
#             title = "TEST VIDEO")
#     )        
# 
#         
    return oc
                
####################################################################################################

def LiveStream(hls_provider='Ustream', include_container=False):
    vco = VideoClipObject(
    key = Callback(LiveStream, hls_provider=hls_provider, include_container=True),
    rating_key = LIVE_URLS[hls_provider],
    title = hls_provider,
    thumb = R('icon-twitlive.png'),
    items = [
    MediaObject(
        parts = [
                 PartObject(key=HTTPLiveStreamURL(LIVE_URLS[hls_provider]))
                 ]
                )
             ]
    )
    
    if include_container:
        return ObjectContainer(objects=[vco])
    else:
        return vco
    
